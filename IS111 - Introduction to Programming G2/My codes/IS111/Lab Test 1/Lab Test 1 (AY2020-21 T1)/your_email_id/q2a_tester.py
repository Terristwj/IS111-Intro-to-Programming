try:
    from q2a import get_sum_of_digits
except:
    pass


########  Internal  ########
filename = 'q2a.csv'

# find the username
import os
cwd = os.path.dirname(__file__)
username = cwd.split("/")[-1]

def append_to_file(content):
    with open(filename, 'a') as f:
        f.write(username + content + '\n')
########  Internal  ########


count_correct = 0

test_cases = [  ("345", 12),
                ("SMU12-5-3-4", 15),
                ("SIS2*5*13", 11),
                ("124-12*[8]+4", 22),
                ("LabTEST", 0),
                ("", 0),
                ("Lab-Test2", 2)]
                
num = 0
for value,result in test_cases:
    try:
        num += 1
        print(f'TC {num}: get_sum_of_digits("{value}")')
        print(f'Expected:{result}')
        print(f'Actual  :{get_sum_of_digits(value)}')

        if  get_sum_of_digits(value) == result:
            count_correct += 1
            print('Result  :Pass')
            print()
        else:
            print('Result  :Fail')
            print()
    except:
        print('Result  :Fail')
        print()

try:
    num += 1
    print(f'TC {num}: get_sum_of_digits("{value}")')
    print(f'Expected:{type(result)}')
    print(f'Actual  :{type(get_sum_of_digits(value))}')

    if isinstance(get_sum_of_digits(value), int):
        count_correct += 1
        print('Result  :Pass')
        print()
    else:
        print('Result  :Fail')
        print()
except:
    print('Result  :Fail')
    print()



marks = 0
if count_correct in (1,):
    marks = 1
elif count_correct in (2,3):
    marks = 2
elif count_correct in (4,5):
    marks = 3
elif count_correct in (6,7):
    marks = 3.5
elif count_correct in (8,):
    marks = 4


print(f'{count_correct} of {num} passed.')
print(f'{marks} marks awarded.')


########  Internal  ########
append_to_file(f',{marks},{count_correct}')
########  Internal  ########
   