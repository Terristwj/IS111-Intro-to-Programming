def get_title_of_longest_movie(movie_list):
    if movie_list == []:
        return ''
    
    # assume the longest movie is the first movie
    longest_movie = movie_list[0]
    for movie in movie_list:
        # compare the movies based on their durations
        if movie[2] > longest_movie[2]:
            longest_movie = movie
    
    # return the title of the longest movie
    return longest_movie[0]
    
def get_movies_with_keyword(movie_list, substring):
    if movie_list == []:
        return []
    
    # initialise the list to return
    list_to_return = []
    # iterate through the list. If the title of a movie contains the substring, 
    # then add the movie to the list to return
    for movie in movie_list:
        if substring in movie[0]:
            list_to_return.append(movie)
            
    return list_to_return
    
def get_average_duration(movie_list):
    if movie_list == []:
        return 0.0
    
    # initialise a sum variable
    sum_duration = 0
    # iterate through the list and get the duration of each movie. add it to the sum.
    for movie in movie_list:
        sum_duration += movie[2]
     
    # return the average duration
    return sum_duration / len(movie_list)

def get_num_movies_of_genre(movie_list, genre):
    
    # initialise a counter
    num_list_with_genre = 0
    
    # iterate through the list and check if the movies are from that genre.
    # if yes, increment the counter.
    for movie in movie_list:
        if movie[1] == genre:
            num_list_with_genre += 1 
            
    return num_list_with_genre