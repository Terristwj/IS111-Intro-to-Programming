def binary_to_music(binary_code):
    ## YOUR CODE GOES HERE ##
    my_dict = {'000':'C', '001':'D', '010':'E', '011':'F', '100':'G', '101':'A', '110':'B'}
    my_notes = ""
    while len(binary_code) != 0:
        code = binary_code[0:3]
        binary_code = binary_code[3:]
        my_notes += my_dict[code]
    return my_notes



