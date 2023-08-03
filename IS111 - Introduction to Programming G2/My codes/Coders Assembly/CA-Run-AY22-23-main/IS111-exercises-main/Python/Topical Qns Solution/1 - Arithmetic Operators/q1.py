def calculate_rectangle_area(length,breadth):
    return length * breadth

def calculate_rectangle_perimeter(length,breadth):
    return length * 2 + breadth * 2


length = float(input("Enter rectangle length: "))
breadth = float(input("Enter rectangle breath: "))

area = calculate_rectangle_area(length,breadth)
perimeter = calculate_rectangle_perimeter(length,breadth)

print("The area of the rectangle is " + str(area))
print("The perimeter of the rectangle is " + str(perimeter))