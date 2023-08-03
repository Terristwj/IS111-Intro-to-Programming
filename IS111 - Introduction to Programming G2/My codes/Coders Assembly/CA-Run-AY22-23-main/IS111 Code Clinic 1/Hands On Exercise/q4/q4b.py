##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def decode_formula(string):
    # YOUR CODE GOES HERE
    num1 = ""
    optr = ""
    num2 = ""
    div_count = 0

    for ch in string:
        if ch in "+-/*":
            if ch == "/":
                div_count += 1
            if div_count == 2:
                optr = "//"
            else:
                optr = ch
        if ch.isnumeric():
            if optr:
                num2 += ch
            else:
                num1 += ch
    if num1[0] == "0":
        num1 = num1[1:]
    if num2[0] == "0":
        num2 = num2[1:]
    print(num1,optr,num2)
    return eval(str(num1) + optr + str(num2))
        
        
    
        

# DO NOT MODIFY THE CODE BELOW:
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
print("Expected: 2501024627" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = decode_formula('SoCh0a5*sok2sapsms')
print("Expected: 10" )
print("Actual:   " + str(result))
print()