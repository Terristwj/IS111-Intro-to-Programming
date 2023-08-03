import sys

def print_test_case(str_list):
    print("\tget_all_third_digits(" + str(str_list) + ")")


def match_as_string(my_result, result):
    if not isinstance(my_result, list):
        return False
    if len(my_result) != len(result):
        return False
    for index in range(len(result)):
        if my_result[index] != str(result[index]):
            return False
    return True

# Test Cases
test_cases = [ ([], []),
               (['+-*/', '', '***'], []),
               (['452'], [2]),
               (['00'], []),
               (['a9 $3 2#5'], [2]),
               (['4XT3(90)', '--453*&6', '64073'], [9, 3, 0]),
               (['3T7 2#9', 'Uo-!', '35-'], [2]) ]

# Counter is to record how many test cases are passed.
# Some test cases are given partial marks.
counter = 0.0

try:
    from q2b import get_all_third_digits

    tc_no = 1

    for (str_list, result) in test_cases:
    
        print()
        print("Test Case " + str(tc_no) + ":")
        tc_no += 1
        print_test_case(str_list)
        print("Expected: " + str(result))       
    
        try:
            my_result = get_all_third_digits(str_list)
            
            print("Actual  : " + str(my_result))
            
            if my_result == result:
                counter += 1.0
                print("passed")
            elif match_as_string(my_result, result):
                # Partially correct if the answers are strings.
                counter += 0.5
                print("partially passed")
            else:
                print("failed")
        except:
            print('Exception:', sys.exc_info())
            print("failed")
            
except:
    print('Exception:', sys.exc_info())

# There are in total 7 test cases.
# We allocate 3.5 marks for q2b.
my_marks = counter / 2

print("\nTotal marks: " + str(my_marks))