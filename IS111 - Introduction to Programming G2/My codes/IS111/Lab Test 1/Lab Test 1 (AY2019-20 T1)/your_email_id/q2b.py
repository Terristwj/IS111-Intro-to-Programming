# Name:
# Email ID:

def add_even_numbers(str_list):
    # Modify the code below.
    sum = 0
    string = ""
    if str_list:
        for list in str_list:
            string += "|" + list
        string = string[1:]

        for num in string.split("|"):
            if int(num) % 2 == 0:
                sum += int(num)
    return sum