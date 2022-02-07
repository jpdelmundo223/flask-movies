from flask import Blueprint, render_template, abort, jsonify
from .request import Movies
from .utils import get_movie_trailer

views = Blueprint('views', __name__)
m = Movies()

@views.route('/test_json')
def test():
    return m.get_movie("popular")

@views.route('/')
def index():
    get_popular_movies = m.get_movie("popular")
    get_toprated_movies = m.get_movie("top_rated")
    get_upcoming_movies = m.get_movie("upcoming")
    return render_template('movies/index.html', popular=get_popular_movies['results'], toprated=get_toprated_movies['results'])

# @views.route('/image')
# def details():
#     movie_image = m.get_image("bcCBq9N1EMo3daNIjWJ8kYvrQm6.jpg", "w500")
#     return f'<img src="{movie_image}" />'

@views.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    try:
        movie = m.get_movie_details(movie_id)
    except:
        abort(404)
        
    video = m.get_movie_details(movie_id)
    print(video)
    # trailer = ""
    # if video['results']['type'] == 'Trailer':
    #     trailer = "https://www.youtube.com/watch?v={}".format(video['results']['key'])

    # print(trailer)

    trailer = get_movie_trailer(movie_id)
    
    return render_template('movies/details.html', movie=movie, trailer=trailer)

