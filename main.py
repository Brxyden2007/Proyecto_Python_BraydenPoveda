import os
import json
from modules.dataManager import cargar_datos, guardar_datos
from modules.collectionManager import menu
from utils import screenController as sc  # screenController es usado para poder definir las funciones del sistema, ya sea en linux o en otro Sistema Operativo
import modules.menu as mn
from tabulate import tabulate  # Tabulate usado para implementar tablas a la hora de imprimir los datos

# Se crean listas vacías que permiten almacenar los elementos
Libros = []
Peliculas = []
Musicas = []

# Funciones para Cargar los Datos añadidos (JSON)
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

# Funciones para Guardar Datos (JSON)
def guardar_datos():
    """Guardar datos en un archivo JSON"""
    data = {
        'Libros': Libros,
        'Peliculas': Peliculas,
        'Musicas': Musicas
    }
    with open('datos.json', 'w', encoding="utf-8") as file:
        json.dump(data, file,indent=4,ensure_ascii=False) #ensure_ascii=False (es usado para poder establecer 'Caracteres Especiales')

# Funciones para Añadir Elementos 
def añadir_libro():
    sc.borrar_pantalla()
    idUnLibro = input('Ingrese el Identificador Unico del Libro: \n')
    titLibro = input('Ingrese el título del libro que desea añadir: \n')
    autorLibro = input('Ingrese el nombre del autor del libro: \n')
    genLibro = input('Ingrese el género del libro: \n')
    valPuntLibro = input('Ingrese la valoración o puntuación del libro: \n')
    contLibro = {
        "IDunica": idUnLibro, #IDunica = Identificador Unico
        "Título": titLibro,
        "Autor": autorLibro,
        "Género": genLibro,
        "Valoración": valPuntLibro
    }
    Libros.append(contLibro)
    print("Libro añadido.")
    sc.pausar_pantalla()

def añadir_peliculas():
    sc.borrar_pantalla()
    idUnPel = input('Ingrese el Identificador Unico de la Pelicula: \n')
    titPel = input('Ingrese el título de la película que desea añadir: \n')
    direcPel = input('Ingrese el director de la película: \n')
    genPel = input('Ingrese el género de la película: \n')
    valPuntPel = input('Ingrese la valoración o puntuación de la película: \n')
    contPel = {
        "IDunica": idUnPel,
        "Título": titPel,
        "Director": direcPel,
        "Género": genPel,
        "Valoración": valPuntPel
    }
    Peliculas.append(contPel)
    print("Película añadida.")
    sc.pausar_pantalla()

def añadir_musicas():
    sc.borrar_pantalla()
    idUnMusic = input('Ingrese el Identificador Unico de la Musica: \n')
    titMusic = input('Ingrese el título de la música: \n')
    autorMusic = input('Ingrese el autor de la música: \n')
    genMusic = input('Ingrese el género de la música: \n')
    valPuntMusic = input('Ingrese la valoración o puntuación de la música: \n')
    contMusic = {
        "IDunica": idUnMusic,
        "Título": titMusic,
        "Autor": autorMusic,
        "Género": genMusic,
        "Valoración": valPuntMusic
    }
    Musicas.append(contMusic)
    print("Música añadida.")
    sc.pausar_pantalla()

# Funciones para ver todos los elementos 
def ver_todos_los_libros():
    sc.borrar_pantalla()
    if Libros:
        print("Libros:")
        tabla_libros = [[libro["IDunica"], libro["Título"], libro["Autor"], libro["Género"], libro["Valoración"]] for libro in Libros]
        print(tabulate(tabla_libros, headers=["IDunica", "Título", "Autor", "Género", "Valoración"], tablefmt="grid"))
    else:
        print("No hay libros en la colección.")
    sc.pausar_pantalla()

