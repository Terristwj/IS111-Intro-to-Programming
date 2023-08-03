def unique_sort(sentence):
    ## YOUR CODE GOES BELOW ##
    words = sentence.split(' ')
    my_word_list = []
    for word in words:
        word = word.lower()
        if word not in my_word_list:
            my_word_list.append(word)
    my_word_list.sort()

    my_string = ''.join(i + " " for i in my_word_list)
    return my_string