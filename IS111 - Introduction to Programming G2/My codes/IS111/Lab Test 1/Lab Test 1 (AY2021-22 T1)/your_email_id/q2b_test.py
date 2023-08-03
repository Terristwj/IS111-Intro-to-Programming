from q2b import get_all_third_digits

print()
print('-' * 20)
print()

print("Test Case 1: get_all_third_digits(['IS113 G1', 'xyz1', '5-6-7-8', 'S$10,500']) ")

print()

result = get_all_third_digits(['IS113 G1', 'xyz1', '5-6-7-8', 'S$10,500']) 
print('Expected: [3, 7, 5]')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: get_all_third_digits(['987654', ''])")

print()

result = get_all_third_digits(['987654', ''])
print('Expected: [7]')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print("Test Case 3: get_all_third_digits(['abc', '10'])")

print()

result = get_all_third_digits(['abc', '10']) 
print('Expected: []')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4: get_all_third_digits([])')

print()

result = get_all_third_digits([])
print('Expected: []')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()
