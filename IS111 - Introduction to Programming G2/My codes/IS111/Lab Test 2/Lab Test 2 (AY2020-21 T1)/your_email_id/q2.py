# Name:
# Email ID:
def get_hi_lo(products):
    # Write your code here.
    hi_lo = (None, None)
    if products:
        if len(products) != 1:
            highest_prod = (products[0][0], products[0][1])
            smallest_prod = (products[0][0], products[0][1])

            for i in range(1, len(products)):
                if products[i][1] > highest_prod[1]:
                    highest_prod = (products[i][0], products[i][1])
                elif products[i][1] < smallest_prod[1]:
                    smallest_prod = (products[i][0], products[i][1])
            hi_lo = (highest_prod[0], smallest_prod[0])
        else:
            hi_lo = (products[0][0], products[0][0])
    return hi_lo

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    products = [('apple', 100), ('orange', 200), ('pear', 300)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('pear', 'apple')")
    print(f"Actual   : {result}")
    print()
    
    print("Expected return type : <class 'tuple'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the tuple : <class 'str'>")
    print("Actual return type of the first element of the tuple   : ", end="")
    if (isinstance(result, tuple)):
        print(type(result[0]))
    else:
        print("N/A")

    tc_num += 1
    print('-' * 40)
    
    products = [('apple',100),('orange',250),('pear',200),('banana',150)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('orange', 'apple')")
    print(f"Actual   : {result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    products = [('apple', 100)]
    print(f"Test Case {tc_num} : get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : ('apple', 'apple')")
    print(f"Actual   : {result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    products = []
    print(f"Test Case {tc_num}:get_hi_lo({products})")
    result = get_hi_lo(products)
    print("Expected : (None, None)")
    print(f"Actual   : {result}")
    print()
