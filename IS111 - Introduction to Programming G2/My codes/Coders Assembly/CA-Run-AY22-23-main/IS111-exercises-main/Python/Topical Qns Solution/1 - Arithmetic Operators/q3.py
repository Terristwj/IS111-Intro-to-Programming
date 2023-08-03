def calculate_bmi(weight,height):
    bmi = weight / ( height ** 2)
    return bmi


weight = float(input("Enter weight (kg): "))
height = float(input("Enter height (cm): "))
height = height / 100
bmi = calculate_bmi(weight,height)

print("Your BMI is " + str(bmi))