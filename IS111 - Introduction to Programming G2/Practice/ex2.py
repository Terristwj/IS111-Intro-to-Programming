movies = {'barbie': {'rank': 1, 'views': 1324831, 'date': '10/02/03', 'sales': 1239013}, 'transformer': {'rank': 2, 'views': 5678, 'date': '25/05/10', 'sales': 4513}, 'batman': {'rank': 3, 'views': 38759, 'date': '24/12/22', 'sales': 12233}}

# find the rank of transformer 
print(movies["transformer"]["rank"])

# find the date of barbie 
print(movies["barbie"]["date"])

# sum up the sales of all movies 
sum = 0
for movie in movies.keys():
    for data in movies[movie].keys():
        if data == "sales":
            sum += movies[movie][data]
print(sum)

# find the average of the views of all movies 
sum = 0
for movie in movies.keys():
    for data in movies[movie].keys():
        if data == "views":
            sum += movies[movie][data]
print(sum/len(movies))