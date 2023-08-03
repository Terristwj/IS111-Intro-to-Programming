# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg

def is_overlapping(rect_1, rect_2):
    # # Replace the code below with your implementation.

    # # min[x,y] , max[x,y]
    # # btm_left, top_left, top_right, btm_right

    # rect_1_cords =  [[rect_1[1], rect_1[2]],    [rect_1[1], rect_1[2]+rect_1[4]],   [rect_1[1]+rect_1[3], rect_1[2]+rect_1[4]], [rect_1[1]+rect_1[3], rect_1[2]]]
    # rect_2_cords = [[rect_2[1], rect_2[2]],    [rect_2[1], rect_2[2]+rect_2[4]],   [rect_2[1]+rect_2[3], rect_2[2]+rect_2[4]], [rect_2[1]+rect_2[3], rect_2[2]]]


    # for i in range(len(rect_1_cords)):
    #     # print(i, rect_1_cords[i])
    #     # print(i, rect_2_cords[0], rect_2_cords[2])
    #     if rect_1_cords[i][0] > rect_2_cords[0][0] and rect_1_cords[i][1] > rect_2_cords[0][1]:
    #         if rect_1_cords[i][0] < rect_2_cords[2][0] and rect_1_cords[i][1] < rect_2_cords[2][1]:
    #             # print(rect_1_cords[i], rect_2_cords[2])
    #             return True
    #     # if rect_1_cords[i][0] >= rect_2_cords[0][0] and rect_1_cords[i][1] >= rect_2_cords[0][1]:
    #     #     if rect_1_cords[i][0] == rect_2_cords[1][0] and rect_1_cords[i][1] < rect_2_cords[1][1]:
    #     #         return True
    #     # if rect_1_cords[i][0] < rect_2_cords[0][0] and rect_1_cords[i][1] < rect_2_cords[0][1]:
    #     #     if rect_1_cords[i][0] > rect_2_cords[1][0] and rect_1_cords[i][1] > rect_2_cords[1][1]:
    #     #         return True

    # # print(rect_1_cords)
    # # print(rect_2_cords)

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

    # Check for same cords
    for cords in rect_1_cords:
        if cords in rect_2_cords:
            return True

    return False