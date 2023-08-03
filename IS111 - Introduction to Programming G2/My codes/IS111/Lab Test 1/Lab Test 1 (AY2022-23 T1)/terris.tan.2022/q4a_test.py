from q4a import is_overlapping

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

print("Test Case 1: A and B")

print()

result = is_overlapping(rect_a, rect_b)
print("Expected: False")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 2: B and C")

print()

result = is_overlapping(rect_b, rect_c)
print("Expected: True")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 3: E and B")

print()

result = is_overlapping(rect_e, rect_b)
print("Expected: False")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 4: D and A")

print()

result = is_overlapping(rect_d, rect_a)
print("Expected: True")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 5: A and C")

print()

result = is_overlapping(rect_a, rect_c)
print("Expected: False")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()
