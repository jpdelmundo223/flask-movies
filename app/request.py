import requests

BASE_URL = 'https://api.themoviedb.org/3/movie/{}'
IMAGE_BASE_URL = "https://image.tmdb.org/t/p/{}/{}"
TRAILER_BASE_URL = "https://api.themoviedb.org/3/movie/{}/videos"
API_KEY = '16a1f43665a8603d33b87aee7bc14d9f'
params = dict(api_key=API_KEY)

class Movies():
    def get_movie(self, category):
        """Helper function that will fetch all the movies 
            depending on which category the user has selected
        """
        self.category = category
        r = requests.get(BASE_URL.format(self.category), params=params)
        return r.json()
        # self.category = category
        # return self.category

    def get_image(self, poster_path, size):
        """Helper function that will fetch the movie json data 
            which contains the poster_path of the image.
        """
        self.poster_path = poster_path
        self.size = size
        r = requests.get(IMAGE_BASE_URL.format(self.size, self.poster_path))
        return r.url

    def get_movie_details(self, movie_id):
        """Helper function that will fetch the movie json which
            contains all the information about the movie.
        """
        self.movie_id = movie_id
        r = requests.get(BASE_URL.format(self.movie_id), params=params)
        return r.json()

    def get_movie_trailer(self, movie_id):
        """Helper function to get the movie trailer
        """
        self.movie_id = movie_id
        r = requests.get(TRAILER_BASE_URL.format(self.movie_id), params=params)
        return r.json()