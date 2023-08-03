##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def sort_numbers(num_list):
    # YOUR CODE GOES HERE
    new_list = []

    for i in range(len(num_list)):
        smallest_num = num_list[0]

        for num in num_list[1:]:
            if num < smallest_num:
                smallest_num = num
        
        num_list.pop(num_list.index(smallest_num))
        new_list.append(smallest_num)

    return new_list
        
        
    
        

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = sort_numbers([5,1,1,3,2,6])
print("Expected: [1, 1, 2, 3, 5, 6]" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = sort_numbers([-1,-2,2,3,10,6,12,11])
print("Expected: [-2, -1, 2, 3, 6, 10, 11, 12]" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = sort_numbers([-10,-12,-15,-10])
print("Expected: [-15, -12, -10, -10]" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = sort_numbers([2])
print("Expected: [2]" )
print("Actual:   " + str(result))
print()