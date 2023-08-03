#
# Name: 
# Email ID: 
#
def get_prices_in_range(price_list, low, high):
    # Modify the code below    
    my_prices = []
    for price in price_list:
        if price >= low and price<= high:
            my_prices.append(price)
    return my_prices