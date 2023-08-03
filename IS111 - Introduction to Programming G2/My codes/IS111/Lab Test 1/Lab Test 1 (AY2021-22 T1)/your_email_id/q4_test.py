from q4 import print_puzzle, solve_puzzle

def read_vocab(file_name):
    vocab = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            line = line.rstrip()
            vocab.append(line.upper())
    return vocab

vocabulary = read_vocab('vocabulary.txt')

print()
print('-' * 20)
print()

puzzle = ['BRE* BED', 
          '     * I', 
          '  BIRD R', 
          '  I I  *', 
          'R *IDE  ', 
          'I D     ', 
          '*RIDE   ', 
          '  E     ']
word_positions = [(0, 0, 'H', 4), (0, 5, 'H', 3), (2, 2, 'H', 4), 
                  (4, 2, 'H', 4), (6, 0, 'H', 5), (0, 5, 'V', 3),
                  (0, 7, 'V', 4), (2, 2, 'V', 6), (2, 4, 'V', 3),
                  (4, 0, 'V', 3)]
key = 'BDEIR'

print("Test Case 1:")
print("\nThe puzzle:\n")
print_puzzle(puzzle)
print("\nThe key: " + key)
print()

result = solve_puzzle(puzzle, word_positions, key, vocabulary)
expected_result = [(0, 3, 'D'), (1, 5, 'I'), (3, 7, 'E'), (4, 2, 'R'), (6, 0, 'B')]

# sort both lists such that the order doesn't matter
print('Expected: ' + str(sorted(expected_result)))
if isinstance(result, list):
    print('Actual:   ' + str(sorted(result)))
else:
    print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'list'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

puzzle = ['    L   ', 
          '  PL*D  ', 
          'GE* D   ', 
          'L E G   ', 
          'E *EE*  ', 
          'E G  E P', 
          '  E  E E', 
          '     LEG']
word_positions = [(1, 2, 'H', 4), (2, 0, 'H', 3), (4, 2, 'H', 4), 
                  (7, 5, 'H', 3), (2, 0, 'V', 4), (1, 2, 'V', 6),
                  (0, 4, 'V', 5), (4, 5, 'V', 4), (5, 7, 'V', 3)]
key = 'DELP'
exit()
print("Test Case 2:")
print("\nThe puzzle:\n")
print_puzzle(puzzle)
print("\nThe key: " + key)
print()

result = solve_puzzle(puzzle, word_positions, key, vocabulary)
expected_result = [(1, 4, 'E'), (2, 2, 'L'), (4, 2, 'D'), (4, 5, 'P')]

# sort both lists such that the order doesn't matter
print('Expected: ' + str(sorted(expected_result)))
if isinstance(result, list):
    print('Actual:   ' + str(sorted(result)))
else:
    print('Actual:   ' + str(result))
    
print()
print('-' * 20)
print()

puzzle = ['    L   ', 
          '  PL*D  ', 
          'GE* D   ', 
          'L E G   ', 
          'E *EE*  ', 
          'E G  E P', 
          '  E  E E', 
          '     LEG']
word_positions = [(1, 2, 'H', 4), (2, 0, 'H', 3), (4, 2, 'H', 4), 
                  (7, 5, 'H', 3), (2, 0, 'V', 4), (1, 2, 'V', 6),
                  (0, 4, 'V', 5), (4, 5, 'V', 4), (5, 7, 'V', 3)]
key = 'DDDD'

print("Test Case 3:")
print("\nThe puzzle:\n")
print_puzzle(puzzle)
print("\nThe key: " + key)
print()

result = solve_puzzle(puzzle, word_positions, key, vocabulary)

print('Expected: None')
print('Actual:   ' + str(result))
    
print()
print('-' * 20)
print()