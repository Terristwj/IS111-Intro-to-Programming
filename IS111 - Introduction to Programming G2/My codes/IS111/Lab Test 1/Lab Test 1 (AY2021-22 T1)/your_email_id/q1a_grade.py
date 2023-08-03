import sys

def print_test_case(w1, h1, w2, h2):
    print("\tget_area_difference(" + str(w1) + ", " + str(h1) + ", " + str(w2) + ", " + str(h2) + ")")

# Test Cases
test_cases = [  (3, 3, 2, 2, 5), 
                (10, 2, 6, 3, 2), 
                (1, 5, 3, 2, 1),
                (4, 9, 5, 10, 14),
                (15, 2, 10, 3, 0),
                (5, 7, 7, 5, 0) ]

# Counter is to record how many test cases are passed.
# Some test cases are given partial marks.
counter = 0.0

try:
    from q1a import get_area_difference

    # Test case 1: Check whether the returned value's type is correct.
    try:
        (w1, h1, w2, h2, result) = test_cases[0]
        
        print("Test Case 1: check the data type of the returned value")
        print_test_case(w1, h1, w2, h2)
        print("Expected: <class 'int'>")
        
        my_result = get_area_difference(w1, h1, w2, h2)
        
        print("Actual  : " + str(type(my_result)))
        
        if isinstance(my_result, int):
            counter += 1.0
            print("passed")
        else:
            print("failed")
    except:
        print('Exception:', sys.exc_info())
        print("failed")

    # Other test cases:
    tc_no = 2
    for (w1, h1, w2, h2, result) in test_cases:
    
        print()
        print("Test Case " + str(tc_no) + ":")
        print_test_case(w1, h1, w2, h2)
        print("Expected: " + str(result))
    
        try:
            my_result = get_area_difference(w1, h1, w2, h2)
            print("Actual  : " + str(my_result))
            
            if my_result == result:
                counter += 1.0
                print("passed")
            elif my_result == -result or int(my_result) == result:
                # Partially correct if the answers are negative values, or the
                # answers are of other types.
                counter += 0.5
                print("partially passed")
            else:
                print("failed")
                
        except:
            print('Exception:', sys.exc_info())
            print("failed")
        
        tc_no += 1
            
except:
    print('Exception:', sys.exc_info())

# There are in total 7 test cases.
# We allocate 3.5 marks for q1a.
my_marks = counter / 2

print("\nTotal marks: " + str(my_marks))