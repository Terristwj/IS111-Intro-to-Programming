##
# Author : Stephen Pang Qing Yang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def isFactor(num,factor):
    if factor == 0 or factor == 1:
        return None
    elif (num % factor == 0):
        return True
    else:
        return False


print('----Test Case 1----')
result = isFactor(5,2)
print("isFactor(5,2)")
print("Expected Type: <class 'bool'>")
print("Expected: False" )
print("Actual:   " + str(result))
print("Actual Type: " + str(type(result)))
print()
print('----Test Case 2----')
result = isFactor(30,2)
print("isFactor(30,2)")
print("Expected Type: <class 'bool'>")
print("Expected: True" )
print("Actual:   " + str(result))
print("Actual Type: " + str(type(result)))
print()
print('----Test Case 3----')
result = isFactor(100,0)
print("isFactor(100,0)")
print("Expected: None" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = isFactor(45,1)
print("isFactor(45,1)")
print("Expected: None" )
print("Actual:   " + str(result))
print()