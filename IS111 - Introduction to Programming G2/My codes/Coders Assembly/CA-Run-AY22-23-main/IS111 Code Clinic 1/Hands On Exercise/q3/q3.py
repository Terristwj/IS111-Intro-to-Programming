##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

from operator import index


def get_min_average_max(tup_list):
    # YOUR CODE GOES HERE
    total_score_list = []
    for scores in tup_list:
        total_score_list.append(scores[0]+scores[1]+scores[2])
    
    lowest_score = total_score_list[0]
    average_score = total_score_list[0]
    highest_score = total_score_list[0]

    for score in total_score_list[1:]:
        if score < lowest_score:
            lowest_score = score
        if score > highest_score:
            highest_score = score
        average_score += score
    
    low_set = tup_list[total_score_list.index(lowest_score)]
    high_set = tup_list[total_score_list.index(highest_score)]

    average_score = average_score / len(total_score_list)

    return (low_set, average_score, high_set)

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = get_min_average_max([(3,5,4),(10,5,13),(2,100,30),(15,20,25),(80,72,10)])
print("Expected: ((3, 5, 4), 78.8, (80, 72, 10))" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_min_average_max([(5,10,20),(3,5,10),(10,2,34),(20,1,28)])
print("Expected: ((3, 5, 10), 37.0, (20, 1, 28))" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_min_average_max([(5,2,3)])
print("Expected: ((5, 2, 3), 10.0, (5, 2, 3))" )
print("Actual:   " + str(result))
print()