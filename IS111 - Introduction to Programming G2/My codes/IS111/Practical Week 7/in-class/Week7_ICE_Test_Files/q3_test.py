import q3

# Test case 1 - Pangram
sentence = "The quick brown fox jumps over the lazy dog."
print(q3.is_pangram(sentence))

# Test case 2 - Not a Pangram
sentence = "The quick brown fox jumps over the lazy cat."
print(q3.is_pangram(sentence))

# Test case 3 - Pangram
sentence = "How vexingly quick daft zebras jump!"
print(q3.is_pangram(sentence))

# Test case 4 - Pangram
sentence = "Pack my box with five dozen liquor jugs."
print(q3.is_pangram(sentence))