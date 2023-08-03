from q4a import read_file

print('--- Test Case 1 ---')
print()
result = read_file('beverage_preference.txt')
expected = {
            'Alice': [
                      ('Black Tea Mousse', 'TEA', 0.5),
                      ('Americano', 'COFFEE', 0.5)
                     ],
            'Bob': [
                    ('Pearl Milk Tea', 'TEA', 0.2),
                    ('Black Tea Mousse', 'TEA', 0.5),
                    ('Caramel Frappuccino', 'COFFEE', 0.3)
                   ],
            'Cheryl': [
                       ('Pearl Milk Tea', 'TEA', 0.2),
                       ('Americano', 'COFFEE', 0.8)
                      ],
            'Mary': [
                     ('Black Tea Mousse', 'TEA', 0.3),
                     ('Americano', 'COFFEE', 0.1),
                     ('Caramel Frappuccino', 'COFFEE', 0.6)
                    ],
            'Marc': [
                     ('Sauvignon Blanc', 'WHITE WINE', 0.5),
                     ('Bordeaux Rouge', 'RED WINE', 0.5)
                    ],
            'Prakash': [
                        ('Sauvignon Blanc', 'WHITE WINE', 1.0)
                       ]
           }
print(f'Expected: {expected}')
print(f'Actual  : {result}')

print(f'Expected type: {type(expected)}')
print(f'Actual type  : {type(result)}')
print()
print(f'Test Case 1: {"Passed" if expected == result else "Fail"}')
print('-------------------')
