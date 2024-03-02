# Usar una imagen base de Python
FROM python:3.11-slim

ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PYTHONUNBUFFERED=1

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar los archivos de la aplicación al contenedor
COPY ./requirements.txt .
RUN python -m venv venv

RUN /bin/bash -c "source venv/bin/activate"

# Instalar las dependencias de la aplicación
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# Exponer el puerto en el que la aplicación FastAPI está escuchando
EXPOSE 80

# Comando para ejecutar la aplicación FastAPI
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]

