from q1 import get_promotion

print()
print('-' * 20)
print()

print('Test Case 1: get_promotion("vegetable")')

print()

result = get_promotion('vegetable')
print('Expected: 5%')
print('Actual:   ' + result)

print("Expected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

##
print('Test Case 2: get_promotion("fruits")')

print()

result = get_promotion('fruits')
print('Expected: 7.5%')
print('Actual:   ' + result)

print()
print('-' * 20)
print()

##
print('Test Case 3: get_promotion("seasoningss")')

print()

result = get_promotion('seasoningss')
print('Expected: No Promotion')
print('Actual:   ' + result)

print()
print('-' * 20)
print()

##
print('Test Case 4: get_promotion(" ")')

print()

result = get_promotion(' ')
print('Expected: No Promotion')
print('Actual:   ' + result)

print()
print('-' * 20)
print()