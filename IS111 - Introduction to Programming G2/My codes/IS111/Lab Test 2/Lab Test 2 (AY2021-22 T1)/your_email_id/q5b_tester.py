import sys
from q5a import get_persons


def check_output(input_list, expected, actual, n, m):
        if expected == [] and actual == []:
            return True
        # length
        if len(expected) != len(actual):
            return False
        # elements
        if set(expected) != set(actual):
            return False
        
        # enclosing condition
        # if the input list already satisfies the condition
        # should return the same list with no change
        if len(get_persons(input_list, n)) >= m:
            if input_list != actual:
                return False
        
        if len(get_persons(actual, n)) < m:
            return False

        return True

def run_test():
    print('########## TESTING Q5b ##########')
    # Test Cases
    person_list_1 = [('A', 'F'), ('B', 'M'), ('C', 'F'), ('E', 'M'), ('D', 'F'), ('F', 'F'), ('G', 'M')]
    person_list_2 = [('alpha', 'F'), ('beta', 'F'), ('gamma', 'M'), ('delta', 'M'), ('zeta', 'F'), ('epsilon', 'F'), ('theta', 'F')]
    
    test_cases = [(person_list_1, 3, 2, [('A', 'F'), ('B', 'M'), ('C', 'F'), ('E', 'M'), ('D', 'F'), ('F', 'F'), ('G', 'M')]), # person_list already satisfy enclosing conditions
                (person_list_1, 4, 1, [('A', 'F'), ('B', 'M'), ('C', 'F'), ('E', 'M'), ('G', 'M'), ('D', 'F'), ('F', 'F')]),
                (person_list_2, 4, 2, [('alpha', 'F'), ('beta', 'F'), ('gamma', 'M'), ('zeta', 'F'), ('delta', 'M'), ('epsilon', 'F'), ('theta', 'F')]),
                (person_list_2, 5, 1, [('alpha', 'F'), ('beta', 'F'), ('gamma', 'M'), ('zeta', 'F'), ('delta', 'M'), ('epsilon', 'F'), ('theta', 'F')])
                ]

    # Counter is to record how many test cases are passed.
    counter = 0
    marks = 0.0

    try:
        from q5b import get_seating

        for (person_list, n, m, result) in test_cases:
            try:
                my_result = get_seating(person_list, n, m)
                
                if check_output(person_list, result, my_result, n, m):
                    counter += 1
                else:
                    print(f'Test case failed: get_seating("{person_list}", {n}, {m})')
                    print(f'Expected: {result}')
                    print(f'Actual: {my_result}')
                    print()
            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    # There are in total 4 test cases.
    # We allocate 1 mark (!!) for q5b
    marks = counter * 0.25
    return (counter, marks)

if __name__ == "__main__":
    counter, marks = run_test()
    print(f'Number of test cases passed: {counter}')
    print(f'Marks awarded: {marks}')