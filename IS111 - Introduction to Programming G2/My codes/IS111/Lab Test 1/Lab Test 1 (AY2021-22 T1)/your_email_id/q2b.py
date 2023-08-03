# Name:
# Email ID:

def get_all_third_digits(str_list):
    # Replace the code below with your implementation.
    num_list = []
    for str in str_list:
        digit_count = 0
        for ch in str:
            if ch.isnumeric():
                digit_count += 1
                if digit_count == 3:
                    num_list.append(int(ch))
            
    return num_list