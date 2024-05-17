# Usa una imagen base de Python
FROM python:3.8-slim

# Configura el directorio de trabajo
WORKDIR /app

# Primero copia solo los requerimientos para cachear la instalación de las dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Ahora copia el resto del código fuente
COPY . .

# Instala herramientas necesarias para ejecutar comandos de sistema operativo, como dirb
RUN apt-get update && apt-get install -y dirb

# Limpiar caché de apt para reducir tamaño de imagen
RUN apt-get clean && rm -rf /var/lib/apt/lists/*

# Configura la variable de entorno para Flask
ENV FLASK_APP=app.py

# Expone el puerto en el que Flask se ejecutará
EXPOSE 5000

# Comando para iniciar la aplicación Flask
CMD ["flask", "run", "--host=0.0.0.0"]
