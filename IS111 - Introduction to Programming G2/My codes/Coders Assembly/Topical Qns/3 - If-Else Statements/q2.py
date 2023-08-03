def greet_user(name,gender):
    # YOUR CODE GOES HERE
    print("Nice to meet you,", end=" ")
    if gender == 'F':
        print("Ms.", end=" ")
    elif gender == 'M':
        print("Mr.", end=" ")
    print(name)
    pass


# DO NOT MODIFY THE BELOW TEST CASES
print('----Test Case 1----')
greet_user('Sarah Chin','F')

print('----Test Case 2----')
greet_user('Lancy Ng Fu Ting','M')

print('----Test Case 3----')
greet_user('Jacqueline','None')