def ver_todas_las_peliculas():
    sc.borrar_pantalla()
    if Peliculas:
        print("Películas:")
        tabla_peliculas = [[pelicula["IDunica"], pelicula["Título"], pelicula["Director"], pelicula["Género"], pelicula["Valoración"]] for pelicula in Peliculas]
        print(tabulate(tabla_peliculas, headers=["IDunica", "Título", "Director", "Género", "Valoración"], tablefmt="grid"))
    else:
        print("No hay películas en la colección.")
    sc.pausar_pantalla()

def ver_toda_la_musica():
    sc.borrar_pantalla()
    if Musicas:
        print("Música:")
        tabla_musica = [[musica["IDunica"], musica["Título"], musica["Autor"], musica["Género"], musica["Valoración"]] for musica in Musicas]
        print(tabulate(tabla_musica, headers=["IDunica", "Título", "Autor", "Género", "Valoración"], tablefmt="grid"))
    else:
        print("No hay música en la colección.")
    sc.pausar_pantalla()

# Función para buscar elementos
def buscar_elemento():
    sc.borrar_pantalla()
    SearchElementOp = input('Ingrese el título, autor o género para buscar: \n')
    
    resultados_libros = [libro for libro in Libros 
                         if SearchElementOp.lower() in libro["Título"].lower() or 
                         SearchElementOp.lower() in libro["Autor"].lower() or 
                         SearchElementOp.lower() in libro["Género"].lower()]
    
    resultados_peliculas = [pelicula for pelicula in Peliculas 
                            if SearchElementOp.lower() in pelicula["Título"].lower() or 
                            SearchElementOp.lower() in pelicula["Director"].lower() or 
                            SearchElementOp.lower() in pelicula["Género"].lower()]
    
    resultados_musica = [musica for musica in Musicas 
                         if SearchElementOp.lower() in musica["Título"].lower() or 
                         SearchElementOp.lower() in musica["Autor"].lower() or 
                         SearchElementOp.lower() in musica["Género"].lower()]
    
    if resultados_libros or resultados_peliculas or resultados_musica:
        print("Resultados de la búsqueda:")
        if resultados_libros:
            print("\nLibros encontrados:")
            for libro in resultados_libros:
                print(f"Título: {libro['Título']}, Autor: {libro['Autor']}, Género: {libro['Género']}, Valoración: {libro['Valoración']}")
        
        if resultados_peliculas:
            print("\nPelículas encontradas:")
            for pelicula in resultados_peliculas:
                print(f"Título: {pelicula['Título']}, Director: {pelicula['Director']}, Género: {pelicula['Género']}, Valoración: {pelicula['Valoración']}")
        
        if resultados_musica:
            print("\nMúsica encontrada:")
            for musica in resultados_musica:
                print(f"Título: {musica['Título']}, Autor: {musica['Autor']}, Género: {musica['Género']}, Valoración: {musica['Valoración']}")
    else:
        print("No se encontraron resultados.")
    sc.pausar_pantalla()

