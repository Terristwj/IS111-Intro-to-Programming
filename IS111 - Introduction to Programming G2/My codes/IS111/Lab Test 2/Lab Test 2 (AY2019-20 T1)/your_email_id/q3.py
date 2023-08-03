# Name:
# Email ID:

def compute_total_price(price_dict, item_list):
    # Modify the code below.
    total_price = 0.0

    for item in item_list:
        name = item[0]
        qty = item[1]

        if name in price_dict:
            total_price += price_dict[name] * qty
        else:
            total_price += 0.0
    return total_price