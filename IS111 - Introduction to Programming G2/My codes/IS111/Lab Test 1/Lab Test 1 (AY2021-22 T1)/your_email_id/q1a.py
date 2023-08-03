# Name:
# Email ID:

def get_area_difference(width1, length1, width2, length2):
    # Replace the code below with your implementation.
    area1 = width1 * length1
    area2 = width2 * length2

    if area1 > area2:
        return area1 - area2
    else:
        return area2 - area1