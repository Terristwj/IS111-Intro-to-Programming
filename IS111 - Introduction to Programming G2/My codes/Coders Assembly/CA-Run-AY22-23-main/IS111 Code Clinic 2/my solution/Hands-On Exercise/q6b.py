def binary_to_music2(binary_code):
    ## YOUR CODE GOES HERE ##
    my_dict = {'000':'C', '001':'D', '010':'E', '011':'F', '100':'G', '101':'A', '110':'B'}
    my_notes = ""
    if len(binary_code) % 3 == 0:
        while len(binary_code) != 0:
            code = binary_code[0:3]
            binary_code = binary_code[3:]
            my_notes += my_dict[code]
    else:
        while len(binary_code) != 0:
            code = binary_code[0:3]
            if code in my_dict:
                binary_code = binary_code[3:]
                my_notes += my_dict[code]
            else:
                binary_code = binary_code[1:]
    return my_notes