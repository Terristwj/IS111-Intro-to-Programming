def count_vowel(input_str):
    count = 0
    for ch in input_str:
        if ch.lower() in 'aeiou':
            count += 1

    return count

# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = count_vowel('Anecdote')
print("Expected: 4" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = count_vowel('Cjkl')
print("Expected: 0" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = count_vowel('lUnacy')
print("Expected: 2" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = count_vowel('Can you stop doing this')
print("Expected: 7" )
print("Actual:   " + str(result))
print()