from q2b import insert_into_list

print('--- Test Case 1 ---')
print()
result = insert_into_list([3, 6], 2)
expected = [2, 3, 6]
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

result = insert_into_list([2, 5], 4)
expected = [2, 4, 5]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 3 ---')
print()

result = insert_into_list([1, 3], 7)
expected = [1, 3, 7]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 3: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 4 ---')
print()

result = insert_into_list([3, 5, 6], 5)
expected = [3, 5, 5, 6]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 4: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 5 ---')
print()

result = insert_into_list([3, 18, 27], 15)
expected = [3, 15, 18, 27]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 5: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 6 ---')
print()

result = insert_into_list([], 15)
expected = [15]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 6: {"Passed" if expected == result else "Fail"}')
print('-------------------')
