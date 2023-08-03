PI = 3.14 # DO NOT MODIFY THIS GIVEN VALUE


def calculate_cone_area(radius):
    # YOUR CODE GOES HERE
    return PI*radius**2

def calculate_cone_circumference(radius,height):
    # YOUR CODE GOES HERE
    return 1/3*PI*radius**2*height


# YOUR CODE GOES HERE
radius = float(input("Enter radius of cone: "))
height = float(input("Enter height of cone: "))

curved_area = calculate_cone_area(radius)
print("The curved area of the cone is", curved_area)
volume = calculate_cone_circumference(radius, height)
print("The volume of the cone is", volume)