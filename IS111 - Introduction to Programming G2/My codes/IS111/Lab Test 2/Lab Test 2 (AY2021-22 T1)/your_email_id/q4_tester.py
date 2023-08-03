import sys

# need to check the list of tuples for each key-value pair
# as any order is correct
def compare_dicts(expected, actual):
    if expected == actual:
        return True
    if len(expected) != len(actual):
        return False
        
    for key in expected:
        if len(expected[key]) != len(actual[key]):
            return False

        if set(expected[key]) != set(actual[key]):
            return False
        
    return True

def run_test():
    print('########## TESTING Q4 ##########')
    # Test Cases
    test_cases = [('schedule3.txt', {'Tue': [(10, 11, 'user0')], 'Wed': [(13, 16, 'user1'), (13, 16, 'user2')], 'Mon': [(9, 17, 'user3')], 'Sat': [(14, 16, 'user4'), (14, 16, 'user5'), (14, 16, 'user6'), (14, 16, 'user7')]}),
                ('schedule4.txt', {'Wed': [(10, 17, 'ahlian'), (10, 17, 'ahbeng'), (10, 17, 'user2')], 'Thu': [(11, 17, 'user1')], 'Sun': [(13, 16, 'user1'), (13, 16, 'user3')]}),
                ('schedule5-1.txt', {'Tue': [(10, 15, 'user1'), (11, 16, 'user2'), (11, 16, 'user3')], 'Thu': [(13, 15, 'user4'), (13, 15, 'user5')]}),
                ('schedule5-2.txt', {'Tue': [(10, 14, 'user1'), (10, 14, 'user2'), (11, 16, 'user3')], 'Thu': [(9, 12, 'user10'), (9, 12, 'user11')]}),
                ('schedule6.txt',  {'Sat': [(10, 14, 'user1'), (12, 16, 'user2')], 'Thu': [(9, 13, 'user2'), (9, 13, 'user3')]}),
                ('schedule7.txt', {'Tue': [(10, 13, 'alina'), (10, 13, 'ahbeng'), (10, 13, 'ahlian'), (9, 16, 'starkov')], 'Wed': [(9, 10, 'potter'), (9, 11, 'harry'), (9, 10, 'alina')], 'Fri': [(14, 17, 'ron'), (11, 14, 'starkov'), (14, 17, 'tony'), (14, 17, 'ahlian')], 'Sat': [(14, 17, 'harry')]})
                ]

    # Counter is to record how many test cases are passed.
    counter = 0
    marks = 0.0

    try:
        from q4 import read_schedule

        for (filename, result) in test_cases:
            try:
                my_result = read_schedule(filename)
                if compare_dicts(my_result, result):
                    counter += 1
                else:
                    print(f'Test case failed: read_schedule("{filename}")')
                    print(f'Expected: {result}')
                    print(f'Actual: {my_result}')
                    print()
            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    # There are in total 6 test cases.
    # We allocate 3 marks for q4.
    marks = counter * 0.5
    return (counter, marks)

if __name__ == "__main__":
    counter, marks = run_test()
    print(f'Number of test cases passed: {counter}')
    print(f'Marks awarded: {marks}')