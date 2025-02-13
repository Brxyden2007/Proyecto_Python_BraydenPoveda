from modules.dataManager import Libros, Peliculas, Musicas

def menu():
    """Mostrar el menú principal y manejar la selección del usuario"""
    while True:
        print("1. Añadir Libro")
        print("2. Añadir Película")
        print("3. Añadir Música")
        print("4. Salir")
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            añadir_libro()
        elif opcion == '2':
            añadir_pelicula()
        elif opcion == '3':
            añadir_musica()
        elif opcion == '4':
            break
        else:
            print("Opción no válida.")

def añadir_libro():
    """Añadir un libro a la colección"""
    libro = input("Introduce el nombre del libro: ")
    Libros.append(libro)
    print(f"Libro '{libro}' añadido.")

def añadir_pelicula():
    """Añadir una película a la colección"""
    pelicula = input("Introduce el nombre de la película: ")
    Peliculas.append(pelicula)
    print(f"Película '{pelicula}' añadida.")

def añadir_musica():
    """Añadir música a la colección"""
    musica = input("Introduce el nombre de la música: ")
    Musicas.append(musica)
    print(f"Música '{musica}' añadida.")