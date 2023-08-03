# Name:
# Email ID:
polynomials = [[1, 2, 3], [4]]


def multiply(polynomials):
    ## [coefficient, power]

    polynomials_edited = []
    for poly in polynomials: 
        length = len(poly) ## highest power = length - 1
        poly_edited = []
        for i in range(len(poly)): 
            poly_edited.append([poly[i], length - 1 - i]) 
        polynomials_edited.append(poly_edited)
    
    # print("1: ", polynomials_edited)

    ## multiply the first two polynomials, remove the first two polynomials from 
    ## polynomials_edited, add the result to the back of polynomials_edited 

    while len(polynomials_edited) > 1: 
        resulting_poly = [] 
        for poly0 in polynomials_edited[0]: 
            for poly1 in polynomials_edited[1]: 
                coeff = poly0[0] * poly1[0]
                power = poly0[1] + poly1[1]
                resulting_poly.append([coeff, power])
        polynomials_edited.remove(polynomials_edited[0])
        polynomials_edited.remove(polynomials_edited[0])
        polynomials_edited.append(resulting_poly)

    # print("2: ", polynomials_edited)

    ## form a dictionary, where the key is the power, and the value is the sum of 
    ## coefficient

    mydict = {} 
    max_power = 0 
    for i in polynomials_edited[0]: 
        if i[1] in mydict: ## i[1] is the power of the element 
            mydict[i[1]] += i[0] ## mydict[power] += coefficient 
        else: 
            mydict[i[1]] = i[0] ## mydict[power] = coefficient 
        if i[1] > max_power: 
            max_power = i[1]
    
    # print("3: ", mydict)

    results = [] 
    for i in range(max_power, -1, -1): 
        results.append(mydict[i])

    ## alternative way instead of using max_power 
    # sorted(mydict, reverse=True)
    # results = []
    # for key, value in mydict.items(): 
    #     results.append(value)

    all_0 = True 
    for i in results:
        if i != 0: 
            all_0 = False 

    if all_0: 
        return [0]

    return results

# multiply(polynomials)
# DO NOT MODIFY THE CODE BELOW!
name = "main"
if name == "main":
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
    if isinstance(result, list):
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