##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def get_shuriken_distance(horizontal,vertical):
    # YOUR CODE GOES HERE
    return round((horizontal**2 + vertical**2) ** (1/2), 2)

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = get_shuriken_distance(2,5)
print("Expected: 5.39" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_shuriken_distance(10,5.0)
print("Expected: 11.18" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_shuriken_distance(0,0.0)
print("Expected: 0.0" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_shuriken_distance(3.0,3.0)
print("Expected: 4.24" )
print("Actual:   " + str(result))
print()