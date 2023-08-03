# Name:
# Email ID:
def get_tuples_of_size(tup_list, num):
    # Write your code here.
    my_list = []
    for tup in tup_list:
        if len(tup) >= num:
            my_list.append(tup)
    return my_list

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, tup_list, num, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_tuples_of_size({tup_list}, {num})')
        print()
        print(f'Expected: {expected_output}')
        result = get_tuples_of_size(tup_list, num)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
    
    run_test_case(1, [(1, -1, 18), (4, 2, 6), (19, 0)], 3, '[(1, -1, 18), (4, 2, 6)]', "<class 'list'>")
    run_test_case(2, [(1, 2, 0), (4, 20)], 1, '[(1, 2, 0), (4, 20)]', "<class 'list'>")
    run_test_case(3, [(1, 2), (9, 6), (-9, 2)], 4, '[]', "<class 'list'>")
    run_test_case(4, [], 1, '[]', "<class 'list'>")