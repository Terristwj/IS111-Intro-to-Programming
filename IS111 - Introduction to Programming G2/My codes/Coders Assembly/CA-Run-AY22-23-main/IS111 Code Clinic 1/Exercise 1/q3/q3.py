##
# Author : Stephen Pang
# Created : July 31, 2021
# Last Updated : July 31, 2021
#
# This question was adapted from the FizzBuzz programming question
##

def fizzbuzz(num):
    # YOUR CODE GOES HERE
    # if num % 3 == 0 and num % 5 == 0:
    #     return "FizzBuzz"
    # else:
    #     if num % 3 == 0:
    #         return "Fizz"
    #     elif num % 5 == 0:
    #         return "Buzz"
    #     else:
    #         return num

    if num % 3 == 0 and num % 5 == 0:
        return 'FizzBuzz'
    if num % 3 == 0:
        return 'Fizz'
    if num % 5 == 0:
        return 'Buzz'
    return num

# DO NOT MODIFY THE CODE BELOW
print('----Test Case 1----')
result = fizzbuzz(4)
print("str_formation(4)")
print("Expected: 4" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = fizzbuzz(25)
print("str_formation(25)")
print("Expected: Buzz" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = fizzbuzz(15)
print("str_formation(15)")
print("Expected: FizzBuzz" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = fizzbuzz(21)
print("str_formation(21)")
print("Expected: Fizz" )
print("Actual:   " + str(result))
print()

