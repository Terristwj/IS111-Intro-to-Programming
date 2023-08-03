# Name:
# Email ID:
def multiply(polynomials):

    # Write your code here.
    count = len(polynomials)

    highest_pow = 0
    for poly in polynomials:
        highest_pow += len(poly)-1
        if poly == [0]:
            return [0]

    highest_pow += 1

    while len(polynomials) != 1:
        copy_poly = []
        for i in range(1,len(polynomials),2):
            power = len(polynomials[i]) + len(polynomials[i-1])
            result = []
            for p in range(power):
                result.append(0)
            for p1 in range(len(polynomials[i])):
                for p2 in range(len(polynomials[i-1])):
                    value = polynomials[i][p1] * polynomials[i-1][p2]
                    pow_1 = len(polynomials[i]) - p1
                    pow_2 = len(polynomials[i-1]) - p2
                    result[len(result) - pow_1 - pow_2] += value
            copy_poly.append(result)
        if len(polynomials) % 2 != 0:
            copy_poly.append(polynomials[len(polynomials)-1])
        polynomials = copy_poly[:]

    for i in range(len(polynomials[0]) - highest_pow):
        polynomials[0].pop()

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