##
# Author : Stephen Pang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def calculate(num1,num2,opr):
    # YOUR CODE GOES HERE
    # if opr == "+":
    #     return num1 + num2
    # elif opr == "-":
    #     return num1 - num2
    # elif opr == "*":
    #     return num1 * num2
    # elif opr == "/":
    #     return num1 / num2
    # elif opr == "//":
    #     return num1 // num2
    # elif opr == "**":
    #     return num1 ** num2

    if opr in "+-**//":
        return eval(str(num1) + opr + str(num2))
    return None

# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = calculate(1,3,'-')
print("calculate(1,3,'-')")
print("Expected: -2" )
print("Actual: " + str(result))
print()
print('----Test Case 2----')
result = calculate(12,5,'+')
print("calculate(12,5,'+')")
print("Expected: 17" )
print("Actual: " + str(result))
print()
print('----Test Case 3----')
result = calculate(8,10,'*')
print("calculate(8,10,'*')")
print("Expected: 80" )
print("Actual: " + str(result))
print()
print('----Test Case 4----')
result = calculate(9,12,'/')
print("calculate(9,12,'/')")
print("Expected: 0.75" )
print("Actual: " + str(result))
print()
print('----Test Case 5----')
result = calculate(100,14,'//')
print("calculate(100,14,'//')")
print("Expected: 7" )
print("Actual: " + str(result))
print()
print('----Test Case 6----')
result = calculate(5,3,'**')
print("calculate(5,3,'**')")
print("Expected: 125" )
print("Actual: " + str(result))
print()