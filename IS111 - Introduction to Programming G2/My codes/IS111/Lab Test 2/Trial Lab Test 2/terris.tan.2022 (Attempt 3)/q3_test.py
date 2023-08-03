from q3 import create_email_dict

print('Test Case 1:')
result = create_email_dict(['abc@smu.edu.sg', 'xyz.2021@scis.smu.edu.sg', 'john.smith.2020@soe.smu.edu.sg', 'alice.lin.2020@smu.edu.sg', 'dd.2021@scis.smu.edu.sg'])
expected_result = {'scis-2021': ['xyz.2021@scis.smu.edu.sg', 
                                 'dd.2021@scis.smu.edu.sg'],
                   'soe-2020': ['john.smith.2020@soe.smu.edu.sg']}


print('Expected: ' + str(expected_result))
print('Actual  : ' + str(result))

print("Expected type of returned value: <class 'dict'>")
print('Actual type of returned value  : ' + str(type(result)))


print('\nTest Case 2:')
result = create_email_dict(['abc@smu.edu.sg', 'xyz.2021@smu.edu.sg', 'a.b.c@soa.smu.edu.sg'])
print('Expected: {}')
print('Actual  : ' + str(result))
