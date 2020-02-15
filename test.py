import pandas as pd
import sqlalchemy
from sqlalchemy import *
from sklearn.neighbors import NearestNeighbors

full = pd.read_csv('movies.csv').dropna()
selections = full.drop(columns=['movieId','imdbID','title','genres'])


WGARSDFVTGWARSFVZ = selections.iloc[0]

knn = NearestNeighbors(n_neighbors=4)
knn.fit(selections)
arr = knn.kneighbors([thing], return_distance = False)

results = []
for i in arr[0]:
    url = f'https://imdb.com/title/{all_info["imdbID"][i]}'
    plot= all_info['Plot'][i]
    title = all_info['Title'][i]
    poster = all_info['Poster'][i]
    temp_dict = {
        'title':title,
        'url':url,
        'plot':plot,
        'poster':poster
    }
    results.append(temp_dict)