def get_hypotenuse(length,height):
    # YOUR CODE GOES HERE
    return (length**2+height**2)**0.5


# YOUR CODE GOES HERE
length = float(input("Enter length of right_angled triangle: "))
height = float(input("Enter height of right_angled triangle: "))

hype_length = get_hypotenuse(length, height)
print("The length of the hypotenuse is", hype_length)