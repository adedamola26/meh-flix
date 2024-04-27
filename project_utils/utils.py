import pickle
import os
import pandas as pd
import requests
from io import BytesIO
from PIL import Image
from sklearn.metrics.pairwise import cosine_similarity


def get_path(path):
    """
    Returns the absolute path of the file given the relative path
    
    args:
        path (str): The relative path of the file
    """
    dir_path = os.path.dirname(os.path.realpath(__file__))
    return os.path.join(dir_path, path)

def get_movie_data(titles):
    """
    Returns the movie names and images for a given list of movie titles

    args:
        titles (list): A list of movie titles
    return:
        movie_names (list): A list of movie names
        movie_image_urls (list): A list of movie image urls corresponding to the movie names
    """
    movie_names = titles
    movie_posters = [images[t] for t in titles]
    return movie_names, movie_posters


def truncate_title(title, max_length=21):
    """
    Truncates the title of a movie to a given length
    (not used in the current version of the app but 
    can be used to truncate the title of the movie 
    if it is too long to fit in the UI)

    args:
        title (str): The title of the movie
        max_length (int): The maximum length of the title; default is 21
    return:
        title (str): The truncated title
    """
    if len(title) > max_length:
        return title[:max_length] + "..."
    else:
        return title

def get_and_resize_image(url, height):
    """
    Returns the image of a given url resized to a given height

    args:
        url (str): The url of the image
        height (int): The height to which the image should be resized
    return:
        image (PIL Image): The image resized to the given height
    """
    response = requests.get(url)
    image = Image.open(BytesIO(response.content))
    image.thumbnail((image.width, height)) 
    return image


def get_neighbours(title, n=10):
    """
    Returns the 'n' nearest neighbours of a given movie

    args:
        title_string (str): The title of the movie for which you want neighbours
        n (int): The number of neighbours you want; default is 10
    return:
        neighbours (list): A list of 'n' movie titles that are the nearest neighbours of the given movie
    """
    movie_inner_id = algo.trainset.to_inner_iid(title)
    neighbours = algo.get_neighbors(movie_inner_id, k=n)
    neighbours = [algo.trainset.to_raw_iid(inner_id) for inner_id in neighbours]
    return neighbours


def get_recommendations(movie_combo, n_recommendations=10):
    """
    Returns 'n' movie recommendations based on the genre combination provided

    args:
        movie_combo (dict): A dictionary with keys as genres and values as 0 or 1
        n_recommendations (int): The number of recommendations you want; default is 10
    return:
        recommendations (list): A list of 'n' movie titles that are recommended based on the genre combination provided
    """
    combo_df = pd.DataFrame([movie_combo])
    sim_scores = cosine_similarity(movie_genres_sparse, combo_df)
    sim_scores = list(enumerate(sim_scores))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[:n_recommendations]
    similar_movies = [i[0] for i in sim_scores]
    return movie_df['title'].iloc[similar_movies].tolist()

# load the image data in dictionary format with (k,v) as (title, image_url)
with open(get_path("images.pkl"),'rb') as f:
    images = pickle.load(f)

# load the sparse matrix of movie genres with one column representing a unique genre
# and  a row representing a movie
with open(get_path("movie_genres_sparse.pkl"),'rb') as f:
    movie_genres_sparse = pickle.load(f)

# load the movie dataframe with just one column, the title of the movie
with open(get_path('movie_df.pkl'),'rb') as f:
    movie_df = pickle.load(f)

# load the trained KNNBaseline model
with open(get_path("algo.pkl"),'rb') as f:
    algo = pickle.load(f)