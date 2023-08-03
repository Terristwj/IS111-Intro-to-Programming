from q4b import find_overlapping_pairs

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

print("Test Case 1: find overlapping pairs among A, B and C")

print()

result = find_overlapping_pairs([rect_a, rect_b, rect_c])
print("Expected: [('B', 'C')] or [('C', 'B')]")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()


print("Test Case 2: find overlapping pairs among A, B and E")

print()

result = find_overlapping_pairs([rect_a, rect_b, rect_e])
print("Expected: []")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

print("Test Case 3: find overlapping pairs among A, B, C, D and E")

print()

result = find_overlapping_pairs([rect_a, rect_b, rect_c, rect_d, rect_e])
print("Expected: [('A', 'D'), ('B', 'C'), ('B', 'D')] or these pairs in any order")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()
