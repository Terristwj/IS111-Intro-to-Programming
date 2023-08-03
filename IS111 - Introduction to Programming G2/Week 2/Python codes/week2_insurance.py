import week2_utility as utility

age = int(input("What's your age? "))
gender = input("What's your gender [M|F]? ")

print("Your premium is $" + str(utility.get_insurance_premium(age, gender)))