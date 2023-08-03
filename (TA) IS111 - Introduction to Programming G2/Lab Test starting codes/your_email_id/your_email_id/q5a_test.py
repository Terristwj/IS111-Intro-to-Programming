from q5a import summarize_region_data

print('--- Test Case 1 ---')
print()
result = summarize_region_data('region_data.txt')
expected = {
            '2021-12-16T05:00:00': [8, 13, 37, 23, 27],
            '2021-01-14T15:00:00': [8, 13, 10, 11, 7],
            '2021-05-31T04:00:00': [12, 16, 19, 9, 16],
            '2021-05-14T17:00:00': [25, 9, 17, 18, 14],
            '2021-04-30T09:00:00': [11, 15, 16, 12, 13],
            '2021-05-08T01:00:00': [25, 0, 12, 23, 18],
            '2021-11-03T12:00:00': [33, 23, 31, 27, 25]
           }
print(f'Expected: {expected}')
print(f'Actual  : {result}')

print(f'Expected type: {type(expected)}')
print(f'Actual type  : {type(result)}')
print()
print(f'Test Case 1: {"Passed" if expected == result else "Fail"}')
print('-------------------')
