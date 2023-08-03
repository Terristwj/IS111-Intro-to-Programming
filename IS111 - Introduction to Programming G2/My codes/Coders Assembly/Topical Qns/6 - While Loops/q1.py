# YOUR CODE GOES HERE
gender = input("What is your gender? ")
while gender != 'M' and gender != 'F':
    print("Wrong input, please enter your gender again!")
    gender = input("What is your gender? ")

print("Got it! Thank you", end=" ")

if gender == 'M':
    print("Mr.")
else:
    print("Ms.")