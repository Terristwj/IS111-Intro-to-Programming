# PART A 

def banned_words(banned_string,word_list):
    # Add code here
    my_words = []
    for word in word_list:
        if banned_string in word:
            my_words.append(word)
    return my_words

# PART B
# Add your Program Code Here
sentence = input("Please enter a sentence: ")
banned_string = input("Please enter a banned string: ")
words = sentence.split(' ')

print("The following words are banned!")
for word in words:
    if banned_string in word.lower():
        word = ''.join(i for i in word if i.isalpha())
        print(word)

# Oh no! The dog is getting fat... Oh nevermind, get a cat instead PLEASE! Not thAt Bat, a CAT!

# PART C
def banned_words2(banned_list,word_list):
    # Add code here
    my_word_list = []
    for word in word_list:
        for banned in banned_list:
            if banned in word.lower():
                if word not in my_word_list:
                    my_word_list.append(word)
    return my_word_list

    return None

# PART C Program
# Add your program code here
