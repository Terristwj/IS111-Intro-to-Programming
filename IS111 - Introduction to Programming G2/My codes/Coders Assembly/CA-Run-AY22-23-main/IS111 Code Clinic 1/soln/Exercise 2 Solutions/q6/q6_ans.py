##
# Author : Stephen Pang Qing Yang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def count_char(input_string,char):
    count = 0
    for ch in input_string:
        if ch.lower() == char:
            count += 1

    return count

print('----Test Case 1----')
result = count_char('HuiQing','i')
print("Expected: 2" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = count_char('MaRrenTilLOno','o')
print("Expected: 2" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = count_char('GeKItouTAISEn','z')
print("Expected: 0" )
print("Actual:   " + str(result))
print()