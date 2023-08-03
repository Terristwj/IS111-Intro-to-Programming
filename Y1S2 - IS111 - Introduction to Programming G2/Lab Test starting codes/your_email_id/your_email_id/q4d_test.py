from q4d import get_user_with_highest_rating

print('--- Test Case 1 ---')
print()
result = get_user_with_highest_rating('beverage_preference.txt', 'Caramel Frappuccino')
expected = ('Mary', 0.6)
print(f'Expected: {expected}')
print(f'Actual  : {result}')

print(f'Expected type: {type(expected)}')
print(f'Actual type  : {type(result)}')
print()
print(f'Test Case 1: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 2 ---')
print()

result = get_user_with_highest_rating('beverage_preference.txt', 'Black Tea Mousse')
expected = ('Alice', 0.5)
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 3 ---')
print()

result = get_user_with_highest_rating('beverage_preference.txt', 'Evian Water')
expected = (None, 0)
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 3: {"Passed" if expected == result else "Fail"}')
print('-------------------')
