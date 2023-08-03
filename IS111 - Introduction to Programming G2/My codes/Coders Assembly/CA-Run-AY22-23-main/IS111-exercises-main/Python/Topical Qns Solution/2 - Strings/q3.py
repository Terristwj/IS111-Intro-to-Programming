def mask_email(email):
    index = email.find('@')
    masked_email = 'x' * len(email[0:index]) + email[index:]

    return masked_email


# DO NOT MODIFY THE BELOW TEST CASES
print('----Test Case 1----')
result = mask_email('sarah@gmail.com')
print("Expected: xxxxx@gmail.com" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = mask_email('shiba.inu@smu.edu.sg')
print("Expected: xxxxxxxxx@smu.edu.sg" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = mask_email('lisakudrow.2019@scis.smu.edu.sg')
print("Expected: xxxxxxxxxxxxxxx@scis.smu.edu.sg" )
print("Actual:   " + str(result))
print()