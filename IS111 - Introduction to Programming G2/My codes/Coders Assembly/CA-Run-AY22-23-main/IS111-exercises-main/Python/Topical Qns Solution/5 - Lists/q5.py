def get_purchase_price(item_list,item_price_list):
    total_price = 0
    for item in item_list:
        for item_price in item_price_list:
            if item_price[0] == item:
                total_price += item_price[1]

    return total_price

# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = get_purchase_price(['Cabbage'],[('Cabbage',2.50),('Milk',5.50)])
print("Expected: 2.5" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_purchase_price(['Cabbage','Milk'],[('Cabbage',2.50),('Milk',5.50)])
print("Expected: 8.0" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_purchase_price(['Cabbage','Milk','Coffee','Milk'],[('Cabbage',2.50),('Milk',5.50),('Coffee',8.10)])
print("Expected: 21.6" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_purchase_price([],[('Cabbage',2.50),('Milk',5.50)])
print("Expected: 0" )
print("Actual:   " + str(result))
print()