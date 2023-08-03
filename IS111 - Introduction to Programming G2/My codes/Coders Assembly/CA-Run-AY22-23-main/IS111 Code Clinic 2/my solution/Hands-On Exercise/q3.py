def compute_steps(up,down,left,right):
    # YOUR CODE GOES HERE
    total_up = up-down
    total_right = right-left
    distance = (total_up**2 + total_right**2)**(1/2)

    decimal = int(str(distance).split('.')[1])
    if decimal > 0:
        return round(distance, 2)
    return int(distance)