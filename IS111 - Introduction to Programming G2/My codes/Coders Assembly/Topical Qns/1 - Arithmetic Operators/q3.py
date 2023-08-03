def calculate_bmi(weight,height):
    # YOUR CODE GOES HERE
    return weight/(height/100)**2


# YOUR CODE GOES HERE
weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))

bmi = calculate_bmi(weight, height)
print("Your BMI is", bmi)