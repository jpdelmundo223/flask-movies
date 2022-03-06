from re import T
from flask import Blueprint, render_template, abort, jsonify, g, session, request
from .request import get_casts, get_movie, get_movie_details, get_movie, get_movie_genres, sample_func, search_movie, get_movie_trailer
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

@views.route('/movie/<int:movie_id>')
def movie_details(movie_id):
    try:
        movie = get_movie_details(movie_id)
    except:
        abort(404)
        
    casts = get_casts(movie_id)
    
    videos = get_movie_trailer(movie_id)['results']
    
    return render_template('movies/details.html', movie=movie, videos=videos, casts=casts)

@views.route('/movie/search/<string:keyword>')
def movie_search(keyword):
    result = search_movie(keyword)['results']
    return render_template('movies/search.html', keyword=keyword, result=result)