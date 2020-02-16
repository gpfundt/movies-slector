import pandas as pd
import sqlalchemy
import requests
from sqlalchemy import *
import re
import numpy as np
from sklearn.neighbors import NearestNeighbors
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer

engine = create_engine("sqlite:///data/movies-db.sqlite")
conn = engine.connect()
inspector = inspect(engine)
tables = inspector.get_table_names()

# Value from selection on search bar
value = full[full['Title']=='Toy Story'].index.values[0]

<<<<<<< HEAD
full = pd.read_csv('movies.csv').dropna()
selections = full.drop(columns=['Unnamed: 0','movieId','imdbID','Title','Year','Ratings','Released','Runtime','Plot','Poster','imdbVotes'])


kmeans = KMeans(n_clusters=800, random_state = 42)
kmeans.fit(selections)
clusters = kmeans.predict(selections)
full['clusters']=clusters

new_full = full[full['clusters'] == full['clusters'][value]].reset_index()
plots_arr = new_full['Plot'].to_numpy()
plots_l = list(plots_arr)

corpus = []
for i in range(0, len(plots_l)):
    text = re.sub('[^a-zA-Z]', ' ', plots_l[i])
    text = text.lower()
    text=re.sub("&lt;/?.*?&gt;"," &lt;&gt; ",text)
    text=re.sub("(\\d|\\W)+"," ",text)
    corpus.append(text)

vectorizer = TfidfVectorizer(max_features=100, stop_words='english')
X = vectorizer.fit_transform(corpus)

my_tags = vectorizer.get_feature_names()

my_tag_matrix = pd.DataFrame(0, index=np.arange(len(plots_l)), columns=my_tags)
for i in range(0,len(my_tag_matrix)):
    for j in range(0,len(my_tags)):        
        if my_tags[j] in new_full['Plot'].iloc[i]:
            my_tag_matrix.iloc[i][my_tags.index(my_tags[j])] = 1

my_tag_matrix['imdbID'] = new_full['imdbID']

new_selections = my_tag_matrix.drop(columns = ['imdbID'])

thing = new_selections.iloc[value]

knn = NearestNeighbors(n_neighbors=4)
knn.fit(new_selections)
arr = knn.kneighbors([thing], return_distance = False)

results = []
for i in arr[0]:
    url = f'https://imdb.com/title/{new_full["imdbID"][i]}'
    plot= new_full['Plot'].iloc[i]
    title = new_full['Title'].iloc[i]
    poster = new_full['Poster'].iloc[i]
    temp_dict = {
        'title':title,
        'url':url,
        'plot':plot,
        'poster':poster
    }
    results.append(temp_dict)

=======

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
