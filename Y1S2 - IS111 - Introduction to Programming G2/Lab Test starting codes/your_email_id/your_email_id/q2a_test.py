from q2a import get_ordered_list

print('--- Test Case 1 ---')
print()
result = get_ordered_list(3, 6)
expected = [3, 6]
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

result = get_ordered_list(6, 3)
expected = [3, 6]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 3 ---')
print()

result = get_ordered_list(3, 3)
expected = [3, 3]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 3: {"Passed" if expected == result else "Fail"}')
print('-------------------')
