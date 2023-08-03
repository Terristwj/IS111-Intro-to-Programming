def calculate_rectangle_area(length, breadth):
    # YOUR CODE GOES HERE
    return length * breath


def calculate_rectangle_perimeter(length, breadth):
    # YOUR CODE GOES HERE
    return (length+breath)*2


# YOUR CODE GOES HERE
length = float(input("Enter rectangle length: "))
breath = float(input("Enter rectangle breath: "))

area = calculate_rectangle_area(length, breath)
print("The area of the rectangle is", area)
perimeter = calculate_rectangle_perimeter(length, breath)
print("The area of the rectangle is", perimeter)