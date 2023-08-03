##
# Author : Stephen Pang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def get_prime_numbers(num_list):
    # YOUR CODE GOES HERE
    # prime_list = []
    # for num in num_list:
    #     is_prime = True
    #     for i in range(2, num):
    #         if num % i == 0:
    #             is_prime = False
    #     if is_prime:
    #         prime_list.append(num)
    # return prime_list

    prime_list = []
    for num in num_list:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
        if is_prime:
            prime_list.append(num)
    return prime_list

# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = get_prime_numbers([2,5,6,100,13])
print("Expected: [2, 5, 13]" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_prime_numbers([3,5,7,11,19])
print("Expected: [3, 5, 7, 11, 19]" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_prime_numbers([6,9,15,22,80,77])
print("Expected: []" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_prime_numbers([])
print("Expected: []" )
print("Actual:   " + str(result))
print()