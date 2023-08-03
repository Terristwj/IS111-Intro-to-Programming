def count_a(text):
    return count(text, "a")

def count_an(text):
    return count(text, "an")

def count(text, comparison):
    counter = 0
    for letter in text.split():
        if letter == comparison:
            counter += 1
    return counter