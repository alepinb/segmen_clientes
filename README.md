# CARACTERÍSTICAS

Este proyecto es una aplicación de Streamlit que segmenta a los clientes utilizando datos demográficos. Incluye una API con la siguiente estructura de carpetas:

Proyecto_seg_clientes/
├── .devcontainer/
├── catboost_info/
├── Data/
│   └── dockgenore
├── api.py
├── app.py
├── diagnostic_pandas.py
├── dockerfile
├── mejor_modelo.h5
├── modelo_logistico.pkl
├── predicciones.db
├── requirements.txt
├── scaler.pkl
├── seg_clientes_arbol_decision.ipynb
├── seg_clientes_catboost.ipynb
├── seg_clientes_eda.ipynb
├── seg_clientes_ensamble.ipynb
├── seg_clientes_knn.ipynb
├── seg_clientes_pca.ipynb
├── seg_clientes_random_forest.ipynb
├── seg_clientes_red_neuronal_optuna_smoote.ipynb
├── seg_clientes_red_neuronal_optuna.ipynb
└── seg_clientes_reg_logistica_multiclase_optuna.ipynb

# CARACTERÍSTICAS
- Segmenta a los clientes usando datos demográficos
- Incluye una API para acceder al modelo de segmentación
- Dockerizado para una implementación sencilla

# PRIMEROS PASOS
1. Clona el repositorio: `git clone https://github.com/your-username/Proyecto_seg_clientes.git`
2. Construye el contenedor Docker: `docker build -t seg-clientes-app .`
3. Ejecuta el contenedor Docker: `docker run -p 8501:8501 seg-clientes-app`
4. Accede a la aplicación de Streamlit en `http://localhost:8501`

# ENDPOINTS DE LA API
La API incluye los siguientes endpoints:
- `GET /predict`: Devuelve las predicciones de segmentación de clientes para una entrada dada
- `POST /train`: Entrena el modelo de segmentación con nuevos datos

Consulta el archivo `api.py` para más detalles.

# DATOS
El proyecto utiliza datos demográficos en el directorio `Data/`. El archivo `dockgenore` se usa para la gestión de la imagen Docker.

# MODELOS
El proyecto incluye varios modelos, como:
- Regresión logística (`modelo_logistico.pkl`)
- Random Forest (`seg_clientes_random_forest.ipynb`) 
- Red neuronal (`seg_clientes_red_neuronal_optuna.ipynb`)

El mejor modelo se guarda como `mejor_modelo.h5`.

# DEPENDENCIAS
Las dependencias se gestionan en `requirements.txt`. Incluyen:
- Streamlit
- NumPy
- Pandas
- SQLite3
- Scikit-learn
- LightGBM

# CONTRIBUCIÓN
Envía una solicitud de extracción con tus cambios. Realizado por Alejandra Piñango.
