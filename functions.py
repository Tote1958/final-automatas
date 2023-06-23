import pandas as pd
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

def list_by_duration():
    data = csv_read()
    sorted_data = data.sort_values(by=["Duration_ms"], ascending=False)
    final_data = sorted_data.head(10)
    return final_data.loc[:,['Track','Duration_ms']]

def list_artists_by_views():
    data = csv_read()
    suma_artist = data.groupby('Artist')['Views'].sum()
    suma_artist = suma_artist.sort_values(ascending=False)
    artistas_ordenados = suma_artist.index.tolist()
    for i in range(10):
        print(i + 1, artistas_ordenados[i])
