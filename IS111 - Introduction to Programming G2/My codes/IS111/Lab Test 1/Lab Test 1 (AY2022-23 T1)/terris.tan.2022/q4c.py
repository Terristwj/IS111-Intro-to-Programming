# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg

def find_overlap_size(rect_1, rect_2):
    # Replace the code below with your implementation.
    rect_1_cords = []
    rect_2_cords = []

    # To save the cords of rect_1 into a list.
    for i in range(rect_1[3]):
        for j in range(rect_1[4]):
            rect_1_cords.append([rect_1[1] + i, rect_1[2] + j])
            
    # To save the cords of rect_2 into a list.
    for i in range(rect_2[3]):
        for j in range(rect_2[4]):
            rect_2_cords.append([rect_2[1] + i, rect_2[2] + j])

    # Count number of same cords
    counter = 0
    for cords in rect_1_cords:
        if cords in rect_2_cords:
            counter += 1

    return counter