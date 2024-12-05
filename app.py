import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
import joblib  # Para cargar el escalador
import sqlite3
from datetime import datetime
import pandas as pd

def inicializar_bd():
    conexion = sqlite3.connect("predicciones.db")  # Archivo SQLite
    cursor = conexion.cursor()
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS predicciones (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            region INTEGER,
            tenure INTEGER,
            age INTEGER,
            marital INTEGER,
            address INTEGER,
            income REAL,
            ed INTEGER,
            employ INTEGER,
            retire INTEGER,
            gender INTEGER,
            reside INTEGER,
            clase_predicha INTEGER,
            descripcion TEXT,
            fecha TIMESTAMP
        )
    """)
    conexion.commit()
    conexion.close()

inicializar_bd()

def guardar_prediccion(input_data, clase_predicha, descripcion):
    conexion = sqlite3.connect("predicciones.db")
    cursor = conexion.cursor()
    
    # Agregar fecha actual
    fecha_actual = datetime.now()
    
    # Insertar datos en la tabla
    cursor.execute("""
        INSERT INTO predicciones (
            region, tenure, age, marital, address, income, ed, employ, retire, gender, reside, 
            clase_predicha, descripcion, fecha
        ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (*input_data.flatten(), clase_predicha, descripcion, fecha_actual))
    
    conexion.commit()
    conexion.close()


# Cargar modelo y escalador
@st.cache_resource
def cargar_modelo_y_escalador():
    modelo = load_model("mejor_modelo.h5")
    escalador = joblib.load("scaler.pkl")  # Asegúrate de guardar el escalador
    return modelo, escalador

modelo, escalador = cargar_modelo_y_escalador()

# Diccionario para mapear clases a nombres
clase_nombres = {
    1: "Basic Service",
    2: "E-Service",
    3: "Plus Service",
    4: "Total Service"
}

# Título de la app
st.title("Predicción de Cliente")

# Inputs del usuario
region = st.sidebar.selectbox("Región", ["Region 1", "Region 2", "Region 3"])
tenure = st.sidebar.slider("Tenure (años)", 0, 50, step=1)
age = st.sidebar.slider("Edad", 18, 100, step=1)
marital = st.sidebar.selectbox("Estado civil", ["Soltero", "Casado"])
address = st.sidebar.number_input("Años en la dirección actual", min_value=0, step=1)
income = st.sidebar.number_input("Ingreso anual ($)", min_value=0.0, step=1000.0)
ed = st.sidebar.selectbox("Nivel educativo", [1, 2, 3, 4])
employ = st.sidebar.number_input("Años empleado", min_value=0, step=1)
retire = st.sidebar.selectbox("¿Está retirado?", ["No", "Sí"])
gender = st.sidebar.selectbox("Género", ["Hombre", "Mujer"])
reside = st.sidebar.number_input("Número de personas en la residencia", min_value=1, step=1)

# Mapear variables categóricas
region_map = {"Region 1": 1, "Region 2": 2, "Region 3": 3}
marital_map = {"Soltero": 0, "Casado": 1}

region = region_map[region]
marital = marital_map[marital]

# Mapear inputs categóricos a numéricos
retire = 1 if retire == "Sí" else 0
gender = 1 if gender == "Hombre" else 0

# Crear array de entrada
input_data = np.array([[region, tenure, age, marital, address, income, ed, employ, retire, gender, reside]])

# Escalar los datos
input_data_scaled = escalador.transform(input_data)

# Realizar predicción
if st.button("Predecir"):
    prediccion = modelo.predict(input_data_scaled)
    clase_predicha = np.argmax(prediccion, axis=1)[0] + 1  # Sumar 1 si las clases empiezan en 1
    clase_nombre = clase_nombres[clase_predicha]
    
    # Mostrar resultado en la app
    st.write(f"La clase predicha es: {clase_predicha} - {clase_nombre}")
    
    # Guardar predicción en la base de datos
    guardar_prediccion(input_data, clase_predicha, clase_nombre)
    st.write("Predicción guardada en la base de datos.")

if st.checkbox("Mostrar predicciones almacenadas"):
    conexion = sqlite3.connect("predicciones.db")
    predicciones = pd.read_sql_query("SELECT * FROM predicciones", conexion)
    st.write(predicciones)
    conexion.close()
