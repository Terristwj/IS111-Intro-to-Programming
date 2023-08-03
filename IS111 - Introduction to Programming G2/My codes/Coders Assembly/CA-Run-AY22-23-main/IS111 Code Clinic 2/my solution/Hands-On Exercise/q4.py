def get_alpha_num(string):
    # YOUR CODE GOES HERE
    print(string)

    my_string = ''
    my_nums = []

    for i in range(len(string)):
        if string[i].isalpha():
            my_string += string[i]
        if string[i].isnumeric() or string[i] == '-':
            my_nums.append(string[i])

    my_calculations = ''
    print(my_string, my_nums)
    while len(my_nums) != 0:
        if my_nums[0] == '-':
            if my_nums[1].isnumeric():
                my_calculations += my_nums[0] + my_nums[1]
                my_nums.pop(0)
                my_nums.pop(0)
            else:
                my_nums.pop(0)
        else:
            my_calculations += '+' + my_nums[0]
            my_nums.pop(0)

    final_num = 0
    for i in range(len(my_calculations)):
        if my_calculations[i] == '+':
            final_num += int(my_calculations[i+1])
        elif my_calculations[i] == '-':
            final_num -= int(my_calculations[i+1])
    return (my_string, final_num)




    