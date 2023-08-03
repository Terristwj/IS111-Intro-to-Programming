import retail_utility

price_gram_of_small_honey_jar = (58.5, 500)
price_gram_of_big_honey_jar = (98.50, 1000)

amount = float(input("How much money do you want to spend? $"))
can_buy = False
total_change = 0
max_grams = 0

# When amount is too low
if amount < price_gram_of_small_honey_jar[0]:
    print("You cannot buy anything with that amount.")
# When amount is enough
else:
    if amount >= price_gram_of_big_honey_jar[0]:
        max_quantity_and_change = retail_utility.calculate_max_quantity_and_change(price_gram_of_big_honey_jar[0], amount)
        total_change = max_quantity_and_change[1]
        max_grams = max_quantity_and_change[0] * price_gram_of_big_honey_jar[1]
        can_buy = True
        amount -= max_quantity_and_change[0] * price_gram_of_big_honey_jar[0]
    
    if amount >= price_gram_of_small_honey_jar[0]:
        max_quantity_and_change = retail_utility.calculate_max_quantity_and_change(price_gram_of_small_honey_jar[0], amount)
        total_change = max_quantity_and_change[1]
        max_grams += max_quantity_and_change[0] * price_gram_of_small_honey_jar[1]
        can_buy = True

    if can_buy:
        print("You can buy", max_grams , "grams of honey. You have $" + str(round(total_change, 1)) + " left as your change")
    else: # amount < price_gram_of_small_honey_jar[0]:
        print("You cannot buy anything with that amount.")