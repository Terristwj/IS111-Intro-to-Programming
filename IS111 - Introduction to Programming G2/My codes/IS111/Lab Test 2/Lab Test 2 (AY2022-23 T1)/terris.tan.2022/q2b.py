# Name:
# Email ID:

def filter_words(filename, end):
    # Replace the code below with your implementation.
    my_words = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            cols = line.split(' ')
            for word in cols:
                if word[-1] == end:
                    my_words.append(word)
    return my_words
