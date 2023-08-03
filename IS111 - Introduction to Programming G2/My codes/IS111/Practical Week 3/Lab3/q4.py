## Q4
# PART 1
# The following function is for you to implement.
def get_ticket_info(age):
    
    # Modify the code below to return the right value
    price = 33
    is_discount = False
    
    if age <= 12 or age >= 60:
        is_discount = True
        if age >= 60:
            price = 15
        if age <= 12:
            if age >= 3:
                price = 22
            else:
                price = 0
    
    return (price, is_discount)
    
    
# ################################################################################
# The code below is to test your implementation of the function above. 
# DO NOT MODIFY THE CODE BELOW!

# The following line of code should display (33, False)
#print(get_ticket_info(40))

# The following line of code should display (22, True)
#print(get_ticket_info(10))


# PART 2
# Write your code below to prompt the user for age
# and print the expected output
age = int(input("How old are you? "))
if age <= 12 or age >= 60:
    print("Congratulations! You qualify for a discount.")
ticket_info = get_ticket_info(age)
print("You need to pay $" + str(ticket_info[0]))

