from q3b import calculate_student_gpa

def run_test_case(tc_num, filename, start, end, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: calculate_student_gpa("{filename}", {start}, {end})')
        print()
        print(f'Expected: {expected_output}')
        result = calculate_student_gpa(filename, start, end)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
    
expected_output = {'Eric Wong': (1, 4.0), 'Andy Lau': (1, 4.0), 'Jeffrey Heer': (1, 3.8)}
run_test_case(1, 'course_scores.txt', (2022,1),(2022,1), expected_output, "<class 'dict'>")

expected_output = {'Eric Wong': (2, 3.7), 'Andy Lau': (2, 3.8), 'Jeffrey Heer': (1, 3.8)}
run_test_case(2, 'course_scores.txt', (2021,1),(2022,1), expected_output, "<class 'dict'>")
