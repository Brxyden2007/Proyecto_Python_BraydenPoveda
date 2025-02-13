import os
import json
# Listas vacias para almacenar los elementos
Libros = []
Peliculas = []
Musicas = []
def cargar_datos():
    """Cargar datos desde un archivo JSON si existe."""
    global Libros, Peliculas, Musicas
    if os.path.exists("datos.json"):
        try:
            with open("datos.json", "r", encoding="utf-8") as archivo:
                data = json.load(archivo)
                Libros = data.get("Libros", [])
                Peliculas = data.get("Peliculas", [])
                Musicas = data.get("Musicas", [])
        except Exception as e:
            print(f"Error al cargar datos: {e}")

# Mover el archivo

def guardar_datos():
    """Guardar datos en un archivo JSON"""
    data = {
        'Libros': Libros,
        'Peliculas': Peliculas,
        'Musicas': Musicas
    }
    with open('datos.json', 'w') as file:
        json.dump(data, file,indent=4,ensure_ascii=False)