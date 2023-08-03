# YOUR CODE GOES HERE
# Copy and paste your code from q1.py over here
text = input("Enter a sentence: ")
print("There are a total of", len(text.split()), "words in this sentence. They are:")

said_word = []
for word in text.split():
    if word not in said_word:
        print(word)
        said_word.append(word)

