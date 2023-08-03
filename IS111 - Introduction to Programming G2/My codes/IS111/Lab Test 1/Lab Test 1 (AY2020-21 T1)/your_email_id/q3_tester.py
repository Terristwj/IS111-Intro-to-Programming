
try:
    from q3 import check_math
except:
    pass


########  Internal  ########
filename = 'q3.csv'
import os
# find the username
cwd = os.path.dirname(__file__)
username = cwd.split("/")[-1]


def append_to_file(content):
    with open(filename, 'a') as f:
        f.write(username + content + '\n')
########  Internal  ########


count_correct = 0
result_list = []

test_cases = [
    # check all possible operators
    (["5 + 8 = 3"], False),
    (["5 + 2 = 7"], True),
    (["5-2=7"], False),
    (["12-11=1"], True), # (["1-11=-10"], True), 
    (["5*8=3"], False),
    (["5*2=10"], True),
    (["20//8=1"], False),
    (["5//8=0"], True),
    (["2%8=1"], False),
    (["3%8=3"], True),
    
    # 2 equations
    (["5*8=40", "24//7=3"], True),
    (["8-8 =   0", "2 % 4 = 2  "],True),
    # (["6-8 =   -2", "2 % 4 = 2  "],True),
    ([" 5 +   8 =13", "2  * 4 = 8 "],True),

    # 2 equations(1 valid, 1 invalid)
    (["5*8=40", "9- 7=3"], False),
#    (["0 - 100 =   -100", "2 * 4 = 2  "], False),
    (["10000000000000000 - 1 =   9999999999999999", "2 * 4 = 2  "], False),
    ([" 5 +   8 =13", "2000  * 10000 = 20000000 "],True),
    ([" 0 +   8 =8", "0  * 0 = 0 "],True),

    # more than 2
    # check for ordering 
    (["24 % 10 = 3", "8 // 3 = 2", "100 - 20 = 80"],False),
    (["8 // 3 = 2", "24 % 10 = 3", "100 - 20 = 80"],False),
    ([ "8 // 3 = 2", "100 - 20 = 80", "24 % 10 = 3"],False),
    (["24 % 10 = 4", "8 // 3 = 2", "100 - 20 = 80"],True),
    (["8 // 3 = 2", "24 // 10=2", "100 - 20 = 80"],True),
    ([ "8 // 3 = 2", "100 - 20 = 80", "1000 * 9000 = 9000000"],True),

    # more than 3
#    (["   3  + 7=10 ", "5 %   2    = 1", " 10    //3 = -3", "10   * 20 =   200"], False),
    (["   3  + 7=10 ", "5 %   2    = 1", " 12    //3 = 3", "10   * 20 =   200"], False),
    (['   19 + 7=26 ', '5 %   2    = 1', ' 1278   //33 = 38', '10   * 20 =   200'], True),


    # corner case
    ([], True)
    
    
    ]

num = 0
for equation,result in test_cases:

    try:
        num += 1
        print(f'TC {num}: check_math({equation}) ))')
        print(f'Expected:{result}')
        print(f'Actual  :{check_math(equation)}')
    

        if check_math(equation) == result:
            count_correct += 1
            print('Result  :Pass')
            print()
        else:
            print('Result  :Fail')
            print()

        result_list.append(check_math(equation))
        # else:
            # print(equation, check_math(equation), result)
    except:
        print('Result  :Fail')
        print()


# if answers for all test cases are the same ..
# the result is hardcoded
is_brute_force = True
if result_list:
    value = result_list[0]
    for element in result_list[:-1]: # exclude [] TC
        if element != value:
            is_brute_force = False
            break

if is_brute_force:
    count_correct = 0
    print(f'Return value is the same for all: {result_list[:-1]}')


try:
    num += 1
    equation,result = test_cases[-2]
    print(f'TC {num}: check_math({equation}) ))')
    print(f'Expected:{type(result)}')
    print(f'Actual  :{type(check_math(equation))}')

    if isinstance(check_math(equation), bool ):
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


if count_correct == 0:
    marks = 0
elif count_correct < 5:
    marks = 0.5
elif count_correct < 10:
    marks = 1
elif count_correct < 15:
    marks = 1.5
elif count_correct < 20:
    marks = 2
elif count_correct < 23:
    marks = 2.5
elif count_correct < 25:
    marks = 3
elif count_correct < 27:
    marks = 3.5
elif count_correct == 27:
    marks = 4


print(f'{count_correct} of {num} passed.')
print(f'{marks} marks awarded.')


########  Internal  ########
append_to_file(f',{marks},{count_correct}')
########  Internal  ########