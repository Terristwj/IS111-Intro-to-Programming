# Name:
# Email ID:

import q3a

def calculate_entrance_fees_2(m, n):
    
    # These variables are defined for you to use.
    ADULT_TICKET = 75   # 1A
    CHILD_TICKET = 50   # 1C
    
    PACKAGE_A = 140     # 2A
    PACKAGE_B = 110     # 1A+1C
    PACKAGE_C = 200     # 2A+2C
    
    # Modify the code below.
    sum = 0
    min_num = min(m, n)

    m -= min_num
    n -= min_num
    if min_num % 2 :
        if min_num == 1:
            sum += PACKAGE_B
        else:
            sum += PACKAGE_C * (min_num-1) // 2 + PACKAGE_B
    else:
        sum += PACKAGE_C * min_num //2

    if m == 0:
        sum += CHILD_TICKET * n
    else:
        if m % 2:
            if m == 1:
                sum += ADULT_TICKET
            else:
                sum += PACKAGE_A * (m-1) // 2 + ADULT_TICKET
        else:
            sum += PACKAGE_A * m //2

    return sum