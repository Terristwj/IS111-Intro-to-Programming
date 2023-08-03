def get_document_pair(filename):
    # Modify the code below.
    my_dict = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip("\n")
            cols = line.split("\t")

            key = cols[0]
            word_list = cols[1].split(" ")

            for word in word_list:
                if key in my_dict:
                    if word not in my_dict[key]:
                        my_dict[key].append(word)
                else:
                    my_dict[key] = [word]

    compare_counter = {}
    for key in my_dict:
        for key2 in my_dict:
            # Skip duplicate checks
            if key2+"-"+key not in compare_counter:
                counter = 0
                if key != key2:
                    for word in my_dict[key]:
                        for word2 in my_dict[key2]:
                            if word == word2:
                                counter += 1

                if counter != 0:
                    compare_counter[key+"-"+key2] = counter

    first_key = ""
    second_key = ""
    biggest_counter = 0
    for key in compare_counter:
        if compare_counter[key] >= biggest_counter:
            keys = key.split("-")
            first_key = keys[0]
            second_key = keys[1]
            biggest_counter = compare_counter[key]

    return (first_key, second_key, biggest_counter)
    
print(get_document_pair('documents.txt'))