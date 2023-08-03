##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def transcribe_problematic_numlist(string): 
    # Initialize variables
    first_bracket = False
    return_list = []
    current_element = ""
    finished = False
    
    for ch in string: 
        
        if ch == "[":
            first_bracket = True
        
        elif first_bracket and not finished: 
            if ch.isdigit(): 
                current_element += ch
            elif ch == ",":
                if current_element != "":
                    return_list.append(int(current_element)) 
                    current_element = ""
        
        elif ch == "]": 
            finished = True
    
    if current_element != "":
        return_list.append(int(current_element)) 

    return return_list

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