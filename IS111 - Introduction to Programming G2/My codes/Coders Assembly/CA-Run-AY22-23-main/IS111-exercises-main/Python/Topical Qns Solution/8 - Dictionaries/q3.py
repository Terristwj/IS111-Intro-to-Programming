def create_prime_dict(num_list):
    num_dict = {}
    for num in num_list:
        # Check if number is prime
        is_prime = True
        for i in range (2,num):
            if num % i == 0:
                is_prime = False
        
        # Inserting into dictionary
        num_dict[num] = is_prime

    return num_dict

print('----Test Case 1----')
result = create_prime_dict([2, 3, 5, 10, 20, 23])
print("Expected: {2: True, 3: True, 5: True, 10: False, 20: False, 23: True}" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = create_prime_dict([4, 5, 6, 8, 11, 12])
print("Expected: {4: False, 5: True, 6: False, 8: False, 11: True, 12: False}" )
print("Actual:   " + str(result))
print()