def get_purchase_price(item_list,item_price_list):
    # YOUR CODE GOES HERE

    return None

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