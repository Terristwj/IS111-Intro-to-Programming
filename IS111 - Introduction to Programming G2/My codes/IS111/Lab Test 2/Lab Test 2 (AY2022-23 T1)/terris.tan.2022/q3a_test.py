from q3a import read_courses

def run_test_case(tc_num, filename, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: read_courses("{filename}")')
        print()
        print(f'Expected: {expected_output}')
        result = read_courses(filename)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
    
expected_output = {'Eric Wong': [('Math', 2021, 2, 2, 3.6), ('Chemistry', 2022, 1, 1, 4.0)], 'Andy Lau': [('English', 2021, 1, 2, 3.6), ('Math', 2022, 1, 2, 4.0)], 'Jeffrey Heer': [('Chemistry', 2022, 1, 1, 3.8)]}
run_test_case(1, 'course_scores.txt', expected_output, "<class 'dict'>")
