import sys

def print_test_case(puzzle, key):
    print()
    print_puzzle(puzzle)
    print()
    print("Key: " + key)
    print()

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

def read_vocab(file_name):
    vocab = []
    with open(file_name, 'r') as input_file:
        for line in input_file:
            line = line.rstrip()
            vocab.append(line.upper())
    return vocab

vocab = read_vocab('vocab_for_grading.txt')

# Test Cases
          
puzzle_answer = ['  SATIN ', 
                 '  T A   ', 
                 ' SAINT  ', 
                 '  I  I A', 
                 'SIN  N N', 
                 ' T   SIT', 
                 ' S      ', 
                 '        ']
word_positions = [(0, 2, 'H', 5), (2, 1, 'H', 5), (4, 0, 'H', 3), 
                  (5, 5, 'H', 3), (4, 1, 'V', 3), (0, 2, 'V', 5), 
                  (0, 4, 'V', 3), (2, 5, 'V', 4), (3, 7, 'V', 3)]

puzzle_0      = ['  SATIN ', 
                 '  T A   ', 
                 ' SA*NT  ', 
                 '  I  I A', 
                 'SIN  N N', 
                 ' T   SIT', 
                 ' S      ', 
                 '        ']
key_0 = 'I'

puzzle_1      = ['  SATIN ', 
                 '  T A   ', 
                 ' SAINT  ', 
                 '  I  I A', 
                 'SIN  * N', 
                 ' T   SIT', 
                 ' S      ', 
                 '        ']
key_1 = 'N'


puzzle_2      = ['  SATIN ', 
                 '  T A   ', 
                 ' SA*NT  ', 
                 '  I  I A', 
                 'SIN  * N', 
                 ' T   SIT', 
                 ' S      ', 
                 '        ']
key_2 = 'NI'

puzzle_3      = ['  *ATIN ', 
                 '  T A   ', 
                 ' SA*NT  ', 
                 '  I  I A', 
                 'SIN  * N', 
                 ' T   SI*', 
                 ' S      ', 
                 '        ']
key_3 = 'NITS'

# The first and the last test case are 0.5 marks.
# The second test case is 1 mark.
# The third test case is 2 marks.
test_cases = [(puzzle_0, word_positions, key_0, vocab, [(2, 3, 'I')], 0.5),
              (puzzle_1, word_positions, key_1, vocab, [(4, 5, 'N')], 0.5),
              (puzzle_2, word_positions, key_2, vocab, [(4, 5, 'N'), (2, 3, 'I')], 1.0),
              (puzzle_3, word_positions, key_3, vocab, [(4, 5, 'N'), (2, 3, 'I'), (5, 7, 'T'), (0, 2, 'S')], 2.0)]

# Counter is to record how many test cases are passed.
# Some test cases are given partial marks.
counter = 0.0

try:
    from q4 import solve_puzzle

    tc_no = 1

    for index in range(4):
        (puz, pos, k, v, result, marks) = test_cases[index]
        
        print()
        print("Test Case " + str(tc_no) + ":")
        tc_no += 1
        print_test_case(puz, k)
        print("Expected: " + str(result))             
        
        
        try:
            my_result = solve_puzzle(puz, pos, k, v)
            
            print("Actual  : " + str(my_result))
            
            if isinstance(my_result, list):
                if result != None:
                    my_result_set = set(my_result)
                    result_set = set(result)
                
                    if my_result_set == result_set:
                        counter += marks
                        print("passed")
                    else:
                        print("failed")
                else:
                    print("failed")
            
            
            elif my_result == result: # handle the None case
                counter += marks
                print("passed")
            else:
                print("failed")

        except:
            print('Exception:', sys.exc_info())
            print("failed")
            
except:
    print('Exception:', sys.exc_info())

# We allocate 4 marks for q4.
my_marks = counter

print("\nTotal marks: " + str(my_marks))