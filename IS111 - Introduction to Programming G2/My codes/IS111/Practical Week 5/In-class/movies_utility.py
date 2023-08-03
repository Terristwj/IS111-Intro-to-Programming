def get_average_duration(movies):
    avg_duration = 0.0
    if movies:
        for movie in movies:
            avg_duration += movie[2]
        avg_duration = avg_duration / len(movies)
    return avg_duration

def get_num_movies_of_genre(movies, genre):
    counter = 0
    for movie in movies:
        if movie[1] == genre:
            counter += 1
    return counter

def get_title_of_longest_movie(movies):
    long_movie = ""
    if movies:
        long_duration = 0
        for movie in movies:
            if movie[2] > long_duration:
                long_duration = movie[2]
                long_movie = movie[0]
        return long_movie
    return long_movie

def get_movies_with_keyword(movies, keyword):
    new_movies = []
    if movies:
        for movie in movies:
            if keyword in movie[0]:
                new_movies.append(movie)
    return new_movies