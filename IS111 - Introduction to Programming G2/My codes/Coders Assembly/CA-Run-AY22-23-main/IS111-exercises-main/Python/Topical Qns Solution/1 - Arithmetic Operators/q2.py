PI = 3.14 # DO NOT MODIFY THIS GIVEN VALUE


def calculate_curved_cone_area(diameter,height):
    radius = diameter / 2
    return PI * radius ** 2

def calculate_cone_volume(diameter,height):
    radius = diameter / 2
    return 1/3 * PI * radius ** 2 * height


radius = float(input("Enter radius of cone: "))
diameter = radius * 2

height = float(input("Enter height of cone: "))

area = calculate_curved_cone_area(diameter,height)
volume = calculate_cone_volume(diameter,height)

print("The curved area of the cone is " + str(area))
print("The volume of the cone is " + str(volume))