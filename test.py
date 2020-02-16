import pandas as pd
import sqlalchemy
import requests
from sqlalchemy import *
import numpy as np
from sklearn.neighbors import NearestNeighbors

engine = create_engine("sqlite:///data/movies-db.sqlite")
conn = engine.connect()
inspector = inspect(engine)
tables = inspector.get_table_names()

postData = req.form
json = str(postData['param'].value)
return json

# def movie_algo(id_from_js):
#     full = pd.read_csv('movies.csv').dropna()
#     selections = full.drop(columns=['movieId','imdbID','title','genres'])


#     knn = NearestNeighbors(n_neighbors=4)
#     knn.fit(selections)
#     arr = knn.kneighbors([thing], return_distance = False)

#     results = []
#     for i in arr[0]:
#         url = f'https://imdb.com/title/{all_info["imdbID"][i]}'
#         plot= all_info['Plot'][i]
#         title = all_info['Title'][i]
#         poster = all_info['Poster'][i]
#         temp_dict = {
#             'title':title,
#             'url':url,
#             'plot':plot,
#             'poster':poster
#         }
#         results.append(temp_dict)
    
#     return "Hooray"

# movie_algo("test")
>>>>>>> refs/remotes/origin/master
