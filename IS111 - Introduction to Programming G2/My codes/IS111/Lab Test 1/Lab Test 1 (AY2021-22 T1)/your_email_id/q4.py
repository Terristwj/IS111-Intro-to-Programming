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
    word_list = []
    ast_pos = []

    for position in word_positions:
        row = position[0]
        col = position[1]
        dir = position[2]
        length = position[3]
        word = ""
        # print(row, col, dir, length)

        if dir == 'H' or dir == 'V':
            # print(row, col, dir, length)
            for i in range(length):
                if dir == 'H':
                    word += puzzle[row][col + i]
                else:
                    word += puzzle[row + i][col]

            # print(word)
            if "*" in word:
                word_list.append(word)
                if dir == 'H':
                    ast_pos.append([row, col + word.index("*")])
                else:
                    ast_pos.append([row + word.index("*"), col])
                    
    print(1, word_list)

    new_word_set_list = []
    ast_pos2 = []

    priority_list = []
    for i in range(len(word_list)):
        for ch in key:
            word = word_list[i].replace("*", ch)
            if word in vocabulary:
                new_word_set_list.append([word, ast_pos[i], ch])
                ast_pos2.append(ast_pos[i])

    for i in range(len(new_word_set_list)):
        if ast_pos2.count(new_word_set_list[i][1]) == 1:
            priority_list.append(new_word_set_list[i])

    used_key = []
    for i in range(len(priority_list)):
        used_key.append(priority_list[i][2])

    # for i in range(len(new_word_set_list)):
    #     if new_word_set_list[i][1]:
        
            
    print(2, new_word_set_list)
    print(3, priority_list)
    print(4, used_key)

    

    print(ast_pos)
    exit()
    return hor_word_list
        
