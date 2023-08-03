# Name:
# Email ID:
from re import L
from symbol import comparison

# Write your code here.
def multiply2(polynomials):
    # print(polynomials)
        my_list = []
        for num in polynomials[0]:
            my_list.append([num,polynomials[1]])
        # print(my_list)

        my_list_2 = []
        for i in range(len(my_list)):
            my_mini_list = []
            for number in my_list[i][1]:
                my_mini_list.append(my_list[i][0]*number)

            for i2 in range(len(my_list)-(i+1)):
                my_mini_list.append(0)

            my_list_2.append(my_mini_list)
        # print(my_list_2)

        my_list_3 = my_list_2[0].copy()
        for i in range(1, len(my_list_2)):
            for i2 in range(len(my_list_2[i]) - 1, -1, -1):
                my_list_3[i2+i] += my_list_2[i][i2]
        
        return my_list_3

def multiply(polynomials):
    if len(polynomials) != 1:
        no_zero = True
        for set in polynomials:
            if set[0] == 0:
                no_zero = not no_zero
        
        if no_zero:
            original_length = len(polynomials)
            my_list = []
            
            while len(polynomials) != 0:
                comparison = []
                if len(polynomials) == original_length:
                    comparison.append(polynomials.pop(0))
                    comparison.append(polynomials.pop(0))
                else:
                    comparison.append(my_list)
                    comparison.append(polynomials.pop(0))
                # print(comparison)
                my_list = multiply2(comparison)
        else:
            my_list = [0]
        return my_list
    else:
        return polynomials[0]

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0
    
    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 2, 3], [5, 6, 7]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print("Expected : [5, 16, 34, 32, 21]")
    result = multiply(polynomials)
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
    
    polynomials = [[1, 2], [3, 4, 5], [6, 7, 8]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print('Expected : [18, 81, 172, 231, 174, 80]')
    print(f"Actual   : {multiply(polynomials)}")
    print() 
    
    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 2], [0], [3, 4, 5], [6, 7, 8]]
    print(f"Test Case {tc_num} : multiply({polynomials})")
    print('Expected : [0]')
    print(f"Actual   : {multiply(polynomials)}")
    print()     

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 2, 3], [5, 6, 7], [8, 9, 0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [40, 173, 416, 562, 456, 189, 0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 1, -1, 1], [2, 0], [8, 9, 0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [16, 34, 2, -2, 18, 0, 0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1], [0]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print('Expected : [0]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    

    tc_num += 1
    print('-' * 40)
    
    polynomials = [[1, 5, 0, 4]]
    print(f'Test Case {tc_num} : multiply({polynomials})')
    print(f'multiply({polynomials})')
    print('Expected : [1, 5, 0, 4]')
    print(f'Actual   : {multiply(polynomials)}')
    print()    