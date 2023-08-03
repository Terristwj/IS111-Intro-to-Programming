from q3b import retrieve_low_income_households

income_dict = {
                15: (12340, 4),
                32: (19344, 5),
                14: (3115, 2),
                3: (7569, 6),
                7: (15398, 5),
                13: (2340, 1),
                31: (13567, 4),
                12: (3115, 3),
                4: (7625, 3),
                8: (8357, 5)
              }

print('--- Test Case 1 ---')
print()
result = retrieve_low_income_households(income_dict, 2383.56)
expected = [14, 3, 13, 12, 8]
print(f'Expected: {expected}')
print(f'Actual  : {result}')

print(f'Expected type: {type(expected)}')
print(f'Actual type  : {type(result)}')
print()
print(f'Test Case 1: {"Passed" if expected == result else "Fail"}')
print('-------------------')
