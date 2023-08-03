##
# This question was adapted from SPM Programming Exercise, Roman Numerals
# Author : Stephen Pang Qing Yang
# Created : August 30, 2021
# Last Updated : August 30, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def get_average_of_values(keyword,values_dict):
    # YOUR CODE GOES HERE
    avg = 0
    for key in values_dict:
        if keyword == key:
            for num in values_dict[key]:
                avg += num
            avg /= len(values_dict[key])
    return avg


# DO NOT MODIFY THE CODE BELOW

test_dict = {'Savona':[2,5,3,1,2,3], 'Morgana':[10,12,4,13,1,20,10,12], 'Lance':[2,5], 'Emmy':[25]}


print('----Test Case 1----')
result = get_average_of_values('Morgana',test_dict)
print("Expected: 10.25" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_average_of_values('Emmy',test_dict)
print("Expected: 25.0" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_average_of_values('Caslyn',test_dict)
print("Expected: 0.0" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_average_of_values('Lance',test_dict)
print("Expected: 3.5" )
print("Actual:   " + str(result))
print()