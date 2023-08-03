
sentence = input("Enter a sentence: ")

word_list = sentence.split(" ")

print("There are a total of " + str(len(word_list)) + " words in this sentence. They are: ")
for word in word_list:
    print(word)


