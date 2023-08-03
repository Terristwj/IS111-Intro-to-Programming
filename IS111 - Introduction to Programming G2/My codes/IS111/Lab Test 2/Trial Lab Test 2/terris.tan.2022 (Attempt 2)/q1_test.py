from q1 import get_ppl_with_fever

print('Test Case 1:')
result = get_ppl_with_fever([('John', [37.6, 37.8]), ('George', [38.1, 37.2, 37.5]), ('Vivian', [36.7])])
print("Expected: ['John', 'George']")
print('Actual  : ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value  : ' + str(type(result)))


print('\nTest Case 2:')
result = get_ppl_with_fever([])
print("Expected: []")
print('Actual  : ' + str(result))

print('\nTest Case 3:')
result = get_ppl_with_fever([('Gideon', [36.5, 36.7]), ('Mary', [37.6, 36.8, 36.9, 36.8])])
print("Expected: []")
print('Actual  : ' + str(result))