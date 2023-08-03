def greet_user(name,gender):
    if gender == "F":
        print("Nice to meet you, Ms. " + name)
    elif gender == "M":
        print("Nice to meet you, Mr. " + name)
    else:
        print("Nice to meet you, " + name)


# DO NOT MODIFY THE BELOW TEST CASES
print('----Test Case 1----')
greet_user('Sarah Chin','F')

print('----Test Case 2----')
greet_user('Lancy Ng Fu Ting','M')

print('----Test Case 3----')
greet_user('Jacqueline','None')
