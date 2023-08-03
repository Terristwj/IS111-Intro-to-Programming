from q2c import return_ordered_ints

print('--- Test Case 1 ---')
print()
result = return_ordered_ints([])
expected = []
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

result = return_ordered_ints([2])
expected = [2]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 3 ---')
print()

result = return_ordered_ints([3, 2])
expected = [2, 3]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 3: {"Passed" if expected == result else "Fail"}')
print('-------------------')


print()

print('--- Test Case 4 ---')
print()

result = return_ordered_ints([3, 6, 2])
expected = [2, 3, 6]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 4: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 5 ---')
print()

result = return_ordered_ints([6, 3, 5])
expected = [3, 5, 6]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 5: {"Passed" if expected == result else "Fail"}')
print('-------------------')


print()

print('--- Test Case 6 ---')
print()

result = return_ordered_ints([5, 3, 6, 5])
expected = [3, 5, 5, 6]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 6: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 7 ---')
print()

result = return_ordered_ints([18, 3, 27, 15])
expected = [3, 15, 18, 27]
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 7: {"Passed" if expected == result else "Fail"}')
print('-------------------')
