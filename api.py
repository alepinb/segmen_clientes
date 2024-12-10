from fastapi import FastAPI
from pydantic import BaseModel
import numpy as np
import joblib

# Inicializar FastAPI
app = FastAPI()

# Cargar el modelo y el escalador
modelo = joblib.load("modelo_logistico.pkl")  # Cargar el modelo logístico
escalador = joblib.load("scaler.pkl")  # Asegúrate de que el escalador también esté guardado

# Diccionario para mapear clases a nombres
clase_nombres = {
    1: "Basic Service",
    2: "E-Service",
    3: "Plus Service",
    4: "Total Service"
}

# Clase para los datos de entrada
class ClienteData(BaseModel):
    region: str
    tenure: int
    age: int
    marital: str
    address: int
    income: float
    ed: int
    employ: int
    retire: str
    gender: str
    reside: int

# Mapeos
region_map = {"Region 1": 1, "Region 2": 2, "Region 3": 3}
marital_map = {"Soltero": 0, "Casado": 1}
retire_map = {"No": 0, "Sí": 1}
gender_map = {"Hombre": 1, "Mujer": 0}

@app.post("/predict/")
def predict(data: ClienteData):
    try:
        # Convertir entradas categóricas a numéricas
        region = region_map[data.region]
        marital = marital_map[data.marital]
        retire = retire_map[data.retire]
        gender = gender_map[data.gender]

        # Crear el array de entrada
        input_data = np.array([[region, data.tenure, data.age, marital, data.address, 
                                data.income, data.ed, data.employ, retire, gender, data.reside]])
        
        # Escalar los datos
        input_data_scaled = escalador.transform(input_data)

        # Hacer predicción
        clase_predicha = int(modelo.predict(input_data_scaled)[0])  # Scikit-learn devuelve directamente la clase
        clase_nombre = clase_nombres[clase_predicha]

        # Devolver una respuesta compatible con JSON
        return {
            "clase_predicha": clase_predicha,
            "descripcion": clase_nombre
        }
    except Exception as e:
        # Manejar errores y registrar información útil
        return {"error": f"Error interno en el servidor: {str(e)}"}




# Se corre esta línea: uvicorn api:app --reload

# Se abre aquí: http://127.0.0.1:8000/docs 
