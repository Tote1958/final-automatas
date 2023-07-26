import pandas as pd
import re
import os

def csv_read():
    PATH = './Listado temas 2023.csv'
    data = pd.read_csv(PATH)
    return data

def list_most_commented_songs():
    data = csv_read()
    sorted_data = data.sort_values(by=["Comments"], ascending=False)
    final_data = sorted_data.head(5)
    return final_data.loc[:,['Track','Comments']]

def list_most_viewed_songs():
    data = csv_read()
    sorted_data = data.sort_values(by=["Views"], ascending=False)
    final_data = sorted_data.head(5)
    return final_data.loc[:,['Track','Views']]

def list_most_liked_songs():
    data = csv_read()
    sorted_data = data.sort_values(by=["Likes"], ascending=False)
    final_data = sorted_data.head(5)
    return final_data.loc[:,['Track','Likes']]

def list_most_ratio_songs():
    data = csv_read()
    data['Ratio'] = data['Likes']/data['Views']
    sorted_data = data.sort_values(by=["Ratio"], ascending=False)
    final_data = sorted_data.head(5)
    return final_data.loc[:,['Track','Ratio']]

def search_track():
    data = csv_read()
    while True:
        print("┌─────────────────────────────────────────────────────────────────┐")
        print("│       Ingrese el número de la opción que desee buscar           │")
        print(" ───────────────────────────────────────────────────────────────── ")
        print("│ 1 - Canción                                                     │")
        print("│ 2 - Album                                                       │")
        print("│ 3 - Artista                                                     │")
        print("└─────────────────────────────────────────────────────────────────┘")
        opcionMenu = input('--> ')  # solicitamos una opción al usuario
        print("┌────────────────────────────────────────────────┐")
        print("│       Ingrese el nombre que desee buscar       │")
        print("└────────────────────────────────────────────────┘")
        name = str(input('--> '))
        if opcionMenu == '1':
            filter = 'Track'
            break
        elif opcionMenu == '2':
            filter = 'Album'
            break
        elif opcionMenu == '3':
            filter = 'Artist'
            break
        else:
            borrar = 'cls' if os.name == 'nt' else 'clear'
            os.system(borrar)
            print("┌─────────────────────────────────────────────────────────────────────────┐")
            print('|-------------Ingresó un valor invalido. Vuelva a intentar...-------------|')
            print("└─────────────────────────────────────────────────────────────────────────┘")
    result = data[data[filter].str.contains(name)]
    return result

def validate_manual_track():
    while True:
        artist = input('Ingrese el artista: ')
        REG_EX = r'([a-zA-Z0-9]| )+'
        if re.fullmatch(REG_EX, artist):
            break
        print("Ha escrito algo mal, intente de nuevo") 
    while True:
        url_spotify = input('Ingrese la URL de Spotify: ')    #url de ejemplo: https://open.spotify.com/track/5HNCy40Ni5BZJFw1TKzRsC?si=26024379e98f4ba6
        REG_EX = r'((https://)?(www\.)?(open\.spotify\.com/track/|open\.spotify\.com/artist/)([a-zA-Z0-9]|\_)+)'
        if re.fullmatch(REG_EX, url_spotify):
            break
        print("Ha escrito algo mal, intente de nuevo") 
    while True:
        track = input('Ingrese el track: ')
        REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        if re.fullmatch(REG_EX, track):
            break
        print("Ha escrito algo mal, intente de nuevo")  
    while True:
        album = input('Ingrese el album: ')
        REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        if re.fullmatch(REG_EX, album):
            break
        print("Ha escrito algo mal, intente de nuevo")  
    while True:
        album_type = input('Ingrese el tipo de album: ')
        REG_EX = r'album|single|compilation' # Solo pueden ser album, single o compilation
        if re.fullmatch(REG_EX, album_type):
            break
        print("Ha escrito algo mal, intente de nuevo... (recuerde que solo puede ser 'album', 'single' o 'compilation')")  
    while True:
        url = input('Ingrese la URL: ')
        REG_EX = r'(spotify:track:([a-zA-Z0-9])+)'
        if re.fullmatch(REG_EX, url):
            break 
        print("Ha escrito algo mal, intente de nuevo") 
    while True:
        duration = str(input('Ingrese la duracion (en milisegundos, en enteros, sin las siglas, ni letras): '))
        REG_EX = r'([0-9]+)'  #CHEQUEAR QUE ONDA CON LO DE MS
        if re.fullmatch(REG_EX, duration):
            break 
        print("Ha escrito algo mal, intente de nuevo") 
    while True:
        url_youtube = input('Ingrese la URL de YouTube: ')
        REG_EX = r'((https://)?(www\.)?(youtube\.com/watch\?v=)([a-zA-Z0-9]|\_|\-)+)'
        if re.fullmatch(REG_EX, url_youtube):
            break 
        print("Ha escrito algo mal, intente de nuevo") 
    while True:
        title = input('Ingrese el title: ')
        REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        if re.fullmatch(REG_EX, title):
            break
        print("Ha escrito algo mal, intente de nuevo") 
    song_to_add = pd.DataFrame({'Artist': artist,
                         'Url_spotify': url_spotify,
                         'Track': track,
                         'Album': album,
                         'Album_type':album_type,
                         'Uri':url,  #EL CSV DICE URI, NO URL, ESTA BIEN ESO?
                         'Duration_ms': float(duration),
                         'Url_youtube':url_youtube,
                         'Title':title}, index=[0]) 
    
    return song_to_add

