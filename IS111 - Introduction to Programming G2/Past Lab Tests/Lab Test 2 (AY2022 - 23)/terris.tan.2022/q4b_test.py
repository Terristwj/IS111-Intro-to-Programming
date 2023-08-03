from q4b import find_words

def run_test_case(tc_num, word_list, input_str, step, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: find_words({word_list}, "{input_str}", {step})')
        print()
        print(f'Expected: {expected_output}')
        result = find_words(word_list, input_str, step)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned list the same as expected? {expected_output == result}')
    
expected_output = [[],[0,1,5], [6,7,8,9],[]]
run_test_case(1, ['no', 'cat', 'doog', 'not'], 'caaaatdoogname', 1, expected_output, "<class 'list'>")

expected_output = [[19, 21, 24], [8, 10, 13]]
run_test_case(2, ['cat', 'dog'], 'gaaaatttdoonagmedogcaaggt', 2, expected_output, "<class 'list'>")

expected_output = [[]]
run_test_case(3, ['notin'], 'notin', 3, expected_output, "<class 'list'>")