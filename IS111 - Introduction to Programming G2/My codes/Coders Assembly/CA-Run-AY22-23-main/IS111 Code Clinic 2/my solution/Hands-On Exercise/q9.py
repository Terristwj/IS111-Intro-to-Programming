def get_nested_list(list_str):
    # YOUR CODE GOES HERE
    # print(list_str)
    # list_str = list_str.replace(' ', '')
    # print(list_str)
    # list_str = list_str[1:-1]

    # list_str = list_str.replace(']', '[')
    # cols = list_str.split('[')[1:-1]

    # print(cols)
    # my_final_list = cols[0][:-1] + cols[-1]
    # my_final_list = my_final_list.split(',')

    # my_final_list_number = []
    # for num_str in my_final_list:
    #     if num_str:
    #         my_final_list_number.append(int(num_str))
    # print(my_final_list)

    # print(list_str)
    list_str = list_str.replace(' ', '')
    # print(list_str)
    list_str = list_str[1:-1]

    first_bracket_index = list_str.find('[')
    for i in range(len(list_str)):
        if list_str[i] == ']':
            last_bracket_index = i
    list_str = list_str[first_bracket_index+1:last_bracket_index]
    # print(list_str)

    final_list = list_str.split(',')
    # print(final_list)
    final_num_list = []
    for element in final_list:
        if element.isnumeric():
            final_num_list.append(int(element))
    return final_num_list