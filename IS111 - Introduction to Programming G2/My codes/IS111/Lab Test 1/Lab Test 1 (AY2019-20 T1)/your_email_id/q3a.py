# Name:
# Email ID:

def calculate_entrance_fees_1(n):

    # These variables are defined for you to use.
    PACKAGE_B = 110
    PACKAGE_C = 200

    # Modify the code below.
    if n % 2:
        if n == 1:
            return PACKAGE_B
        else:
            return PACKAGE_C * (n-1) // 2 + PACKAGE_B
    return PACKAGE_C * n //2
        