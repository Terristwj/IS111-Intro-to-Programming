##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

import q2a_ans # should be q2a , the exact name of the file in part A.


def make_purchase(item_list,shop_list,current_money):
    total_cost = q2a_ans.get_total_cost(item_list,shop_list)
    if total_cost > current_money:
        return (False, current_money)
    else:
        new_money = current_money - total_cost
        return (True, new_money)



shop = [('Kunai',100),
        ('Four-edged Shuriken',50),
        ('Senbon',20),
        ('Machete',350),
        ('Super Heaven Fan',1200),
        ('Iron Knuckles',800),
        ('Jonin Sword',1500),
        ('Hokage Mace',3200)
        ]
# DO NOT MODIFY THE CODE BELOW:

print('----Test Case 1----')
result = make_purchase(['Kunai','Machete'],shop, 300)
print("Expected: (False, 300)" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = make_purchase(['Iron Knuckles'],shop,1500)
print("Expected: (True, 700)" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = make_purchase([],shop,0)
print("Expected: (True, 0)" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = make_purchase(['Super Heaven Fan','Jonin Sword','Senbon','Senbon','Senbon','Four-edged Shuriken'],shop,3200)
print("Expected: (True, 390)" )
print("Actual:   " + str(result))
print()