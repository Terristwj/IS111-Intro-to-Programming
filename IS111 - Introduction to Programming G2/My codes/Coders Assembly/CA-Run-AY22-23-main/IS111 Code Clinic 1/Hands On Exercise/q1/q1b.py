##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

import random

def shoot_shurikens(num):
    # YOUR CODE GOES HERE
    num_hits = 0
    for i in range(num):
        if random.randint(0,1):
            num_hits += 1
            print("Your shuriken hit its mark!")
        else:
            print("Your shuriken missed its target")
    print("You threw", num, "shurikens.")
    print("You hit the target with a total of", num_hits, "shurikens")
    pass


# DO NOT MODIFY THE CODE BELOW:
print('----Test Case 1----')
result = shoot_shurikens(3)

print('----Test Case 2----')
result = shoot_shurikens(12)
