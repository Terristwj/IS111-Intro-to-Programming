
num = int(input("Enter a number to guess: "))

guessed_number = ""

guessed_number = int(input("Now forget all about that number, and try to guess it: "))

while guessed_number != num:
    if guessed_number < num:
        print("Your guess was too low.")
    elif guessed_number > num: 
        print("Your guess was too high.")
    guessed_number = int(input("Enter your guess again: "))

print("You got it!")