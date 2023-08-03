import sys

def run_test():
    print('########## TESTING Q2a ##########')
    # Test Cases
    test_cases = [('jing jiang#wang yong#donta', ['jing jiang', 'wang yong', 'donta']),
                ('first1 last1####first2 mid2 last2##first3', ['first1 last1', 'first2 mid2 last2', 'first3']),
                ('a###123##$$4  56#b', ['a', '123', '$$4  56', 'b']),
                ('a  b', ['a  b'])]

    # Counter is to record how many test cases are passed.
    counter = 0
    marks = 0.0

    try:
        from q2a import extract_names_1

        for (str_name, result) in test_cases:
            try:
                my_result = extract_names_1(str_name)
                if my_result == result:
                    counter += 1
                else:
                    print(f'Test case failed: extract_names_1({str_name})')
                    print(f'Expected: {result}')
                    print(f'Actual: {my_result}')
                    print()
            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    # There are in total 4 test cases.
    # We allocate 4 marks for q2a.
    marks = counter
    return (counter, marks)

if __name__ == "__main__":
    counter, marks = run_test()
    print(f'Number of test cases passed: {counter}')
    print(f'Marks awarded: {marks}')