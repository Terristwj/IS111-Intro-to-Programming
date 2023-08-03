# YOUR CODE GOES HERE
# Copy and paste your code from q1.py over here
sentence = input("Enter a sentence: ")

word_list = sentence.split(" ")

print("There are a total of " + str(len(word_list)) + " words in this sentence. They are: ")

# q1_b.py code
unique_word_list = []
for word in word_list:
    if word not in unique_word_list:
        unique_word_list.append(word)

for unique_word in unique_word_list:
    print(unique_word)