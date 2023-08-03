from q3a import shift_string

print()
print('-' * 20)
print()

my_string = 'ABCDE'

print("Test Case 1: shift_string('" + my_string + "')")

print()

result = shift_string(my_string)
print("Expected: ['ABCDE', 'BCDEA', 'CDEAB', 'DEABC', 'EABCD']")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

my_string = '1234567'


print("Test Case 2: shift_string('" + my_string + "')")

print()

result = shift_string(my_string)
print("Expected: ['1234567', '2345671', '3456712', '4567123', '5671234', '6712345', '7123456']")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))


print()
print('-' * 20)
print()

my_string = ''


print("Test Case 3: shift_string('" + my_string + "')")

print()

result = shift_string(my_string)
print("Expected: []")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))


print()
print('-' * 20)
print()