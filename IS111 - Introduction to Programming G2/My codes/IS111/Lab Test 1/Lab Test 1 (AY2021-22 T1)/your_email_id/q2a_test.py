from q2a import get_right_most_even_digit

print()
print('-' * 20)
print()

print('Test Case 1: get_right_most_even_digit(7684357)')

print()

result = get_right_most_even_digit(7684357)
print('Expected: 4')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: get_right_most_even_digit(50570)')

print()

result = get_right_most_even_digit(50570) 
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: get_right_most_even_digit(853751)')

print()

result = get_right_most_even_digit(853751) 
print('Expected: 8')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4: get_right_most_even_digit(37953)')

print()

result = get_right_most_even_digit(37953)
print('Expected: None')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'NoneType'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()
