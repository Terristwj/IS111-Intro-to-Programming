# YOUR CODE GOES HERE
text = input("Enter a sentence: ")
print("There are a total of", len(text.split()), "words in this sentence. They are:")

for word in text.split():
    print(word)