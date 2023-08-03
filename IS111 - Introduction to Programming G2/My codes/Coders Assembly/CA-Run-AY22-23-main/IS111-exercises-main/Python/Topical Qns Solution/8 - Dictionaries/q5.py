wordcount_dict = {}

continue_asking = 'Yes'
while continue_asking == 'Yes':
    word = input("Enter the word: ")

    if word in wordcount_dict:
        wordcount_dict[word] += 1
    else:
        wordcount_dict[word] = 1

    continue_asking = input("Word added to dictionary. Continue adding? [Yes / No]")

print("Here are the following words present in your dictionary: ")
for word in wordcount_dict:
    if wordcount_dict[word] == 1:
        print(word + " with " + str(wordcount_dict[word]) + " appearance.")
    else:
        print(word + " with " + str(wordcount_dict[word]) + " appearances.")