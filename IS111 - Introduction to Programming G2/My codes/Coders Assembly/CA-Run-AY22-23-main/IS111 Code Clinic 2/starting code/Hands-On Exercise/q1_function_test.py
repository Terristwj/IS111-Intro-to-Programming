import q1

print("===============TEST CASES FOR PART (A)====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q1.banned_words('sa',['them','call','lolling','sarah','hall','mimosa'])
print("Expected: ['sarah', 'mimosa']")
print("Actual  : " + str(result))
print()
print("Expected type of returned value: <class 'list'>")
print("Actual type of returned value  : " + str(type(result)))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
result = q1.banned_words('lle',['paradox','omega','falafel'])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q1.banned_words('ras',[])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print() 

print("===============TEST CASES FOR PART (C)====================")
print()
print("====================")
print()

# Test Case 1:
print("Test Case #1:")
print()
result = q1.banned_words2(['str','int','num'],['numbers','ontegers','marry','integer','string'])
print("Expected: ['numbers', 'integer', 'string']")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 2:

print("Test Case #2:")
print()
result = q1.banned_words2(['ill','bor','hap','ness'],['happiness','prosperity','death','boredom','fairwill','illness'])
print("Expected: ['happiness', 'boredom', 'fairwill', 'illness']")
print("Actual  : " + str(result))
print()
print("====================")
print()

# Test Case 3:

print("Test Case #3:")
print()
result = q1.banned_words2(['lay','sar','choo'],[])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print() 

# Test Case 3:

print("Test Case #4:")
print()
result = q1.banned_words2([],['lunatic','dongle','scent','horrible'])
print("Expected: []")
print("Actual  : " + str(result))
print()
print("====================")
print() 