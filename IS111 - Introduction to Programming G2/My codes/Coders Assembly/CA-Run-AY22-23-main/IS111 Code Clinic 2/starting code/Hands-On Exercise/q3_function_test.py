import q3

print("===============TEST CASES FOR Q3====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q3.compute_steps(5,3,3,2)
print("Expected: 2.24")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
result = q3.compute_steps(0,0,0,0)
print("Expected: 0")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q3.compute_steps(5,5,5,3)
print("Expected: 2")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 4:

print("Test Case #4:")
print()
result = q3.compute_steps(0,4,1,1)
print("Expected: 4")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 5:

print("Test Case #5:")
print()
result = q3.compute_steps(10,4,5,2)
print("Expected: 6.71")
print("Actual  : " + str(result))
print()
print("====================")
print()