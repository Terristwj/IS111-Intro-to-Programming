# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg

from q4a import is_overlapping
def find_overlapping_pairs(rect_list):
    # # print(rect_list)
    # overlap_list = []
    # for rect1 in rect_list:
    #     for rect2 in rect_list:
    #         if rect1 != rect2:
    #             if is_overlapping(rect1, rect2):
    #                 if overlap_list:
    #                     in_list = False
    #                     for item in overlap_list:
    #                         # print(rect1[0], rect2[0])
    #                         # print(item)
    #                         if (rect1[0] == item[0] and rect2[0] == item[1]) or (rect2[0] == item[0] and rect1[0] == item[1]):
    #                             # print("append")
    #                             # print(rect1[0], rect2[0])
    #                             # print(item)
    #                             in_list = True
    #                         # if (rect1[0] != item[0] and rect2[0] != item[1]) or (rect2[0] != item[0] and rect1[0] != item[1]):
    #                             # overlap_list.append((rect1[0], rect2[0]))
    #                     if not in_list:
    #                         overlap_list.append((rect1[0], rect2[0]))
    #                 else:
    #                     overlap_list.append((rect1[0], rect2[0]))
    # # Replace the code below with your implementation.

    overlap_list = []
    for rect_1 in rect_list:
        for rect_2 in rect_list:
            if rect_1 != rect_2 and is_overlapping(rect_1, rect_2):
                if (rect_1[0], rect_2[0]) not in overlap_list and (rect_2[0], rect_1[0]) not in overlap_list:
                    overlap_list.append((rect_1[0], rect_2[0]))

    return overlap_list


# from q4a import is_overlapping

########################################
# Solution
########################################
# def find_overlapping_pairs(mylist): 
#     results = [] 
#     for i in mylist: 
#         for j in mylist: 
#             if i != j and is_overlapping(i,j):
#                 if (i[0],j[0]) not in results and (j[0],i[0]) not in results: 
#                     results.append((i[0],j[0]))

#     return results 


########################################
# Solution with strategic filtering
# Computation Thinking concept
# Filter out before comparing
########################################
# def find_overlapping_pairs(mylist): 
#     results = [] 
#     for i in range(len(mylist)): 
#         for j in range(i+1, len(mylist)): 
#             if is_overlapping(mylist[i], mylist[j]): 
#                 results.append((mylist[i][0],mylist[j][0]))
#     return results