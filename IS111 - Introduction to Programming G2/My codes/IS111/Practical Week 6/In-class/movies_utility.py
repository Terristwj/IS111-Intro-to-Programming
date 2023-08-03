def get_title_of_longest_movie(movie_list):
    longest_duration = movie_list[0][2]
    movie_title = movie_list[0][0]
    for i in range(1, len(movie_list)):
        if movie_list[i][2] > longest_duration:
            longest_duration = movie_list[i][2]
            movie_title = movie_list[i][0]
    return movie_title

def get_movies_with_keyword(movie_list, keyword):
    new_movie_list = []
    for movie in movie_list:
        if keyword in movie[0]:
            new_movie_list.append(movie)
    return new_movie_list

def get_average_duration(movie_list):
    avg_time = 0.0
    if movie_list:
        for movie in movie_list:
            avg_time += movie[2]
        avg_time /= len(movie_list)
    return avg_time

def get_num_movies_of_genre(movie_list, genre):
    num_movies = 0
    for movie in movie_list:
        if movie[1] == genre:
            num_movies += 1
    return num_movies