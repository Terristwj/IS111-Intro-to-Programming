# YOUR CODE GOES HERE
word_dict = {}
word = input("Enter the word: ")
word_dict[word] = 1
to_continue = input("Word added to dictionary. Continue adding? [Yes / No]")

while to_continue == "Yes":
    word = input("Enter the word: ")
    if word in word_dict:
        word_dict[word] += 1
    else:
        word_dict[word] = 1
    to_continue = input("Word added to dictionary. Continue adding? [Yes / No]")

print("Here are the following words present in your dictionary: ")
for word in word_dict:
    print(f"{word} with {word_dict[word]} appearances.")