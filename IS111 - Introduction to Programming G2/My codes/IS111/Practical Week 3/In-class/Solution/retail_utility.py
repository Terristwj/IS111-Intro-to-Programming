def calculate_max_quantity_and_change(unit_price, amount):
    qty = int(amount // unit_price)
    price_to_pay = unit_price * qty
    change = amount - price_to_pay
    # You can also use the following code:
    # change = amount % unit_price
    return (qty, change)