def validate_file(file):
    for i in range(file['Index'].max() + 1):
        artist = file['Artist'].values[i]
        #REG_EX = r'([a-zA-Z0-9]| )+'
        REG_EX = r'(.)+'
        if re.fullmatch(REG_EX, artist):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que el artista {artist} no es aceptado por la expresión regular')
            return False 

        url_spotify = file['Url_spotify'].values[i]   
        REG_EX = r'((https://)?(www\.)?(open\.spotify\.com/track/|open\.spotify\.com/artist/)([a-zA-Z0-9]|\_)+)'
        if re.fullmatch(REG_EX, url_spotify):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que la Url_spotify {url_spotify} no es aceptada por la expresión regular')
            return False 
        
        track = file['Track'].values[i]
        #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        REG_EX = r'(.)+'
        if re.fullmatch(REG_EX, track):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que el track {track} no es aceptado por la expresión regular')
            return False 

        album = file['Album'].values[i]
        #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'          
        if re.fullmatch(REG_EX, album):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que el album {album} no es aceptado por la expresión regular')
            return False 

        album_type = file['Album_type'].values[i]
        #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        REG_EX = r'album|single|compilation' # Solo pueden ser album, single o compilation
        if re.fullmatch(REG_EX, album_type):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que el tipo de album {album_type} no es aceptado por la expresión regular')
            return False 

        url = file['Uri'].values[i]
        REG_EX = r'(spotify:track:([a-zA-Z0-9])+)'
        if re.fullmatch(REG_EX, url):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que el url {url} no es aceptado por la expresión regular')
            return False 
        duration = str(int(file['Duration_ms'].values[i]))
        REG_EX = r'([0-9]+)'  #CHEQUEAR QUE ONDA CON LO DE MS
        if re.fullmatch(REG_EX, duration):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que la duración {duration} no es aceptado por la expresión regular')
            return False

        url_youtube = file['Url_youtube'].values[i]
        REG_EX = r'((https://)?(www\.)?(youtube\.com/watch\?v=)([a-zA-Z0-9]|\_|\-)+)'
        if re.fullmatch(REG_EX, url_youtube):                                           #El error que tira esta bien, between de bars no tiene streams por ejemplo
            pass
        else:
            print(f'La fila {i} no es válida, debido al que el url de youtube {url_youtube} no es aceptado por la expresión regular')
            return False

        title = file['Title'].values[i]
        #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\'|\[|\])+'
        REG_EX = r'(.)+'          #Le puse un punto porque hay muchos simbolos 
        if re.fullmatch(REG_EX, title):
            pass
        else:
            print(f'La fila {i} no es válida, debido al que el titulo {title} no es aceptado por la expresión regular')
            return False
        
    return True


def incorrect_file(file):
        final_file = file
        while True:
            print("┌────────────────────────────────────────────────────────┐")
            print("│ El archivo tiene filas con campos incorrectos          │")
            print("│ Seleccione una opción:                                 │")
            print("|────────────────────────────────────────────────────────|")
            print("│ 1 - Añadir el archivo salteando los campos incorrectos │")
            print("│ 2 - No añadir el archivo                               │")
            print("└────────────────────────────────────────────────────────┘")
            option = str(input('--> '))
            if option == "1":
                for i in range(final_file['Index'].max() + 1):
                    artist = final_file['Artist'].values[i]
                    #REG_EX = r'([a-zA-Z0-9]| )+'
                    REG_EX = r'(.)+'
                    if re.fullmatch(REG_EX, artist):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que el artista {artist} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue

                    url_spotify = final_file['Url_spotify'].values[i]   
                    REG_EX = r'((https://)?(www\.)?(open\.spotify\.com/track/|open\.spotify\.com/artist/)([a-zA-Z0-9]|\_)+)'
                    if re.fullmatch(REG_EX, url_spotify):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que la Url_spotify {url_spotify} no es aceptada por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue
                    
                    track = final_file['Track'].values[i]
                    #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
                    REG_EX = r'(.)+'
                    if re.fullmatch(REG_EX, track):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que el track {track} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue

                    album = final_file['Album'].values[i]
                    #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'          
                    if re.fullmatch(REG_EX, album):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que el album {album} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue

                    album_type = final_file['Album_type'].values[i]
                    #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
                    REG_EX = r'album|single|compilation' # Solo pueden ser album, single o compilation
                    if re.fullmatch(REG_EX, album_type):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que el tipo de album {album_type} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue

                    url = final_file['Uri'].values[i]
                    REG_EX = r'(spotify:track:([a-zA-Z0-9])+)'
                    if re.fullmatch(REG_EX, url):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que el url {url} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue 
                    duration = str(int(final_file['Duration_ms'].values[i]))
                    REG_EX = r'([0-9]+)'  #CHEQUEAR QUE ONDA CON LO DE MS
                    if re.fullmatch(REG_EX, duration):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que la duración {duration} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue

                    url_youtube = final_file['Url_youtube'].values[i]
                    REG_EX = r'((https://)?(www\.)?(youtube\.com/watch\?v=)([a-zA-Z0-9]|\_|\-)+)'
                    if re.fullmatch(REG_EX, url_youtube):                                           #El error que tira esta bien, between de bars no tiene streams por ejemplo
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que el url de youtube {url_youtube} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue

                    title = final_file['Title'].values[i]
                    #REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\'|\[|\])+'
                    REG_EX = r'(.)+'          #Le puse un punto porque hay muchos simbolos 
                    if re.fullmatch(REG_EX, title):
                        pass
                    else:
                        print(f'La fila {i} no es válida, debido al que el titulo {title} no es aceptado por la expresión regular')
                        final_file.drop([i],axis=0)
                        continue
                return final_file


            elif option == "2":
                return False
            else:
                print("")
                print("No has pulsado ninguna opción correcta...")





