# Name:
# Email ID:

def find_words(word_list, input_str, step):
    # Replace the code below with your implementation.
    index_list_list = []
    for word in word_list:
        index_list = []
        my_word = ''
        counter = 0
        first_run = True
        for ch in word:
            if first_run:
                for i in range(counter, len(input_str), 1):
                    counter += 1
                    if input_str[i] == ch:
                        index_list.append(i)
                        my_word += input_str[i]
                        first_run = False
                        break
            else:
                # counter += 1 ????
                # print(counter)
                for i in range(counter, len(input_str), step):
                    # print(input_str[i])
                    # print(counter, len(input_str), step)
                    counter += step
                    # print(counter, i, input_str[i], ch)
                    if input_str[i] == ch:
                        index_list.append(i)
                        my_word += input_str[i]
                        break
        if my_word == word:
            index_list_list.append(index_list)
        else:
            index_list_list.append([])
    return index_list_list