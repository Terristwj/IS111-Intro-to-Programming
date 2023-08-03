from q2b import trim_number_with_list

print()
print('-' * 20)
print()

print("Test Case 1: trim_number_with_list(1006, [7]) ")

print()

result = trim_number_with_list(1006, [7]) 
print('Expected: 1006')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

##
print()
print('-' * 20)
print()

print("Test Case 2: trim_number_with_list(1006, [3])")

print()

result = trim_number_with_list(1006, [3])
print('Expected: 1003')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

##
print("Test Case 3: trim_number_with_list(1004, [7, 9, 2, 3])")

print()

result = trim_number_with_list(1004, [7, 9, 2, 3]) 
print('Expected: 1002')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

##
print('Test Case 4: trim_number_with_list(1009, [1, 0, 2])')

print()

result = trim_number_with_list(1009, [1, 0, 2])
print('Expected: 1001')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

##
print('Test Case 5: trim_number_with_list(1005, [7, 5, 8, 6, 9])')

print()

result = trim_number_with_list(1005, [7, 5, 8, 6, 9])
print('Expected: 1005')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()