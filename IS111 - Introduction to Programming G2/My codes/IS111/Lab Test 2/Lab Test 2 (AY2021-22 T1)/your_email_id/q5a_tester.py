import sys

def compare_lists(expected, actual):
    return set(expected) == set(actual) and len(expected) == len(actual)

def run_test():
    print('########## TESTING Q5a ##########')
    # Test Cases
    person_list_1 = [('A', 'F'), ('B', 'M'), ('C', 'F'), ('E', 'M'), ('D', 'F'), ('F', 'F'), ('G', 'M')]
    person_list_2 = [('alpha', 'F'), ('beta', 'F'), ('gamma', 'F'), ('delta', 'F'), ('epsilon', 'F'), ('zeta', 'M')]
    
    test_cases = [(person_list_1, 2, [('B', 'M'), ('C', 'F'), ('E', 'M'), ('G', 'M'), ('A', 'F') ]),
                (person_list_1, 3, [('E', 'M'), ('G', 'M')]),
                (person_list_1, 4, []),
                (person_list_2, 5, [('zeta', 'M')]),
                ([('loner', 'M')], 2, []),
                ([('loner', 'M'), ('friend', 'F')], 2, []),
                ([('loner', 'M'), ('friend', 'F'), ('new friend', 'F')], 2, [('loner', 'M')]),
                ([('loner', 'M'), ('friend', 'F'), ('new friend', 'F'), ('more friend', 'F')], 4, [])
                ]

    # Counter is to record how many test cases are passed.
    counter = 0
    marks = 0.0
    always_empty = True

    try:
        from q5a import get_persons

        for (person_list, n, result) in test_cases:
            try:
                my_result = get_persons(person_list, n)
                if len(my_result) > 0:
                    always_empty = False
                
                if compare_lists(my_result, result) and not always_empty:
                    counter += 1
                else:
                    print(f'Test case failed: get_persons("{person_list}", {n})')
                    print(f'Expected: {result}')
                    print(f'Actual: {my_result}')
                    if always_empty:
                        print(f'Always return empty: {always_empty}')
                    print()
            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    # There are in total 8 test cases.
    # We allocate 2 marks for q5a.
    marks = counter * 0.25
    return (counter, marks)

if __name__ == "__main__":
    counter, marks = run_test()
    print(f'Number of test cases passed: {counter}')
    print(f'Marks awarded: {marks}')
