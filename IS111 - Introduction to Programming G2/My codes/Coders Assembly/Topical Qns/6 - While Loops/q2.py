# YOUR CODE GOES HERE
num = int(input("Enter a number to guess: "))
guess = int(input("Now forget all about that number, and try to guess it: "))

while(guess != num):
    if guess < num:
        print("Your guess is too low.")
    else:
        print("Your guess is too high.")
    guess = int(input("Now forget all about that number, and try to guess it: "))

print("You got it!")