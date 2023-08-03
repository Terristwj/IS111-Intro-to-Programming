from q1b import is_official_language

print()
print('-' * 20)
print()

print('Test Case 1: is_official_language("Belgium", "French")')

print()

result = is_official_language("Belgium", "French")
print('Expected: True')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print('Test Case 2: is_official_language("Belgium", "Malay")')

print()

result = is_official_language("Belgium", "Malay")
print('Expected: False')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 3: is_official_language("Singapore", "German")')

print()

result = is_official_language("Singapore", "German")
print('Expected: False')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()

print('Test Case 4: is_official_language("Canada", "English")')

print()

result = is_official_language("Canada", "English")
print('Expected: True')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()
