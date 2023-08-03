# Name:
# Email ID:

def check_sum(n1, n2, n3):
    # Modify the code below.
    is_valid = False
    if n1 == n2+n3:
        is_valid = True
    if n2 == n1+n3:
        is_valid = True
    if n3 == n1+n2:
        is_valid = True
    return is_valid
    