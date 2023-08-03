##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

import random

# In this answer, I take 0 as the shuriken had missed, and 1 as the shuriken had hit its target.
def shuriken_hit():
    target_hit = random.randint(0,1)
    if (target_hit == 0):
        print("Your shuriken missed its target")
        return False
    else:
        print("Your shuriken hit its mark!")
        return True


def shoot_shurikens(num):
    no_hits = 0
    for i in range(num):
        is_hit = shuriken_hit()
        if is_hit:
            no_hits += 1
    
    print("You threw " + str(num) + " shurikens.")
    print("You hit the target with a total of " + str(no_hits) + " shurikens.")

print('----Test Case 1----')
result = shoot_shurikens(3)

print('----Test Case 2----')
result = shoot_shurikens(12)
