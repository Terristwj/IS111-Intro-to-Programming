def reverse_words(sentence):
    new_sentence = ""
    if sentence:
        for word in sentence.split(" "):
            new_sentence += word[::-1] + " "
        new_sentence = new_sentence[0:-1]
    return new_sentence

print(reverse_words("I study at SMU"))
print(reverse_words("Python is a programming language."))
