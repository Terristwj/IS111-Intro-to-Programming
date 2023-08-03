from q4c import get_user_rating_for

print('--- Test Case 1 ---')
print()
result = get_user_rating_for('beverage_preference.txt', 'Black Tea Mousse')
expected = [('Alice', 0.5), ('Bob', 0.5), ('Mary', 0.3)]
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

result = get_user_rating_for('beverage_preference.txt', 'Hot Chocolate')
expected = []
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')
