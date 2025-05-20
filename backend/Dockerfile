# Imagen base
FROM python:3.11-slim

# Variables de entorno para evitar archivos pyc y output buffering
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Directorio de trabajo
WORKDIR /app

# Copiar solo requirements primero para aprovechar cache
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar el resto del proyecto
COPY . /app/

# Crear carpeta para archivos multimedia (fotos)
RUN mkdir -p /app/media

# Exponer puerto 8000
EXPOSE 8000

# Comando para correr el servidor Django
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

