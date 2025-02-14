# Imagen base de Python
FROM python:3.12-slim

# Establecer directorio de trabajo
WORKDIR /app

# Copiar y actualizar dependencias
COPY ./requirements.txt ./pyproject.toml ./
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt

# Copiar el código fuente
COPY . /app/    

# Definir usuario no root para mayor seguridad
RUN useradd -m appuser && chown -R appuser /app
USER appuser

# Exponer el puerto de FastAPI
EXPOSE 8000

# Comando de inicio
CMD ["uvicorn", "backendpython.main:app", "--host", "0.0.0.0", "--port", "8000"]
