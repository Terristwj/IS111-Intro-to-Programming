##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

def decode_calculate(string):
    # YOUR CODE GOES HERE
    no_int = ""
    dash_tracker = ""
    total_sum = 0
    for ch in string:
        if not ch.isnumeric() and ch != "-":
            if "-" in dash_tracker:
                no_int += dash_tracker
                dash_tracker = ""
            no_int += ch
        else:
            if ch == "-":
                dash_tracker += "-"
            else:
                if ch.isnumeric():
                    if "-" in dash_tracker:
                        total_sum -= int(ch)
                    else:
                        total_sum += int(ch)
                    dash_tracker = dash_tracker[0:-1]
                    no_int += dash_tracker
                else:
                    no_int += dash_tracker
                dash_tracker = ""
    return (no_int, total_sum)

# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = decode_calculate('aS-3o5AkE2b05#6')
print("Expected: ('aSoAkEb#', 15)" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = decode_calculate('@kaNsaShiRo')
print("Expected: ('@kaNsaShiRo', 0)" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = decode_calculate('-25010245-35-92')
print("Expected: ('', 10)" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = decode_calculate('s-5A-N--8cHa2---Na')
print("Expected: ('sA-N-cHa---Na', -11)" )
print("Actual:   " + str(result))
print()