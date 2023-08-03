gender_right = False

gender = "" # Initialize the variable

while not gender_right:
    gender = input("What is your gender? ")
    if gender == 'M' or gender == 'F':
        gender_right = True
    else:
        print("Wrong input, please enter your gender again!")

if gender == "M":
    print("Got it! Thank you Mr.")
else:
    print("Got it! Thank you Ms.")
