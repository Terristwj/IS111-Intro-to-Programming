from q2a import trim_number

print()
print('-' * 20)
print()

print('Test Case 1: trim_number(1000, 5)')

print()

result = trim_number(1000, 5)
print('Expected: 1000')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

##
print()
print('-' * 20)
print()

print('Test Case 2: trim_number(5007, 2)')

print()

result = trim_number(5007, 2) 
print('Expected: 5002')
print('Actual:   ' + str(result))

##
print()
print('-' * 20)
print()

print('Test Case 3: trim_number(905, 5)')

print()

result = trim_number(905, 5) 
print('Expected: 905')
print('Actual:   ' + str(result))

##
print()
print('-' * 20)
print()

print('Test Case 4: trim_number(1, 5)')

print()

result = trim_number(1, 5)
print('Expected: 1')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()
