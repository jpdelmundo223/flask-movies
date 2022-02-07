from .request import Movies

m = Movies()

def get_movie_trailer(movie_id):
    video = m.get_movie_trailer(movie_id)['results']
    for key in range(len(video)):
        if video[key]['type'] == "Trailer":
            trailer = "https://www.youtube.com/embed/{}".format(video[key]['key'])
    return trailer