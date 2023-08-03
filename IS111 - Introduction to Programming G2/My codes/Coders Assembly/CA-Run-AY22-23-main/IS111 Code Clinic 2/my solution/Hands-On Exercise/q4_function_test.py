import q4

print("===============TEST CASES FOR Q4====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q4.get_alpha_num('Po52*5_2+i2@so1n')
print("Expected: ('Poison', 17)")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
result = q4.get_alpha_num('Ma-2,5=R)c0-U-38s!@#')
print("Expected: ('MaRcUs', 8)")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q4.get_alpha_num('--5,5,6WON2(%De#R-92')
print("Expected: ('WONDeR', 1)")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 4:

print("Test Case #4:")
print()
result = q4.get_alpha_num('')
print("Expected: ('', 0)")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 5:

print("Test Case #5:")
print()
result = q4.get_alpha_num('--5--29')
print("Expected: ('', 2)")
print("Actual  : " + str(result))
print()
print("====================")
print()