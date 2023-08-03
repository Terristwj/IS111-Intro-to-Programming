import q9

print("===============TEST CASES FOR Q9====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q9.get_nested_list('[ 1, 5, [ 2, 3, 5, [ 8 ], 5 ], 9 ]')
print("Expected: [2, 3, 5, 5]")
print("Actual  : " + str(result))
print()
print("====================")
print()



# Test Case 2:

print("Test Case #2:")
print()
result = q9.get_nested_list('[ 2, 3, [ [ 5, 2 ], 3, [5, [ [ [ 3 ] ] ], 6], 9 ] ]')
print("Expected: [3, 9]")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q9.get_nested_list('[2,3,[5,2]]')
print("Expected: [5, 2]")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 4:

print("Test Case #4:")
print()
result = q9.get_nested_list('[1, 2, 3, [5], 6]')
print("Expected: [5]")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 5:

print("Test Case #5:")
print()
result = q9.get_nested_list('[1,3, [] ]')
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print()