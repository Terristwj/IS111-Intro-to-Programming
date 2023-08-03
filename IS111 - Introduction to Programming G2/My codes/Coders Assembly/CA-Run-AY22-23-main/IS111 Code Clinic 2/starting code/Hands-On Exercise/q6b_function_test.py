import q6b

print("===============TEST CASES FOR Q6b====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q6b.binary_to_music2('1110010110001')
print("Expected: BEBD")
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
result = q6b.binary_to_music2('01111100100111110100')
print("Expected: FBEFBG")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q6b.binary_to_music2('100101110001101110000')
print("Expected: GABDABC")
print("Actual  : " + str(result))
print()
print("====================")
print()