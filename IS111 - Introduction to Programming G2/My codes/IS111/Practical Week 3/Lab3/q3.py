## Q3 PART 1
# This function is for you to implement!
def calculate_salary(monthly_sales):
    
    # This variable is defined for you to use.
    BASE_SALARY = 2000.0
    
    # ################################################################################
    # Modify the code below to return the right amount of salary.
    salary = BASE_SALARY
    if monthly_sales < 10000:
        salary += monthly_sales * 0.05
    elif monthly_sales < 15000:
        salary += monthly_sales * 0.1
    elif monthly_sales < 18000:
        salary += monthly_sales * 0.15
    else:
        salary += monthly_sales * 0.18
    
    return salary
    # ################################################################################

## Q3 PART 2
# Write your code below
sales = float(input("Enter monthly sales amount($): "))
pay = calculate_salary(sales)
print("The monthly pay for the salesperson is $" + str(pay))

