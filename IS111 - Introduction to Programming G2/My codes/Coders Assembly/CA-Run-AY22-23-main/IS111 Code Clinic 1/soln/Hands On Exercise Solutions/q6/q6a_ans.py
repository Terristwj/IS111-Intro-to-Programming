##
# This question was adapted from SPM Programming Exercise, Roman Numerals
# Author : Stephen Pang Qing Yang
# Created : August 30, 2021
# Last Updated : August 30, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

# Created functions to determine the roman thousandth, hundredth, tenth and oneth values.

def get_thousand(thousand_int):
    thousand_list = ['','M','MM','MMM']
    return thousand_list[thousand_int]

def get_hundred(hundred_int):
    hundred_list = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    return hundred_list[hundred_int]

def get_ten(ten_int):
    ten_list = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    return ten_list[ten_int]

def get_one(one_int):
    one_list = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    return one_list[one_int]

def convert_to_roman(num):
    num_str = str(num)
    roman_num_str = ""
    # Check if the number is in the thousands
    if len(num_str) == 4:
        roman_num_str += get_thousand(int(num_str[0]))
        roman_num_str += get_hundred(int(num_str[1]))
        roman_num_str += get_ten(int(num_str[2]))
        roman_num_str += get_one(int(num_str[3]))
    
    # Check if number is in the hundreds
    elif len(num_str) == 3:
        roman_num_str += get_hundred(int(num_str[0]))
        roman_num_str += get_ten(int(num_str[1]))
        roman_num_str += get_one(int(num_str[2]))

    # Check if number is in the tens
    elif len(num_str) == 2:
        roman_num_str += get_ten(int(num_str[0]))
        roman_num_str += get_one(int(num_str[1]))
    
    # Number must be in the ones
    else:
        roman_num_str += get_one(int(num_str))

    return roman_num_str


print('----Test Case 1----')
result = convert_to_roman(5)
print("Expected: V" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = convert_to_roman(46)
print("Expected: XLVI" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = convert_to_roman(102)
print("Expected: CII" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = convert_to_roman(2097)
print("Expected: MMXCVII" )
print("Actual:   " + str(result))
print()