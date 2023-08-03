##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def decode_calculate(string):
    value = 0
    new_string = ""
    is_minus = False

    for ch in string:
        if not ch.isdigit():
            if is_minus:
                new_string += '-'
                is_minus = False
            if ch == "-":
                is_minus = True
            else:
                new_string += ch
        
        else:
            if is_minus:
                value -= int(ch)
                is_minus = False
            else:
                value += int(ch)

    return (new_string, value)

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