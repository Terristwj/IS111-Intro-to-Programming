##
# Author : Stephen Pang Qing Yang
# Created : August 19, 2021
# Last Updated : August 19, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def get_total_cost(purchase_list,shop_list):
    total_cost = 0
    for purchase in purchase_list:
        for shop_item_tup in shop_list:
            if purchase == shop_item_tup[0]:
                total_cost += shop_item_tup[1]
                

    return total_cost


shop = [('Kunai',100),
        ('Four-edged Shuriken',50),
        ('Senbon',20),
        ('Machete',350),
        ('Super Heaven Fan',1200),
        ('Iron Knuckles',800),
        ('Jonin Sword',1500),
        ('Hokage Mace',3200)
        ]

if __name__ == "__main__":
    print('----Test Case 1----')
    result = get_total_cost(['Kunai','Machete'],shop)
    print("Expected: 450" )
    print("Actual:   " + str(result))
    print()
    print('----Test Case 2----')
    result = get_total_cost(['Iron Knuckles','Iron Knuckles'],shop)
    print("Expected: 1600" )
    print("Actual:   " + str(result))
    print()
    print('----Test Case 3----')
    result = get_total_cost([],shop)
    print("Expected: 0" )
    print("Actual:   " + str(result))
    print()
    print('----Test Case 4----')
    result = get_total_cost(['Super Heaven Fan','Jonin Sword','Senbon','Senbon','Senbon','Four-edged Shuriken'],shop)
    print("Expected: 2810" )
    print("Actual:   " + str(result))
    print()