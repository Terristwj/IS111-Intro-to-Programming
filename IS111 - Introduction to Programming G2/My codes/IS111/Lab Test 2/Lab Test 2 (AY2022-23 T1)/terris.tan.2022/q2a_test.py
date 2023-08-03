from q2a import get_n_odd_numbers

def run_test_case(tc_num, filename, n, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_n_odd_numbers("{filename}", {n})')
        print()
        print(f'Expected: {expected_output}')
        result = get_n_odd_numbers(filename, n)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned list the same as expected? {expected_output == result}')
    
expected_output = [3, 621]
run_test_case(1, 'sample1.txt', 2, expected_output, "<class 'list'>")

expected_output = [3, 621, 31]
run_test_case(2, 'sample1.txt', 100, expected_output, "<class 'list'>")

expected_output = [3]
run_test_case(3, 'sample1.txt', 1, expected_output, "<class 'list'>")

expected_output = [3, 621, 31]
run_test_case(4, 'sample1.txt', 3, expected_output, "<class 'list'>")

expected_output = []
run_test_case(5, 'sample1.txt', 0, expected_output, "<class 'list'>")

