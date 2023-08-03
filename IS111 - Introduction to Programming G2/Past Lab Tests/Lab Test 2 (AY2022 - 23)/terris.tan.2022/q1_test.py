from q1 import check_record

def run_test_case(tc_num, record, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: check_record({record})')
        print()
        print(f'Expected: {expected_output}')
        result = check_record(record)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned value the same as expected? {expected_output == result}')
    
expected_output = True
run_test_case(1, ('abc', 3, 51), expected_output, "<class 'bool'>")

expected_output = False
run_test_case(2, ('apple', 5, 3), expected_output, "<class 'bool'>")

expected_output = False
run_test_case(3, ('game', 3, 4), expected_output, "<class 'bool'>")

expected_output = False
run_test_case(4, ('', -1, 0), expected_output, "<class 'bool'>")
