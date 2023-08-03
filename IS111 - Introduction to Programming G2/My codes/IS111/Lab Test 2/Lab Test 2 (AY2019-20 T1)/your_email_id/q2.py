# Name:
# Email ID:

def get_longer_words(file_name):
    # Modify the code below.
    largest_str = []
    with open(file_name) as f:
        for line in f:
            line = line.rstrip("\n")
            word1 = line.split("&")[0]
            word2 = line.split("&")[1]
            if len(word1) >= len(word2):
                largest_str.append(word1)
            else:
                largest_str.append(word2)
    return largest_str