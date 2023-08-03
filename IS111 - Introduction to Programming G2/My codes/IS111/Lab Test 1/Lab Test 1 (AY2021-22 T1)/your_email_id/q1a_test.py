from q1a import get_area_difference

print()
print('-' * 20)
print()

print('Test Case 1: get_area_difference(2, 4, 3, 3)')

print()

result = get_area_difference(2, 4, 3, 3)
print('Expected: 1')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: get_area_difference(4, 3, 2, 5)')

print()

result = get_area_difference(4, 3, 2, 5)
print('Expected: 2')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: get_area_difference(4, 6, 3, 8)')

print()

result = get_area_difference(4, 6, 3, 8)
print('Expected: 0')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()
