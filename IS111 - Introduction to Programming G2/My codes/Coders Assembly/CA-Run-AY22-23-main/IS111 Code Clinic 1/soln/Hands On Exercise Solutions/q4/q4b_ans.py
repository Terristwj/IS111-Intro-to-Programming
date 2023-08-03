##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def decode_formula(string):
    # initialize variables
    answer = ""
    first_num = ""
    operator = ""
    second_num = ""
    is_first = True
    is_operator = False
    is_second = False

    # Go through each character
    for ch in string:

        # Form first num
        if ch.isdigit() and is_first:
            first_num += ch
        
        elif ch in '*/+-' and is_first:
            is_first = False
            is_operator = True

        # Form operator
        if ch in '*/+-' and is_operator:
            operator += ch

        elif ch.isdigit() and is_operator:
            is_operator = False
            is_second = True
        
        # Form second num
        if ch.isdigit() and is_second:
            second_num += ch
    
    first_num = int(first_num)
    second_num = int(second_num)
    # Performing calculation
    if operator == '+':
        answer = first_num + second_num
    elif operator == "-":
        answer = first_num - second_num
    elif operator == "*":
        answer = first_num * second_num
    elif operator == "/":
        answer = first_num / second_num
    elif operator == "//":
        answer = first_num // second_num
    elif operator == "%":
        answer = first_num % second_num

    return answer
        
        
    
        


print('----Test Case 1----')
result = decode_formula('a3S-3o5AkE2b05#6')
print("Expected: -352053" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = decode_formula('@ka55Nsa/Sh/3iRo')
print("Expected: 18" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = decode_formula('2501024535-92')
print("Expected: 2501024443" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = decode_formula('SoCh0a5*sok2sapsms')
print("Expected: 10" )
print("Actual:   " + str(result))
print()