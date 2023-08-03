##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def transcribe_numlist(string): 
    # YOUR CODE GOES HERE
    new_string = ""
    for ch in string:
        if ch.isnumeric() or ch in "[,]":
            new_string += ch

    is_not_open = True
    front_remove = ""
    for ch in new_string:
        if is_not_open:
            if ch == "[":
                is_not_open = not is_not_open
            front_remove += ch
    new_string = new_string[len(front_remove):]

    is_not_close = True
    end_remove = ""
    for ch in new_string[::-1]:
        if is_not_close:
            if ch == "]":
                is_not_close = not is_not_close
            end_remove += ch
            
    new_string = new_string[:len(new_string)-len(end_remove)]

    num_list = []
    for num in new_string.split(","):
        num_list.append(int(num))
    return num_list

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = transcribe_numlist('[2,3,5,62,252]')
print("Expected: [2, 3, 5, 62, 252]" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = transcribe_numlist('aP#[&3,140B,23S2,20aa,34^]')
print("Expected: [3, 140, 232, 20, 34]" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = transcribe_numlist(')JEODOE32sa[P3S;fA,Doo2ew51,Sda1,!=-2fgg0,0]FSDWFSA')
print("Expected: [3, 251, 1, 20, 0]" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = transcribe_numlist('[OISDJFOIDSHJUIOHSDUIFHSDUIB1SO@OKOFEO]jhj')
print("Expected: [1]" )
print("Actual:   " + str(result))
print()