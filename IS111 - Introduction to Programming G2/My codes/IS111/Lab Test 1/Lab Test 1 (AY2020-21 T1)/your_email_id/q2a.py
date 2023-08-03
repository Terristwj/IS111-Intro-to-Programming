# Name:
# Email ID:

def get_sum_of_digits(my_str):
    # Replace the code below with your implementation.
    if my_str:
        num = 0
        for ch in my_str:
            if ch.isnumeric():
                num += int(ch)
        return num
    return 0