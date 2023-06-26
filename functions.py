import pandas as pd
import re
import datetime

def csv_read():
    path = './Listado temas 2023.csv'
    data = pd.read_csv(path)
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
    search = str(input('Ingrese la cancion a buscar: '))
    data["Search"]= data["Track"].str.find(search)
    data.drop(data[data['Search'] == -1].index, inplace = True)
    sorted_data = data.sort_values(by=["Search"], ascending=True)
    del sorted_data['Search']
    return sorted_data



def validate_track():
    while True:
        artist = input('Ingrese el artista: ')
        REG_EX = r'([a-zA-Z0-9]| )+'
        if re.fullmatch(REG_EX, artist):
            break
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
    while True:
        album = input('Ingrese el album: ')
        REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        if re.fullmatch(REG_EX, album):
            break 
    while True:
        album_type = input('Ingrese el tipo de album: ')
        REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        if re.fullmatch(REG_EX, album_type):
            break 
    while True:
        url = input('Ingrese la URL: ')
        REG_EX = r'(spotify:track:([a-zA-Z0-9])+)'
        if re.fullmatch(REG_EX, url):
            break 
    while True:
        duration = str(input('Ingrese la duracion (en milisegundos): '))
        REG_EX = r'([0-9]+)'  #CHEQUEAR QUE ONDA CON LO DE MS
        if re.fullmatch(REG_EX, duration):
            break 
    while True:
        url_youtube = input('Ingrese la URL de YouTube: ')
        REG_EX = r'((https://)?(www\.)?(youtube\.com/watch\?v=)([a-zA-Z0-9]|\_|\-)+)'
        if re.fullmatch(REG_EX, url_youtube):
            break 
    while True:
        title = input('Ingrese el title: ')
        REG_EX = r'([a-zA-Z0-9]| |#|\.|\?|\-|_|\(|\)|\,|\/|\;|"|\')+'
        if re.fullmatch(REG_EX, title):
            break
    song_to_add = pd.DataFrame({'Artist': artist,
                         'Url_spotify': url_spotify,
                         'Track': track,
                         'Album': album,
                         'Album_type':album_type,
                         'Uri':url,  #EL CSV DICE URI, NO URL, ESTA BIEN ESO?
                         'Duration_ms': duration,
                         'Url_youtube':url_youtube,
                         'Title':title}) 
    
    return song_to_add

def add_track():
    data = csv_read()
    print("A continuacion, ingrese los datos de la cancion a añadir")
    new_track = validate_track()
    final_data = data.append(new_track,ignore_index=True)
    return final_data

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
