##
# Author : Stephen Pang Qing Yang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def reformat_string(input_string):
    new_string = ""
    for ch in input_string:
        if ch in 'aeiou':
            new_string += ch.upper()
        else:
            new_string += ch.lower()

    
    return new_string


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