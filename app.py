from flask import Flask, request, jsonify, render_template
import os
import pymongo
from pymongo import MongoClient
import datetime
import requests

app = Flask(__name__)

# Configuración de conexión a MongoDB
client = MongoClient('tu_string_de_conexion')
db = client['resultados']
log_collection = db['resultados']

@app.route('/')
def index():
    return render_template('index.html')

def buscar_subdirectorios(ruta):
    subdirectorios = []
    for root, dirs, files in os.walk(ruta):
        for d in dirs:
            subdirectorios.append(os.path.join(root, d))
    return subdirectorios

@app.route('/buscar_directorios', methods=['POST'])
def buscar_directorios():
    try:
        url = request.json['url']
        if not os.path.exists(url):
            return jsonify({'error': 'La ruta no existe'}), 404

        # Buscar subdirectorios en la ruta especificada
        subdirectorios = buscar_subdirectorios(url)

        # Descargar contenido de las URL y almacenar en MongoDB
        for subdir in subdirectorios:
            # Simplemente imprime la URL por ahora
            print("Descargando contenido de:", subdir)
            # Descarga el contenido de la URL
            response = requests.get(subdir)
            # Almacena la URL y el contenido en MongoDB
            log_collection.insert_one({'url': subdir, 'content': response.text})

        return jsonify({'message': 'Descarga de contenido completa'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
