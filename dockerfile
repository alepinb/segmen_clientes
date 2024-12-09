# Usar una imagen base ligera con Python
FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos del proyecto al contenedor
COPY . /app

# Instalar las dependencias especificadas en requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Exponer los puertos necesarios para Streamlit y FastAPI
EXPOSE 8501 8000

# Comando para ejecutar ambos servicios (Streamlit y FastAPI)
CMD ["sh", "-c", "streamlit run app.py --server.port=8501 --server.address=0.0.0.0 & uvicorn api:app --host 0.0.0.0 --port 8000"]