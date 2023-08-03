import sys

def run_test():
    print('########## TESTING Q2b ##########')
    # Test Cases
    test_cases = [(['jing jiang', 'wendy', 'donta'], ['jing jiang', 'wendy', 'donta']),
                (['fi0rst', 'first1 last1', '2first 2mid! l2as!t'], ['first','first last', 'first mid last']),
                (['$23abc45', '--def67', '123$'], ['abc', 'def']),
                (['!!2', '12j e34ssi5e', '6789', 'mei  li'], ['j essie', 'mei  li']),
                (['@', '$ @@', '@   12 23'], []),
                (['!#a('], ['a'])]

    # Counter is to record how many test cases are passed.
    counter = 0
    marks = 0.0

    try:
        from q2b import extract_names_2

        for (name_list, result) in test_cases:
            try:
                my_result = extract_names_2(name_list)
                if my_result == result:
                    counter += 1
                else:
                    print(f'Test case failed: extract_names_2({name_list})')
                    print(f'Expected: {result}')
                    print(f'Actual: {my_result}')
                    print()
            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    # There are in total 6 test cases.
    # We allocate 3 marks for q2b.
    marks = counter/2    
    return (counter, marks)

if __name__ == "__main__":
    counter, marks = run_test()
    print(f'Number of test cases passed: {counter}')
    print(f'Marks awarded: {marks}')