FROM python:3.12-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar archivos de configuración
COPY backendpython/requirements.txt backendpython/pyproject.toml ./

# Instalar dependencias usando pip y requirements.txt
RUN pip install --upgrade pip \
    && pip install -r requirements.txt

# Copiar el código fuente del backend
COPY backendpython/ ./backendpython/

# Copiar el archivo .env si existe (para variables de entorno)
COPY .env .env

# Exponer el puerto en el que correrá FastAPI
EXPOSE 8000

# Comando para iniciar la aplicación
CMD ["uvicorn", "backendpython.main:app", "--host", "0.0.0.0", "--port", "8000"]

