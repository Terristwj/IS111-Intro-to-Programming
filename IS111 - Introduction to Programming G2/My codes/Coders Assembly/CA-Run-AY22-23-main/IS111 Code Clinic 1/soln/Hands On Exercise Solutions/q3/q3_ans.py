##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def get_min_average_max(tup_list):
    min_tup = ""
    max_tup = ""
    # Calculating Min and Max
    min_val = ""
    max_val = 0
    
    total = 0
    for num_tup in tup_list:
        value = 0
        for num in num_tup:
            value += num
            total += num
        # checking if higher than max
        if value > max_val:
            max_val = value
            max_tup = num_tup

        if min_val == "" or value < min_val:
            min_val = value
            min_tup = num_tup

    # Calculating average
    average = total / len(tup_list)

    return (min_tup, average, max_tup)

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