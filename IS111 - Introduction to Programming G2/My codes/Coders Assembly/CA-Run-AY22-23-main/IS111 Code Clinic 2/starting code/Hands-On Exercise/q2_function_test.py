import q2

print("===============TEST CASES FOR Q2====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q2.unique_sort("hello world and practice makes perfect and hello world again")
print("Expected: again and hello makes perfect practice world")
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
result = q2.unique_sort("Its a fine line on who is really Disgusting and who is REALLY disgusting")
print("Expected: a and disgusting fine is its line on really who")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q2.unique_sort("Who is the one who said that the one is the person who is or are here")
print("Expected: are here is one or person said that the who")
print("Actual  : " + str(result))
print()
print("====================")
print()
