import retail_utility

PRICE_1kg = 98.50
PRICE_500gr = 58.50
amount = float(input('How much money do you want to spend? '))

result_tuple = retail_utility.calculate_max_quantity_and_change(PRICE_1kg, amount)
qty_1kg = result_tuple[0]
change = result_tuple[1]

result_tuple = retail_utility.calculate_max_quantity_and_change(PRICE_500gr, change)
qty_500gr = result_tuple[0]
change = result_tuple[1]

num_grams_can_buy = qty_1kg * 1000 + qty_500gr * 500

print('You can buy '+ str(num_grams_can_buy) + ' grams of honey. You have $' + str(change) + ' left as your change.')

