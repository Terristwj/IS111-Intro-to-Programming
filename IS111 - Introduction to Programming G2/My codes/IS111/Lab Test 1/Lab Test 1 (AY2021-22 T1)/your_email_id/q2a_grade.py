import sys

def print_test_case(number):
    print("\tget_right_most_even_digit(" + str(number) + ")")


# Test Cases
test_cases = [ (8, 8), (132, 2), 
               (569, 6), (457, 4),
               (2094, 4), (4903, 0),
               (39531, None)]

# Counter is to record how many test cases are passed.
# Some test cases are given partial marks.
counter = 0.0
# If the code returns the value in a wrong type,
# we will give some penalty.
wrong_type = False

try:
    from q2a import get_right_most_even_digit

    tc_no = 1

    for (number, result) in test_cases:
    
        print()
        print("Test Case " + str(tc_no) + ":")
        tc_no += 1
        print_test_case(number)
        print("Expected: " + str(result))        
    
    
        try:
            my_result = get_right_most_even_digit(number)
            
            print("Actual  : " + str(my_result))
            
            if my_result == result:
                counter += 1.0
                print("passed")
            elif my_result == str(result):
                # Partially correct if the answers are strings.
                counter += 1.0
                wrong_type = True
                print("partially passed because the data type of the returned value is " + str(type(my_result)))
            else:
                print("failed")
        except:
            print('Exception:', sys.exc_info())
            print("failed")
            
except:
    print('Exception:', sys.exc_info())

# There are in total 7 test cases.
# We allocate 3.5 marks for q2a.
my_marks = counter / 2

if wrong_type:
    if my_marks >= 2.0:
        my_marks -= 0.75
    elif my_marks >= 1.0:
        my_marks -= 0.5
    else:
        my_marks -= 0.25

print("\nTotal marks: " + str(my_marks))