def add_track():
    data = csv_read()
    while True:
        print("┌────────────────────────────────────────────────────┐")
        print("│ Seleccione una opción                                │")
        print("|────────────────────────────────────────────────────|")
        print("│ 1 - Cargar una canción a mano                      │")
        print("│ 2 - Cargar una o mas canciones mediante un archivo │")
        print("│ 3 - Para salir                                     │")
        print("└────────────────────────────────────────────────────┘")
        option = str(input('--> '))
        if option == "1":
            data = csv_read()
            print("A continuacion, ingrese los datos de la cancion a añadir")
            new_track = validate_manual_track()
            final_data = pd.concat([data, new_track], ignore_index=True)
            try:
                final_data.drop('Index', inplace=True, axis=1)
            except KeyError:
                pass                                             #Con el Try borra el nombre pero aparece la columna como Unnamed : 0 
            final_data.to_csv('./Listado temas 2023.csv', index=False) # No agrega columna Unnamed de esta forma (index=False)
            return final_data
        elif option == "2":
            data = csv_read()
            path = str(input('Ingrese la direccion del archivo a agregar: ')) # D:\UM\Repos 3ro\Automatas y gramaticas\Final\final-automatas\archivo_prueba.csv
            new_file = pd.read_csv(path)                                     # ./archivo_prueba.csv
            file_validation = validate_file(new_file)
            if file_validation is True:
                new_file.set_index('Index', drop=False, append=False, inplace=True)
                final_data = pd.concat([data, new_file], ignore_index=True)
                final_data.set_index('Index', drop=False, append=False)
                final_data.reset_index(inplace=True , drop=False)
                final_data.drop('Index', inplace=True, axis=1)
                final_data.rename(columns={'index':'Index'}, inplace=True)
                final_data.to_csv('./Listado temas 2023.csv', index=False) # Con index=False no agrega la columna Unnamed y se pueden agregar muchos nuevos registros sin error, lo que no puedo agregar es que el index se autoincremente dependiendo del index del archivo principal
                return final_data
            elif file_validation is False:
                processed_data = incorrect_file(new_file)
                if processed_data is False:
                    return "Ha decidido no añadir el archivo con errores"
                else:
                    processed_data.set_index('Index', drop=False, append=False, inplace=True)
                    final_data = pd.concat([data, processed_data], ignore_index=True)
                    final_data.set_index('Index', drop=False, append=False)
                    final_data.reset_index(inplace=True , drop=False)
                    final_data.drop('Index', inplace=True, axis=1)
                    final_data.rename(columns={'index':'Index'}, inplace=True)
                    final_data.to_csv('./Listado temas 2023.csv', index=False)
                    return final_data

            else: 
                break
        elif option == "3":
            break
        else:
            print("")
            print("No has pulsado ninguna opción correcta...")


def list_by_duration():
    data = csv_read()
    grouped_data = data.groupby('Track')
#   data['duration'] = datetime.timedelta(milliseconds = data['Duration_ms'])  da error porque no toma bien el valor, no lo toma porque no un valor float y cuando lo intento forzar da otro error.
    data['Duration'] = data['Duration_ms'] / 1000
    sorted_data = grouped_data['Duration'].max().sort_values(ascending=False)
    final_data = sorted_data.head(10)
#   final_data['duration'] = final_data['duration'].apply(lambda x: '{:02d}:{:02d}'.format(*divmod(int(x), 60)))  si lo dejaba sin el .loc daba una advertencia...
    final_data = final_data.reset_index()  # Reinicia el índice porque sinó daba problemas
    final_data.loc[:, 'Duration'] = final_data['Duration'].apply(lambda x: '{:02d}:{:02d}'.format(*divmod(int(x), 60)))
    return final_data.loc[:,['Track','Duration']]

def list_artists_by_views():
    data = csv_read()
    suma_artist = data.groupby('Artist')['Views'].sum()
    suma_artist = suma_artist.sort_values(ascending=False)
    artistas_ordenados = suma_artist.index.tolist()
    for i in range(10):
        print(i + 1, artistas_ordenados[i])
