##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def transcribe_problematic_numlist(string): 
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
    no_num = True

    for ch in new_string:
        if ch.isnumeric():
            no_num = False

    if not no_num:
        for i in range(1, len(new_string)-1):
            prev_ch = new_string[i-1]
            ch = new_string[i]
            if prev_ch == "," and ch == ",":
                new_string = new_string[:i] + " " +new_string[i+1:]

        if new_string[0] == ",":
            new_string = new_string[1:]

        for num in new_string.split(","):
            if num != " ":
                num_list.append(int(num))
        return num_list
    else:
        return []

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = transcribe_problematic_numlist('[,,,,,]')
print("Expected: []" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = transcribe_problematic_numlist('aP,,#[&3,140B,23,,S2,20aa,34^]')
print("Expected: [3, 140, 23, 2, 20, 34]" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = transcribe_problematic_numlist(')JEODOE32sa[P3S;fA,,Doo2ew51,Sda1,!=-2fgg0,0]FSDWFSA')
print("Expected: [3, 251, 1, 20, 0]" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = transcribe_problematic_numlist('[OISDJFOIDS,,,IB1SO@OKOFEO]jhj')
print("Expected: [1]" )
print("Actual:   " + str(result))
print()