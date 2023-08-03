# Name:
# Email ID:

import itertools

def print_puzzle(puzzle):
    print(' |0 1 2 3 4 5 6 7 ')
    print('-' * 17)
    index = 0
    for row in puzzle:
        print(str(index) + '|', end='')
        index = index + 1
        for ch in row:
            print(ch + ' ', end='')
        print()
        
def solve_puzzle(puzzle, word_positions, key, vocabulary):
    # Replace the code below with your implementation.
    board = []
    h_board = []
    # Create the 2D board and store all the values inside
    for row in puzzle:
        for char in row:
            h_board.append(char)
        board.append(h_board)
        h_board = []

    # Store all the words into the list. Store the coord of * into the list as well. As it is needed for the final portion of the solution
    words = []
    for i in word_positions:
        word = ""
        missing = ""
        if i[2] == 'H':
            for x in range(i[3]):
                if board[i[0]][i[1]+x] == "*":
                    missing = (i[0], i[1]+x)
                word += board[i[0]][i[1]+x]
            words.append([word, missing])


        elif i[2] == 'V':
            for x in range(i[3]):
                if board[i[0]+x][i[1]] == "*":
                    missing = (i[0]+x, i[1])
                word += board[i[0]+x][i[1]]
            words.append([word, missing])

    print("words ",words)

    confirmed = [(i[0],i[1]) for i in words if "*" in i[0]]
    print("confirmed " ,confirmed)

    result = [] # Will store all the solved puzzle
    for puz in confirmed:
        for k in key:
            if puz[0].replace("*", k) in vocabulary:
                dd = puz[1] + (k,)
                result.append(dd)

    print("result ",result)

    _ = [result.remove(i) for i in result if result.count(i) > 1] # Remove any duplicate value
    coords_only = [i[:2] for i in result]

    print("coords only ",coords_only)

    unique_coords = [i for i in coords_only if coords_only.count(i) == 1] # remove any duplicate coords

    print("unique ",unique_coords)

    cleaned_solution = []
    for i in result:
        if i[:2] in unique_coords: # String slicing to get the coords
            key = key.replace(i[-1],"") # Remove from keylist
            cleaned_solution.append(i)

    print(key)
    print(cleaned_solution)

    for i in result:
        if i[-1] in key:
            cleaned_solution.append(i)


    return cleaned_solution
    # print(vocabulary)


# =====================================================
# ==================== FOR TESTING ====================
# =====================================================

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
print(result)
exit()
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



