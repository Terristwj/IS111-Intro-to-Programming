def get_hypotenuse(length,height):
    return (length ** 2 + height ** 2) ** (1/2)


length = float(input("Enter length of right-angled triangle: "))
height = float(input("Enter height of right-angled triangle: "))

hypotenuse = get_hypotenuse(length,height)
print("The length of the hypotenuse is " + str(hypotenuse))
