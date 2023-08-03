from q4c import find_all_words

def run_test_case(tc_num, word_list, input_str, step, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: find_all_words({word_list}, "{input_str}", {step})')
        print()
        print(f'Expected: {expected_output}')
        result = find_all_words(word_list, input_str, step)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned list the same as expected? {expected_output == result}')
    
expected_output = [[6, 7, 8, 10], [0, 2, 3, 4], [0, 2, 3, 5], [0, 2, 4, 5], [1, 2, 3, 4], [1, 2, 3, 5], [1, 2, 4, 5], []]
run_test_case(1, ['pane', 'bull', 'not'], 'bbulllpanredno', 1, expected_output, "<class 'list'>")

expected_output = [[], [7, 9, 11, 13], [7, 9, 11, 14], []]
run_test_case(2, ['plane', 'bull', 'not'], 'planredbbunloll', 2, expected_output, "<class 'list'>")

expected_output = [[0,1,2], [3,4,5], []]
run_test_case(3, ['cat', 'dog', 'pig'], 'catdog', 1, expected_output, "<class 'list'>")

expected_output = [[], [], []]
run_test_case(4, ['cat', 'dog', 'pig'], 'catdog', 2, expected_output, "<class 'list'>")
