# Name:
# Email ID:

def get_number_of_long_strings(str_list, n):
    # Modify the code below.
    num_of_bigger = 0
    for string in str_list:
        if len(string) > n:
            num_of_bigger += 1
    return num_of_bigger