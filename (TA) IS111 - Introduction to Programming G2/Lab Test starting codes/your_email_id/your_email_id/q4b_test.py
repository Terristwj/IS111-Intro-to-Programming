from q4b import get_user_preferences_by_category

print('--- Test Case 1 ---')
print()
result = get_user_preferences_by_category('beverage_preference.txt', 'TEA')
expected = {
            'Alice': [
                      ('Black Tea Mousse', 0.5)
                     ],
            'Bob': [
                    ('Pearl Milk Tea', 0.2),
                    ('Black Tea Mousse', 0.5)
                   ],
            'Cheryl': [
                       ('Pearl Milk Tea', 0.2)
                      ],
            'Mary': [
                     ('Black Tea Mousse', 0.3)
                    ]
           }
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

result = get_user_preferences_by_category('beverage_preference.txt', 'WHITE WINE')
expected = {
            'Marc': [
                     ('Sauvignon Blanc', 0.5)
                    ],
            'Prakash': [
                        ('Sauvignon Blanc', 1.0)
                       ]
           }
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 2: {"Passed" if expected == result else "Fail"}')
print('-------------------')

print()

print('--- Test Case 3 ---')
print()

result = get_user_preferences_by_category('beverage_preference.txt', 'CHAMPAGNE')
expected = {}
print(f'Expected: {expected}')
print(f'Actual  : {result}')
print()
print(f'Test Case 3: {"Passed" if expected == result else "Fail"}')
print('-------------------')
