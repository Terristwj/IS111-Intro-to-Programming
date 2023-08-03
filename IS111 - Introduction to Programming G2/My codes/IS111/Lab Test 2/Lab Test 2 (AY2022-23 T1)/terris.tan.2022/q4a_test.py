from q4a import get_flight_durations

def run_test_case(tc_num, filename, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_flight_durations("{filename}")')
        print()
        print(f'Expected: {expected_output}')
        result = get_flight_durations(filename)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
        
        
expected_dict =  {'AirAsia': [('AK705', 'Kuala Lumpur', 'Singapore', 65, 46), ('AK1721', 'Penang', 'Singapore', 90, 73)], 'Malaysia Airlines': [('MH1436', 'Kuala Lumpur', 'Langkawi', 65, 49)]}
run_test_case(1, 'flight1.txt' , expected_dict, "<class 'dict'>")