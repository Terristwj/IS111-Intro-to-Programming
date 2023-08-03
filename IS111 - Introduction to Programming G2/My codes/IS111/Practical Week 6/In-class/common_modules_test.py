from common_modules import check_common_modules

print('Test Case 1')
print()

s_list = [('Zeus',['IS01', 'IS02', 'CS03', 'STAT01']),
          ('Apollo', ['IS02', 'CS04', 'ECON02']),
          ('Athena', ['CS10', 'CT07', 'STAT10']),
          ('Ares', ['CS11', 'CT03', 'STAT10'])]

result = check_common_modules(s_list)

print('Expected: True')
print('Actual:   ' + str(result))

print("Expected type: <class 'bool'>")
print("Actual type  : " + str(type(result)))

print()

print('Test Case 2')
print()

s_list = [('Zeus',['IS01', 'IS02', 'CS03', 'STAT01']),
          ('Apollo', ['IS02', 'CS04', 'ECON02']),
          ('Athena', ['CS10', 'CT07', 'STAT10']),
          ('Hades', ['ECON02', 'IS01', 'STAT01']),
          ('Hera'), ['STAT01', 'ECON02', 'IS02']]

result = check_common_modules(s_list)

print('Expected: False')
print('Actual:   ' + str(result))

print()

print('Test Case 3')
print()

s_list = [('Zeus',['IS01', 'IS02', 'CS03', 'STAT01'])]

result = check_common_modules(s_list)

print('Expected: False')
print('Actual:   ' + str(result))

print()