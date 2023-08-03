import q10

print("===============TEST CASES FOR Q10====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q10.surround([['','','','','X'],['','','','',''],['','','','',''],['','','','','']])
print("Expected: [['', '', '', 'O', 'X'], ['', '', '', '', 'O'], ['', '', '', '', ''], ['', '', '', '', '']]")
print("Actual  : " + str(result))
print()
print("====================")
print()



# Test Case 2:

print("Test Case #2:")
print()
result = q10.surround([['', '', 'X', '', ''], ['', '', '', '', ''], ['', '', '', '', ''], ['', '', '', '', '']])
print("Expected: [['', 'O', 'X', 'O', ''], ['', '', 'O', '', ''], ['', '', '', '', ''], ['', '', '', '', '']]")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q10.surround([['', '', '', ''], ['', '', '', ''], ['', '', 'X', ''], ['', '', '', '']])
print("Expected: [['', '', '', ''], ['', '', 'O', ''], ['', 'O', 'X', 'O'], ['', '', 'O', '']]")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 4:

print("Test Case #4:")
print()
result = q10.surround([['', '', '', '','','','','','','','','','','','','',''], ['', '', '', '','','','','','','','','','','','','',''], ['X', '', '', '','','','','','','','','','','','','','']])
print("Expected: [['', '', '', '','','','','','','','','','','','','',''], ['O', '', '', '','','','','','','','','','','','','',''], ['X', 'O', '', '','','','','','','','','','','','','','']]")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 5:

print("Test Case #5:")
print()
result = q10.surround([['', '', '', '','','','','','','','','','','','','',''], ['', '', '', '','','','','','','','','','','','','',''], ['', '', '', '','','','','','X','','','','','','','','']])
print("Expected: [['', '', '', '','','','','','','','','','','','','',''], ['', '', '', '','','','','','O','','','','','','','',''], ['', '', '', '','','','','O','X','O','','','','','','','']]")
print("Actual  : " + str(result))
print()
print("====================")
print()