def surround(field_list):
    # YOUR CODE GOES HERE
    for list in field_list:
        print(list)
        
    y_cord = 0
    x_cord = 0
    for y in range(len(field_list)):
        for x in range(len(field_list[y])):
            if field_list[y][x] == "X":
                y_cord = y
                x_cord = x

    # print(y_cord, x_cord)

    
    # if (y_cord-1 > 0 and y_cord+1 < len(field_list)) and (x_cord-1 > 0 and x_cord+1 < len(field_list[0])):
    if y_cord-1 > 0:
        field_list[y_cord-1][x_cord] = "O"
    if x_cord+1 < len(field_list[0]):
        field_list[y_cord][x_cord+1] = "O"
    if y_cord+1 < len(field_list):
        field_list[y_cord+1][x_cord] = "O"
    if x_cord-1 > 0:
        field_list[y_cord][x_cord-1] = "O"

    # for list in field_list:
    #     print(list)

    return field_list