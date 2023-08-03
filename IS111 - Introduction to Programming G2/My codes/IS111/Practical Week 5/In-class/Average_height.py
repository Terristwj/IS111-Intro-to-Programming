def compute_avg_height(string):
    total_num = 0
    number_of_people = 0
    for words in string.replace(" ","").split("m"):
        if len(words) != 0:
            if words[-1].isnumeric():
                temp_word = words
                temp_num = ""
                for word in temp_word:
                    if word.isnumeric() or word == ".":
                        temp_num += word
                temp_num = temp_num
                total_num += float(temp_num)
                number_of_people += 1
    return total_num / number_of_people
    
print(compute_avg_height("Jonathan Li:1.75m, Lim, Josephine : 1.59m , George Khoo:   1.7 m"))