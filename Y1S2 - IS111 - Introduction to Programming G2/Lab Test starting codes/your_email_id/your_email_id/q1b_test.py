from q1b import get_bill_with_gst

print('--- Test Case 1 ---')
print()
result = get_bill_with_gst(345.88, 2022)
expected = 345.88
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

result = get_bill_with_gst(400, 2022)
expected = 400.00
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 3 ---')
print()

result = get_bill_with_gst(650, 2022)
expected = 695.5
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 3: {"Passed" if expected == result else "Fail"}')
print('-------------------')


print()

print('--- Test Case 4 ---')
print()

result = get_bill_with_gst(345.88, 2023)
expected = 373.55
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 4: {"Passed" if expected == result else "Fail"}')
print('-------------------')


print()

print('--- Test Case 5 ---')
print()

result = get_bill_with_gst(400, 2023)
expected = 432.0
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 5: {"Passed" if expected == result else "Fail"}')
print('-------------------')


print()

print('--- Test Case 6 ---')
print()

result = get_bill_with_gst(745.88, 2024)
expected = 813.01
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 6: {"Passed" if expected == result else "Fail"}')
print('-------------------')
