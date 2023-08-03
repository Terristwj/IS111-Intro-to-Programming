import sys

def run_test():
    print('########## TESTING Q1 ##########')
    # Test Cases
    test_cases = [ ([], 2, []),
                ([(1, 1, 1), (2, 2), (3, 3)], 4 , []),
                ([(1, )], 1, [(1, )]),
               ([(2, 2, 1), (2, 6), (1, 0)], 3 , [(2, 2, 1)]),
               ([(4, 2, 6), (11, 12, 13), (1, 2, 3, 4, 5), (6, 7, 8, 9, 10)], 4, [(1, 2, 3, 4, 5),(6, 7, 8, 9, 10)]),
               ([(1, 1, 1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3)], 5 , [(1, 1, 1, 1, 1), (2, 2, 2, 2, 2), (3, 3, 3, 3, 3)]),
                ([(1, 1, 1, 1, 1), (-2, -2, -2, -2, -2, -2), (3, 3)], 6, [(-2, -2, -2, -2, -2, -2)])]

    # Counter is to record how many test cases are passed.
    counter = 0
    marks = 0.0

    try:
        from q1 import get_tuples_of_size

        for (tup_list, num, result) in test_cases:
            try:
                my_result = get_tuples_of_size(tup_list, num)
                if my_result == result:
                    counter += 1
                else:
                    print(f'Test case failed: get_tuples_of_size({tup_list}, {num})')
                    print(f'Expected: {result}')
                    print(f'Actual: {my_result}')
                    print()
            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    # There are in total 7 test cases.
    # We allocate 7 marks for q1.
    marks = counter
    return (counter, marks)

if __name__ == "__main__":
    counter, marks = run_test()
    print(f'Number of test cases passed: {counter}')
    print(f'Marks awarded: {marks}')