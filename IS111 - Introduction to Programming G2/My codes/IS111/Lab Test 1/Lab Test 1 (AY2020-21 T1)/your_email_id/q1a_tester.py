try:
    from q1a import get_tank_volume
except:
    pass

########  Internal  ########
filename = 'q1a.csv'

# find the username
import os
cwd = os.path.dirname(__file__)
username = cwd.split("/")[-1]

def append_to_file(content):
    with open(filename, 'a') as f:
        f.write(username + content + '\n')
########  Internal  ########

count_correct = 0

test_cases = [  (30, 40, 45, 54), 
                (20, 30, 50, 30), 
                (15, 22, 70, 23),
                (58, 96, 45,250),
                (42, 34, 39,55)]

num = 0
for width, depth, height,result  in test_cases:
    num += 1
    try:
        print(f'TC {num}: get_tank_volume({width}, {depth}, {height})')
        print(f'Expected:{result}')
        print(f'Actual  :{get_tank_volume(width, depth, height)}')

        if get_tank_volume(width, depth, height) == result:
            count_correct += 1
            print('Result  :Pass')
            print()
        elif str(get_tank_volume(width, depth, height)) == str(result) \
                or int(get_tank_volume(width, depth, height)) == int(result): 
            print('Result  :Partial Pass(Wrong data type) ')
            print(f'Expected:{type(result)}')
            print(f'Actual  :{type(get_tank_volume(width, depth, height))}')
            print()
            count_correct += 0.8
    except:
            print('Result  :Fail')
            print()

try:
    num += 1
    print(f'TC {num}: get_tank_volume({width}, {depth}, {height})')
    print(f'Expected:{type(result)}')
    print(f'Actual  :{type(get_tank_volume(width, depth, height))}')
    if isinstance(get_tank_volume(width, depth, height), int):
        count_correct += 1
        print('Result  :Pass')
        print()
    else:
        print('Result  :Fail')
        print()        
except:
    print('Result  :Fail')
    print()

count_correct = int(count_correct)


marks = 0
if count_correct in (1,):
    marks = 1.5
elif count_correct in (2, 3):
    marks = 2
elif count_correct in (4, 5):
    marks = 2.5
elif count_correct in (6,):
    marks = 3
    

print(f'{count_correct} of {num} passed.')
print(f'{marks} marks awarded.')

########  Internal  ########
append_to_file(f',{marks},{count_correct}')
########  Internal  ########


