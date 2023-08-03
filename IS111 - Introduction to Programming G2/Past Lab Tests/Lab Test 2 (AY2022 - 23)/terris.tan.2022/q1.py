# Name:
# Email ID:

def check_record(record):
    # Replace the code below with your implementation.
    my_string = record[0]
    first_num = record[1]
    second_num = record[2]

    if first_num == len(my_string) and second_num > first_num:
        return True
    return False
