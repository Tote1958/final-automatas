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



