## Q2 PART 1
# These variables are defined for you to use.
MEMBER_DISCOUNT_RATE = 0.10
SALE_ITEM_DISCOUNT_RATE = 0.05

# This function is for you to implement!
def calculate_price(orig_price, is_member, is_on_sale):
    
    # ################################################################################
    # Modify the code below to return the correct discounted price.
    if is_member and is_on_sale:
        return orig_price * (1 - MEMBER_DISCOUNT_RATE - SALE_ITEM_DISCOUNT_RATE)
    if is_member:
        return orig_price * (1 - MEMBER_DISCOUNT_RATE)
    if is_on_sale:
        return orig_price * (1 - SALE_ITEM_DISCOUNT_RATE)
    
    return orig_price  
    # ################################################################################

## Q2 PART 2
# Write your code below to prompt the user for the following information: 
# (1) The original price of the item. 
# (2) Whether the user is a member or not. 
# (3) Whether the item is on sale or not.:
ori_price = float(input("What's the original price of them item: $"))
is_member = input("Are you a member [yes|no]? ")
is_on_sale = input("Is the item on sale [yes|no]? ")

final_price = calculate_price(ori_price, is_member == "yes", is_on_sale == "yes")
print("The final price of the item is $" + str(final_price))




