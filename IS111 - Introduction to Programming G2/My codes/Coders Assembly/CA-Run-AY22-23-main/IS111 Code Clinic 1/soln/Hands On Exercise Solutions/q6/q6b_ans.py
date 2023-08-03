##
# This question was adapted from SPM Programming Exercise, Roman Numerals
# Author : Stephen Pang Qing Yang
# Created : August 30, 2021
# Last Updated : August 30, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

# Created functions to determine the roman thousandth, hundredth, tenth and oneth values.

def get_thousand_value(thousand_str):
    thousand_list = ['','M','MM','MMM']
    return thousand_list.index(thousand_str) * 1000

def get_hundred_value(hundred_str):
    hundred_list = ['','C','CC','CCC','CD','D','DC','DCC','DCCC','CM']
    return hundred_list.index(hundred_str) * 100

def get_ten_value(ten_str):
    ten_list = ['','X','XX','XXX','XL','L','LX','LXX','LXXX','XC']
    return ten_list.index(ten_str) * 10

def get_one_value(one_str):
    one_list = ['','I','II','III','IV','V','VI','VII','VIII','IX']
    return one_list.index(one_str)

def convert_to_arabic(roman_numeral):
    # Initialize lists
    thousand_start_letters = ['M']
    hundred_start_letters = ['C','D','M']
    ten_start_letters = ['X','L','C']
    one_start_letters = ['I','V','X']

    # Initialize Booleans
    is_thousand = True
    is_hundred = False
    is_ten = False

    # Initialize string
    thousand_str = ""
    hundred_str = ""
    ten_str = ""
    one_str = "" 

    # Going through each roman character
    for ch in roman_numeral: 

        # Forming the thousandth value
        if ch in thousand_start_letters and is_thousand: 
            thousand_str += ch
        
        elif ch not in thousand_start_letters and is_thousand: 
            is_thousand = False 
            is_hundred = True
        
        # Forming the hundredth value
        if ch in hundred_start_letters and is_hundred: 
            hundred_str += ch 
        
        elif ch not in hundred_start_letters and is_hundred:
            is_hundred = False 
            is_ten = True
        
        # Forming the tenth value
        if ch in ten_start_letters and is_ten:
            ten_str += ch
        
        elif ch not in ten_start_letters and is_ten:
            is_ten = False 
        
        # Forming the oneth values
        if not is_thousand and not is_hundred and not is_ten: 
            one_str += ch

    
    # Calculate values
    # print("thousand: " + thousand_str)
    # print("hundred: " + hundred_str) 
    # print("tens: " + ten_str) 
    # print("ones: " + one_str)
    arabic_numeral = get_thousand_value(thousand_str) + get_hundred_value(hundred_str) + get_ten_value(ten_str) + get_one_value(one_str)
        

    return arabic_numeral


print('----Test Case 1----')
result = convert_to_arabic('VI')
print("Expected: 6" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = convert_to_arabic('XVIII')
print("Expected: 18" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = convert_to_arabic('CMIX')
print("Expected: 909" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = convert_to_arabic('MMMCCLIV')
print("Expected: 3254" )
print("Actual:   " + str(result))
print()