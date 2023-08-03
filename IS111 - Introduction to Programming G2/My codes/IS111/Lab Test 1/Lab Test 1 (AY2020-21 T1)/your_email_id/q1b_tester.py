try:
    from q1b import is_compatible
except:
    pass

########  Internal  ########
filename = 'q1b.csv'

# find the username
import os
cwd = os.path.dirname(__file__)
username = cwd.split("/")[-1]

def append_to_file(content):
    with open(filename, 'a') as f:
        f.write(username + content + '\n')
########  Internal  ########

count_correct = 0

print()
print('-' * 20)
print()

# all possible cases
test_cases = [  ('A', 'AB', True),
                ('B', 'AB', True),
                ('AB', 'AB', True),
                ('O', 'AB', True),
                ('A', 'A', True),
                ('B', 'A', False),
                ('AB', 'A', False),
                ('O', 'A', True),
                ('A', 'B', False),
                ('B', 'B', True),
                ('AB', 'B', False),
                ('O', 'B', True),
                ('A', 'O', False),
                ('B', 'O', False),
                ('AB', 'O', False),
                ('O', 'O', True)]

num = 0
for patient,donor,result in test_cases:
    num += 1
    print(f'TC {num}: is_compatible("{patient}", "{donor}")')
    print(f'Expected:{result}')
    print(f'Actual  :{is_compatible(patient, donor)}')
    try:
        if is_compatible(patient, donor) == result:
            count_correct += 1
            print('Result  :Pass')
            print()
        elif str(is_compatible(patient, donor)) == str(result):
            count_correct += 0.8
            print('Result  :Partial Pass(Wrong data type) ')
            print(f'Expected:{type(result)}')
            print(f'Actual  :{type(is_compatible(patient, donor))}')
            print()
        else:
            print('Result  :Fail')
            print()
    except:
            print('Result  :Fail')
            print()

try:
    num += 1
    result = is_compatible(patient, donor)
    print(f"TC {num}: is_compatible('{patient}', '{donor}')")
    print(f'Expected:{type(result)}')
    print(f'Actual  :{type(is_compatible(patient, donor))}')

    if isinstance(result, bool):
        count_correct += 1
        print('Result  :Pass')
        print()
    else:
        print('Result  :Fail')
        print()          
except:
    print('Result  :Fail')
    print()
# awarding partial marks .. so convert float to int
count_correct = int(count_correct)

marks = 0
if count_correct in (1,2,3,4):
    marks = 2
elif count_correct in (5,6,7,8):
    marks = 2.5
elif count_correct in (9,10,11,12):
    marks = 3
elif count_correct in (13,14,15,16):
    marks = 3.5
elif count_correct in (17,):
    marks = 4

print(f'{count_correct} of {num} passed.')
print(f'{marks} marks awarded.')



########  Internal  ########
append_to_file(f',{marks},{count_correct}')
########  Internal  ########
    

    

