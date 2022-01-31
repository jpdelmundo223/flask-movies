import requests

BASE_URL = 'https://api.themoviedb.org/3/movie/{}'
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/{}/{}"
API_KEY = '16a1f43665a8603d33b87aee7bc14d9f'
params = dict(api_key=API_KEY)

class Movies():
    def __init__(self):
        self.category = ""

    def get_movie(self, category):
        """
            Description:
                This function is going to be responsible for returning 
                json response data from TMDB Api.
            
            Parameters:
                category - will hold the value for movie category
        """
        self.category = category
        r = requests.get(BASE_URL.format(self.category), params=params)
        return r.json()
        # self.category = category
        # return self.category

    def get_image(self, poster_path , size):
        """
            Description:
                This function will return a url containing the poster path
                and the size of the image to be rendered by the front end

            Parameters:
                poster_path - will hold the movie poster path/file name
                size - will hold the size of the image (w500, w300, original based on the API)
        """
        self.size = size
        self.poster_path = poster_path
        r = requests.get(IMAGE_BASE_URL.format(self.size, self.poster_path))
        return r.url

    def get_movie_details(self, movie_id):
        """
            Description:
                This function will return api call for an specific
                movie from movie_id.

            Parameters:
                movie_id = will hold the value for movie
        """
        self.movie_id = movie_id
        r = requests.get(BASE_URL.format(self.movie_id), params=params)
        return r.json()