from q3a import create_avg_income_per_person_dict

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
result = create_avg_income_per_person_dict(income_dict)
expected = {
            15: 3085.0,
            32: 3868.8,
            14: 1557.5,
            3: 1261.5,
            7: 3079.6,
            13: 2340.0,
            31: 3391.75,
            12: 1038.33,
            4: 2541.67,
            8: 1671.4
           }
print(f'Expected: {expected}')
print(f'Actual  : {result}')

print(f'Expected type: {type(expected)}')
print(f'Actual type  : {type(result)}')
print()
print(f'Test Case 1: {"Passed" if expected == result else "Fail"}')
print('-------------------')
