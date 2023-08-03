##
# Author : Stephen Pang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def reformat_string(input_string):
    # YOUR CODE GOES HERE
    new_string = ""
    vowels = 'aeiou'
    for ch in input_string.lower():
        if ch in vowels:
            new_string += ch.upper()
        else:
            new_string += ch.lower()
    return new_string

# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = reformat_string('HuiQing')
print("Expected: hUIqIng" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = reformat_string('MaRrenTilLOno')
print("Expected: mArrEntIllOnO" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = reformat_string('GeKItouTAISEn')
print("Expected: gEkItOUtAIsEn" )
print("Actual:   " + str(result))
print()