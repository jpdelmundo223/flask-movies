from flask import Blueprint, render_template, abort, jsonify, g, session
from .request import get_movie, get_movie_details, get_movie, get_movie_genres, sample_func
from .utils import get_trailer

genre_list = []

views = Blueprint('views', __name__)

@views.route('/test_json')
def test():
    return get_movie("popular")

@views.route('/')
def index():    
    genres = get_movie_genres()['genres']
    for index in range(len(genres)):
        genre_list.append(genres[index]['name'])
    print(genre_list)
    get_popular_movies = get_movie("popular")
    get_toprated_movies = get_movie("top_rated")
    get_upcoming_movies = get_movie("upcoming")
    return render_template('movies/index.html', popular=get_popular_movies['results'], toprated=get_toprated_movies['results'], upcoming=get_upcoming_movies['results'])

# @views.route('/image')
# def details():
#     movie_image = m.get_image("bcCBq9N1EMo3daNIjWJ8kYvrQm6.jpg", "w500")
#     return f'<img src="{movie_image}" />'

@views.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    try:
        movie = get_movie_details(movie_id)
    except:
        abort(404)
        
    video = get_movie_details(movie_id)
    print(video)
    # trailer = ""
    # if video['results']['type'] == 'Trailer':
    #     trailer = "https://www.youtube.com/watch?v={}".format(video['results']['key'])

    # print(trailer)

    trailer = get_trailer(movie_id)
    
    return render_template('movies/details.html', movie=movie, trailer=trailer)

