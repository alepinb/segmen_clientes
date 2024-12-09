# Proyecto de Segmentación de Clientes

Este proyecto tiene como objetivo la segmentación de clientes utilizando diversas técnicas de machine learning, incluyendo árboles de decisión, redes neuronales y otros enfoques de clasificación.

# Estructura del Proyecto

```plaintext
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
```

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

El mejor modelo se guarda como `modelo_logistico.pkl`.

# DEPENDENCIAS
Las dependencias se gestionan en `requirements.txt`. Incluyen:
- Streamlit
- NumPy
- Pandas
- SQLite3
- Scikit-learn
- LightGBM

Entre otras.

# Autora
Realizado por Alejandra Piñango.
