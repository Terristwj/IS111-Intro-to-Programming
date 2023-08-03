##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def sort_numbers(num_list):
    new_list = []
    # Get the largest number and lowest in the list
    largest_num = num_list[0]
    lowest_num = num_list[0]
    for num in num_list: 
        if num > largest_num:
            largest_num = num 
        if num < lowest_num: 
            lowest_num = num 

    # Use a for loop to go through from lowest num to largest num and add them to new list
    for i in range (lowest_num,largest_num+1): 
        for num in num_list: 
            if num == i: 
                new_list.append(num) 
    
    
    return new_list
        
        
    
        


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