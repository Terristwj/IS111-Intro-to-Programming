from q1a import get_cif_in_sgd

print('--- Test Case 1 ---')
print()
result = get_cif_in_sgd(110.50, 0.125, 13.50)
expected = 181.32
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

result = get_cif_in_sgd(423.80, 0.15, 38.50)
expected = 696.45
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')


print()

print('--- Test Case 3 ---')
print()

result = get_cif_in_sgd(573.82, 0.18, 58.12)
expected = 972.22
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 3: {"Passed" if expected == result else "Fail"}')
print('-------------------')

