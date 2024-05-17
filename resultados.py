from pymongo import MongoClient

# Conexión a MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['webscraping']  # Nombre de tu base de datos
resultados = db['resultados']  # Nombre de tu colección

# URL específica para la que quieres ver resultados
url_buscada = 'http://httpbin.org'

# Consulta a la base de datos para obtener los resultados
registros = resultados.find({"url": url_buscada})

# Imprimir los resultados
print(f"Resultados del escaneo para: {url_buscada}")
for registro in registros:
    print(registro['resultado'])
