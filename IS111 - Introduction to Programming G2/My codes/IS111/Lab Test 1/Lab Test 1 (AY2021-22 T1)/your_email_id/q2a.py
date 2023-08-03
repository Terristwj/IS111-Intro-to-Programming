# Name:
# Email ID:

def get_right_most_even_digit(number):
    # Replace the code below with your implementation.
    for ch in str(number)[::-1]:
        if not int(ch) % 2:
            return int(ch)
    return None
    