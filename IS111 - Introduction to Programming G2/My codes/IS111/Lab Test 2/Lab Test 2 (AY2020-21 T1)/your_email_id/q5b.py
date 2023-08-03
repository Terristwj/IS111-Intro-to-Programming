# Name:
# Email ID:
def get_polynomial(poly_str):
    # Write your code here.
    poly_str_copy = poly_str.replace(" ", "")
    poly_str_copy = poly_str_copy.replace("+", ";")
    poly_str_copy = poly_str_copy.replace("-", ";-")
    nums = poly_str_copy.split(";")

    expo_coef = {}
    for num in nums:
        if "x^" in num:
            cols = num.split("x^")
            coef = int(cols[0])
            expo = int(cols[1])
            if expo not in expo_coef:
                expo_coef[expo] = coef
            else:
                expo_coef[expo] += coef
        elif "x" in num:
            cols = num.split("x")
            coef = int(cols[0])
            if 1 not in expo_coef:
                expo_coef[1] = coef
            else:
                expo_coef[1] += coef
        else:
            coef = int(num)
            if 0 not in expo_coef:
                expo_coef[0] = coef
            else:
                expo_coef[0] += coef
    # print(expo_coef)
    
    coef_list = []
    for i in range(max(expo_coef)+1):
        try:
            if expo_coef[i]:
                coef_list.append(expo_coef[i])
        except:
            coef_list.append(0)

    coef_list.reverse()
    return coef_list

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0
    
    tc_num += 1
    print('-' * 40)
    
    poly_str = '2x - 2x^2 + 3x - 1 + 6x^3'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print("Expected : [6, -2, 5, -1]")
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print() 

    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")    
    
    print()
    
    print("Expected return type of the first element of the list : <class 'int'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")    

    tc_num += 1
    print('-' * 40)
    
    poly_str = '  4x -2x^2 +   3x^5 -   6x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [3, 0, 0, -8, 4, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()  

    tc_num += 1
    print('-' * 40)
    
    poly_str = '3x^2 - 2x - 3x^2'
    print(f"Test Case {tc_num} : get_polynomial('{poly_str}')")
    print('Expected : [-2, 0]')
    result = get_polynomial(poly_str)
    print(f"Actual   : {result}")
    print()      

