import os
from functions import *


def menu():
    borrar = 'cls' if os.name == 'nt' else 'clear'
    os.system(borrar)
    print("\t")
    print("┌─────────────────────────────────────────────────────────────────┐")
    print("│Seleccione su opción                                             │")
    print(" ───────────────────────────────────────────────────────────────── ")
    print("│ 1 - Listar las 5 canciones con más likes, vistas y comentarios  │")
    print("│ 2 - Listar las 5 canciones con mejor ratio (likes/view).        │")
    print("│ 3 - Buscar una canción                                          │")
    print("│ 4 - Agregar nueva fila                                          │")
    print("│ 5 - Listar las 10 canciones que más duración tienen             │")
    print("│ 6 - Listar los 10 artistas con más reproducciones en total.     │")
    print("│ 7 - Para salir                                                  │")
    print("└─────────────────────────────────────────────────────────────────┘")
    print(" ☺ ")
    print("┌───────────────────────────┐")
    print("│ Indique la opción elegida │")
    print("└───────────────────────────┘")

while True:
    menu()  # Mostramos el menu
    opcionMenu = input('--> ')  # solicituamos una opción al usuario
    if opcionMenu == "1":
        print("")
        print("Has pulsado la opción 1...")
        print('Las canciones con mas likes son:')
        print(list_most_liked_songs())
        print('Las canciones con mas vistas son:')
        print(list_most_viewed_songs())
        print('Las canciones con mas comentarios son:')
        print(list_most_commented_songs())
        input('Presione enter para volver al menu ')
       
    elif opcionMenu == "2":
        print("")
        print("Has pulsado la opción 2...")
        print("Las canciones con mejor ratio son:")
        print(list_most_ratio_songs())
        input('Presione enter para volver al menu ')
        
    elif opcionMenu == "3":
        print("")
        print("Has pulsado la opción 3...")
        print(search_track())
        input('Presione enter para volver al menu ')
        
        
    elif opcionMenu == "4":
        print("")
        print("Has pulsado la opción 4...")
        print(add_track())
        input('Presione enter para volver al menu ')
        
    elif opcionMenu == "5":
        print("")
        print("Has pulsado la opción 5...")
        print('Las canciones con mayor duración son:')
        print(list_by_duration())
        input('Presione enter para volver al menu ')
        
    elif opcionMenu == "6":
        print("")
        print("Has pulsado la opción 6...")
        print('Lor 10 Artistas con más vistas son:')
        list_artists_by_views()
        input('Presione enter para volver al menu ')

    elif opcionMenu == "7":
        print("Has pulsado la opción 7...")
        print("Saliendo...")
        break  

    else:
        print("")
        print("No has pulsado ninguna opción correcta...")