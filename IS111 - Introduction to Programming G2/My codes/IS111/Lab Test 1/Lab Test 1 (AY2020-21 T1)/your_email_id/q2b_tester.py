try:
    from q2b import get_max_of_min
except:
    pass


########  Internal  ########
filename = 'q2b.csv'
import os
# find the username
cwd = os.path.dirname(__file__)
username = cwd.split("/")[-1]


def append_to_file(content):
    with open(filename, 'a') as f:
        f.write(username + content + '\n')
########  Internal  ########



test_cases = [([(2, 4, 5)], 2),
              ([(4, 2, 5)], 2),
              ([(5, 4, 2)], 2),

              ([(3, 5, 0), (-2, -5, 6)], 0),
              ([(5, 0, 3), (-2, -5, 6)], 0),
              ([(0, 5, 3), (-2, -5, 6)], 0),

              ([(-2, -5, 6), (3, 5, 0)], 0),
              ([(-2, -5, 6), (5, 0, 3)], 0),
              ([(-2, -5, 6), (0, 5, 3)], 0),

              ([(5, -7, 10), (15, -3, -1), (-5, 5, 10)], -3),
              ([(5, -7, 10), (-3, 9, 3), (-5, 5, 10)], -3),
              ([(-3, 7, 10), (-5, 9, 3), (-5, 5, 10)], -3),

              ([], None),
              ([(-5, 5, 10), (15, 9, -4), (-5, 5, 10), (15, 9, -3)], -3),
              ([(-5, 5, 10), (15, 9, -4),  (15, -3, 9), (-5, 5, 10)], -3),
              ([(-5, 5, 10),  (-3, 15, 9), (15, 9, -4), (-5, 5, 10)], -3)
              # last case is used to check data type
              ]

count_correct = 0
num = 0
for num_tuples, result in test_cases:
    
    try:
        num += 1
        print(f'TC {num}: get_max_of_min({num_tuples}))')
        print(f'Expected:{result}')
        print(f'Actual  :{get_max_of_min(num_tuples)}')

        if get_max_of_min(num_tuples) == result:
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
    print(f'TC {num}: get_max_of_min({num_tuples}))')
    print(f'Expected:{type(result)}')
    print(f'Actual  :{type(get_max_of_min(num_tuples))}')
    if isinstance(get_max_of_min(num_tuples), int):
        count_correct += 1
        print('Result  :Pass')
        print()
    else:
        print('Result  :Fail')
        print()
except:
    print('Result  :Fail')
    print()


# those who uses max/min functions would fail these test cases
import builtins
builtins.min = 1
builtins.max = 1

try:
    from q2b import get_max_of_min
except:
    pass

for num_tuples, result in test_cases:
    try:
        num += 1
        print(f'TC {num}: get_max_of_min({num_tuples}))')
        print(f'Expected:{result}')
        print(f'Actual  :{get_max_of_min(num_tuples)}')


        if get_max_of_min(num_tuples) == result:
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
    print(f'TC {num}: get_max_of_min({num_tuples}))')
    print(f'Expected:{type(result)}')
    print(f'Actual  :{type(get_max_of_min(num_tuples))}')

    if isinstance(get_max_of_min(num_tuples), int):
        count_correct += 1
        print('Result  :Pass')
        print()
    else:
        print('Result  :Fail')
        print()
except Exception as e:
    print(f'Result  :Fail')
    print()    

marks = 0

if count_correct == 0:
    marks = 0
elif count_correct  <= 10:
    marks = 1
elif count_correct <= 20:
    marks = 1.5
elif count_correct <= 28:
    marks = 2
elif count_correct < 33:
    marks = 2.5
elif count_correct == 34:
    marks = 3



print(f'{count_correct} of {num} passed.')
print(f'{marks} marks awarded.')


########  Internal  ########
append_to_file(f',{marks},{count_correct}')
########  Internal  ########