def calculate_max_quantity_and_change(unit_price, amount):
    max_quantity = amount // unit_price
    change = amount - max_quantity * unit_price
    max_quantity_and_change = (max_quantity, change)
    return max_quantity_and_change
    