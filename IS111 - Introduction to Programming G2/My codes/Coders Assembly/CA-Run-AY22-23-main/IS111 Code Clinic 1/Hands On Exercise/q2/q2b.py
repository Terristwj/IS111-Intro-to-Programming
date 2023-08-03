##
# Author : Stephen Pang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang
##

# YOU NEED TO WRITE SOMETHING OVER HERE
from q2a import get_total_cost

def make_purchase(item_list,shop_list,current_money):
    # YOUR CODE GOES HERE
    total_cost = get_total_cost(item_list, shop_list)
    if current_money > total_cost:
        can_afford = True
        money_left = current_money - total_cost
    else:
        can_afford = False
        money_left = current_money

    return [can_afford, money_left]


# DO NOT MODIFY THE CODE BELOW:
shop = [('Kunai',100),
        ('Four-edged Shuriken',50),
        ('Senbon',20),
        ('Machete',350),
        ('Super Heaven Fan',1200),
        ('Iron Knuckles',800),
        ('Jonin Sword',1500),
        ('Hokage Mace',3200)
        ]

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