# Función para editar elementos
def editar_elemento():
    sc.borrar_pantalla()
    tipo = input("¿Qué tipo de elemento desea editar? (libro/película/música): \n").lower()
    
    if tipo == "libro":
        tit = input("Ingrese el título del libro que desea editar: \n")
        for libro in Libros:
            if libro["Título"].lower() == tit.lower():
                print("Elemento encontrado. Ingrese los nuevos detalles (deje en blanco para no cambiar):")
                nuevo_tit = input(f'Título (actual: {libro["Título"]}): ') or libro["Título"]
                nuevo_autor = input(f'Autor (actual: {libro["Autor"]}): ') or libro["Autor"]
                nuevo_gen = input(f'Género (actual: {libro["Género"]}): ') or libro["Género"]
                nuevo_val = input(f'Valoración (actual: {libro["Valoración"]}): ') or libro["Valoración"]
                
                libro.update({
                    "Título ": nuevo_tit,
                    "Autor": nuevo_autor,
                    "Género": nuevo_gen,
                    "Valoración": nuevo_val
                })
                print("Libro editado.")
                break
        else:
            print("No se encontró el libro.")
    
    elif tipo == "película":
        tit = input("Ingrese el título de la película que desea editar: \n")
        for pelicula in Peliculas:
            if pelicula["Título"].lower() == tit.lower():
                print("Elemento encontrado. Ingrese los nuevos detalles (deje en blanco para no cambiar):")
                nuevo_tit = input(f'Título (actual: {pelicula["Título"]}): ') or pelicula["Título"]
                nuevo_direc = input(f'Director (actual: {pelicula["Director"]}): ') or pelicula["Director"]
                nuevo_gen = input(f'Género (actual: {pelicula["Género"]}): ') or pelicula["Género"]
                nuevo_val = input(f'Valoración (actual: {pelicula["Valoración"]}): ') or pelicula["Valoración"]
                
                pelicula.update({
                    "Título": nuevo_tit,
                    "Director": nuevo_direc,
                    "Género": nuevo_gen,
                    "Valoración": nuevo_val
                })
                print("Película editada.")
                break
        else:
            print("No se encontró la película.")
    
    elif tipo == "música":
        tit = input("Ingrese el título de la música que desea editar: \n")
        for musica in Musicas:
            if musica["Título"].lower() == tit.lower():
                print("Elemento encontrado. Ingrese los nuevos detalles (deje en blanco para no cambiar):")
                nuevo_tit = input(f'Título (actual: {musica["Título"]}): ') or musica["Título"]
                nuevo_autor = input(f'Autor (actual: {musica["Autor"]}): ') or musica["Autor"]
                nuevo_gen = input(f'Género (actual: {musica["Género"]}): ') or musica["Género"]
                nuevo_val = input(f'Valoración (actual: {musica["Valoración"]}): ') or musica["Valoración"]
                
                musica.update({
                    "Título": nuevo_tit,
                    "Autor": nuevo_autor,
                    "Género": nuevo_gen,
                    "Valoración": nuevo_val
                })
                print("Música editada.")
                break
        else:
            print("No se encontró la música.")
    
    else:
        print("Tipo de elemento no válido.")
    
    guardar_datos()  # Guardar los cambios en el archivo JSON

def eliminar_por_titulo():
    tipoElemento = input("¿Qué tipo de elemento desea eliminar? (libro/película/música): \n").lower()
    tit = input("Ingrese el título del elemento que desea eliminar: \n")
    
    if tipoElemento == "libro":
        for libro in Libros:
            if libro["Título"].lower() == tit.lower():
                confirmacion = input(f"¿Está seguro que desea eliminar el libro '{tit}'? (s/n): ").lower()
                if confirmacion == 's':
                    Libros.remove(libro)
                    print("Libro eliminado.")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("No se encontró el libro.")
    
    elif tipoElemento == "película":
        for pelicula in Peliculas:
            if pelicula["Título"].lower() == tit.lower():
                confirmacion = input(f"¿Está seguro que desea eliminar la película '{tit}'? (s/n): ").lower()
                if confirmacion == 's':
                    Peliculas.remove(pelicula)
                    print("Película eliminada.")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("No se encontró la película.")
    
    elif tipoElemento == "música":
        for musica in Musicas:
            if musica["Título"].lower() == tit.lower():
                confirmacion = input(f"¿Está seguro que desea eliminar la música '{tit}'? (s/n): ").lower()
                if confirmacion == 's':
                    Musicas.remove(musica)
                    print("Música eliminada.")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("No se encontró la música.")
    
    else:
        print("Tipo de elemento no válido.")

