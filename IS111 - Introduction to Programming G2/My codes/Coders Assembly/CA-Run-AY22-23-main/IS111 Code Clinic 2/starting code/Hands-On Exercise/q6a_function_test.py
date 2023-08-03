import q6a

print("===============TEST CASES FOR Q6a====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q6a.binary_to_music("100110001110110001110010101101101")
print("Expected: GBDBBDBEAAA")
print("Actual  : " + str(result))
print()
print("Expected type of returned value: <class 'str'>")
print("Actual type of returned value  : " + str(type(result)))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
result = q6a.binary_to_music("010010010110001000000110010")
print("Expected: EEEBDCCBE")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q6a.binary_to_music("")
print("Expected: ")
print("Actual  : " + str(result))
print()
print("====================")
print()