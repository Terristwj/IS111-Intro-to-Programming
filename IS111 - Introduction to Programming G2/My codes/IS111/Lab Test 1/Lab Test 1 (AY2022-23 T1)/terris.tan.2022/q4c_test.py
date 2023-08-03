from q4c import find_overlap_size

print()
print('-' * 20)
print()

rect_a = ("A", -4, 1, 3, 2)
rect_b = ("B", -1, -2, 4, 3)
rect_c = ("C", 1, -4, 3, 3)
rect_d = ("D", -2, -1, 2, 3)
rect_e = ("E", 2, 1, 2, 2)

print('Rectangle A: ' + str(rect_a))
print('Rectangle B: ' + str(rect_b))
print('Rectangle C: ' + str(rect_c))
print('Rectangle D: ' + str(rect_d))
print('Rectangle E: ' + str(rect_e))

print()
print('-' * 20)
print()

print("Test Case 1: find overlap size between D and B")

print()

result = find_overlap_size(rect_d, rect_b)
print("Expected: 2")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()


print("Test Case 2: find overlap size between A and D")

print()

result = find_overlap_size(rect_a, rect_d)
print("Expected: 1")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 3: find overlap size between A and C")

print()

result = find_overlap_size(rect_a, rect_c)
print("Expected: 0")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 4: find overlap size between E and B")

print()

result = find_overlap_size(rect_e, rect_b)
print("Expected: 0")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'int'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()