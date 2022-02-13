from .request import get_movie_trailer

def get_trailer(movie_id):
    video = get_movie_trailer(movie_id)['results']
    for key in range(len(video)):
        if video[key]['type'] == "Trailer":
            trailer = "https://www.youtube.com/embed/{}".format(video[key]['key'])
    return trailer

def join_items(items, separator):
    """Function that takes a list object then uses the .join() 
    function to join them and can receive customized separator 
    
    :param items: the list object to be iterated and joined
    :param separator: the separator that is going to be used"""
    for item in items:
        return separator.join(item)