def eliminar_por_identificador():
    tipoElemento = input("¿Qué tipo de elemento desea eliminar? (libro/película/música): \n").lower()
    id_unico = input("Ingrese el identificador único del elemento que desea eliminar: \n")
    
    if tipoElemento == "libro":
        for libro in Libros:
            if str(libro["IDunica"]) == id_unico:
                confirmacion = input(f"¿Está seguro que desea eliminar el libro con ID '{id_unico}'? (s/n): ").lower()
                if confirmacion == 's':
                    Libros.remove(libro)
                    print("Libro eliminado.")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("No se encontró el libro.")
    
    elif tipoElemento == "película":
        for pelicula in Peliculas:
            if str(pelicula["IDunica"]) == id_unico:
                confirmacion = input(f"¿Está seguro que desea eliminar la película con ID '{id_unico}'? (s/n): ").lower()
                if confirmacion == 's':
                    Peliculas.remove(pelicula)
                    print("Película eliminada.")
                else:
                    print("Eliminación cancelada.")
                break
        else:
            print("No se encontró la película.")
    
    elif tipoElemento == "música":
        for musica in Musicas:
            if str(musica["IDunica"]) == id_unico:
                confirmacion = input
                if confirmacion == 's':
                    Musicas.remove(musica)
                    print("Musica eliminada.")
                else:
                    print("Eliminación cancelada")
                break
        else:
            print("No se encontró la musica")



# Función para eliminar elementos
def eliminar_elemento():
    sc.borrar_pantalla()
    print(mn.menuDeleteElement)
    opmDE = int(input('')) #opmDE = Opcion de menuDeleteElement
    match opmDE:
        case 1:
            eliminar_por_titulo()
        case 2:
            eliminar_por_identificador()
        case 3:

    
            guardar_datos()  # Guardar los cambios en el archivo JSON

# Función para ver elementos por categoría
def ver_elementos_por_categoria():
    sc.borrar_pantalla()
    print(mn.menuElementCategory)
    opcion = input("Selecciona una opción: \n")
    
    match opcion:
        case '1':
            ver_todos_los_libros()
        case '2':
            ver_todas_las_peliculas()
        case '3':
            ver_toda_la_musica()
        case '4':
            return  # Regresar al menú principal
        case _:
            print("Opción no válida.")
            sc.pausar_pantalla()

# Función para guardar y cargar colección
def guardar_y_cargar_coleccion():
    sc.borrar_pantalla()
    print(mn.menusSaveAndUploadElement)
    opcion = input("Selecciona una opción: \n") 
    match opcion:
        case '1':
            guardar_datos()
        case '2':
            cargar_datos()
        case '3':
            return # Regresar al menú principal
        case _:
            print("Opción no válida.")
            sc.pausar_pantalla()

# Función principal del menú
def menu():
    cargar_datos()  # Cargar datos al iniciar
    while True:
        sc.borrar_pantalla()
        print(mn.menuAdCo)
        opcion = input("Selecciona una opción: \n")

        match opcion:
            case '1':
                print(mn.menuAddElement)
                optm1 = int(input(''))
                match optm1:
                    case 1:
                        añadir_libro()
                    case 2:
                        añadir_peliculas()
                    case 3:
                        añadir_musicas()
                    case 4:
                        continue  # Regresar al menú principal
            case '2':
                print(mn.menuAllElement)
                optm2 = int(input(''))
                match optm2:
                    case 1:
                        ver_todos_los_libros()
                    case 2:
                        ver_todas_las_peliculas()
                    case 3:
                        ver_toda_la_musica()
                    case 4:
                        continue  # Regresar al menú principal
            case '3':
                buscar_elemento()
            case '4':
                editar_elemento()
            case '5':
                eliminar_elemento()
            case '6':
                ver_elementos_por_categoria()
            case '7':
                guardar_y_cargar_coleccion()
            case '8':
                guardar_datos()  # Guardar datos antes de salir
                print("Saliendo del programa.")
                break
            case _:
                print("Opción no válida. Por favor, selecciona una opción válida.")
                sc.pausar_pantalla()

if __name__ == "__main__":
    menu()