import requests

BASE_URL = 'https://api.themoviedb.org/3/movie/{}'
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/{}/{}"
TRAILER_BASE_URL = "https://api.themoviedb.org/3/movie/{}/videos"
GENRES_URL = "https://api.themoviedb.org/3/genre/movie/list"
API_KEY = '16a1f43665a8603d33b87aee7bc14d9f'
params = dict(api_key=API_KEY)


def get_movie(category):
    """Helper function that will fetch all the movies 
        depending on which category the user has selected
    """
    r = requests.get(BASE_URL.format(category), params=params)
    return r.json()
    # self.category = category
    # return self.category

def get_image(poster_path, size):
    """Helper function that will fetch the movie json data 
        which contains the poster_path of the image.
    """
    r = requests.get(IMAGE_BASE_URL.format(size, poster_path))
    return r.url

def get_movie_details(movie_id):
    """Helper function that will fetch the movie json which
        contains all the information about the movie.
    """
    r = requests.get(BASE_URL.format(movie_id), params=params)
    return r.json()

def get_movie_trailer(movie_id):
    """Helper function to get the movie trailer
    """
    r = requests.get(TRAILER_BASE_URL.format(movie_id), params=params)
    return r.json()

def get_movie_genres():
    r = requests.get(GENRES_URL, params=params)
    return r.json()

def sample_func():
    return 1