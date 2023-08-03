
age = input("Enter your age in integer: ")

if int(age) <= 12: 
    print("You're a kid!")
elif int(age) > 12 and int(age) <= 30:
    print("You're okay.")

else:
    print("You're too old!")
