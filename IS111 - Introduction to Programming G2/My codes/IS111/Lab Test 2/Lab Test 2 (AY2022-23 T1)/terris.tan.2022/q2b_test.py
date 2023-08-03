from q2b import filter_words

def run_test_case(tc_num, filename, end, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: filter_words("{filename}", "{end}")')
        print()
        print(f'Expected: {expected_output}')
        result = filter_words(filename, end)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned list the same as expected? {expected_output == result}')
    
expected_output = ['there', 'separate', 'phone', 'coffee', 'bubble', 'ice', 'cake']
run_test_case(1, 'w_sample1.txt', 'e', expected_output, "<class 'list'>")

expected_output = ['stair', 'bar', 'after', 'air', 'player', 'chair', 'flair']
run_test_case(2, 'w_sample1.txt', 'r', expected_output, "<class 'list'>")

expected_output = ['bread']
run_test_case(3, 'w_sample1.txt', 'd', expected_output, "<class 'list'>")
