##
# This question was adapted from SPM Programming Exercise, Roman Numerals
# Author : Stephen Pang Qing Yang
# Created : August 30, 2021
# Last Updated : August 30, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

# DO NOT MODIFY THIS variable
age_list = [('Molly',25), ('Jett',13), ('Sage', 21), ('Ashley', 40), ('Sean', 31), ('Michelle',21)]


# YOUR CODE GOES HERE
file = 'q2.text'
young = 30
with open(file, 'w') as f:
    for person in age_list:
        if person[1] <= young:
            f.write(f"{person[0]} : {person[1]} -> YOUNG\n")
        else:
            f.write(f"{person[0]} : {person[1]} -> OLD\n")