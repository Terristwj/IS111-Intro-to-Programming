import movies_utility

movie_list = [("The Shawshank Redemption", "drama", 142), 
        ("The Godfather", "drama", 175), 
        ("The Lord of the Rings: The Return of the King", "fantasy", 201), 
        ("Forrest Gump", "comedy", 142), 
        ("The Lord of the Rings: The Fellowship of the Ring", "fantasy", 178), 
        ("Star Wars: Episode IV - A New Hope", "fantasy", 121), 
        ("The Lion King", "animation", 88)]
        
print(movies_utility.get_average_duration(movie_list))

print(movies_utility.get_num_movies_of_genre(movie_list, "drama"))
print(movies_utility.get_num_movies_of_genre(movie_list, "fantasy"))

print(movies_utility.get_title_of_longest_movie(movie_list))
print(movies_utility.get_movies_with_keyword(movie_list, "King"))
print(movies_utility.get_movies_with_keyword(movie_list, "Lord"))