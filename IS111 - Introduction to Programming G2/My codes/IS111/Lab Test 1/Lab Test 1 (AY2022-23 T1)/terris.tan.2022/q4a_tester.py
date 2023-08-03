import sys


def run_test():

    print('########## TESTING Q4a ##########')
    # Test Cases

    rect_1 = ('R1', -4, -3, 3, 2)
    rect_2 = ('R2', 5, 1, 1, 4)
    rect_3 = ('R3', 0, 0, 5, 1)
    rect_4 = ('R4', 0, -3, 7, 4)
    rect_5 = ('R5', -4, -1, 3, 2)
    rect_6 = ('R6', -4, -1, 3, 2)
    rect_7 = ('R7', -2, -2, 2, 5)
    rect_8 = ('R8', 4, -2, 1, 1)

    rect_list = [rect_1, rect_2, rect_3, rect_4,
                rect_5, rect_6, rect_7, rect_8]

    for i in range(1, 9):
        print('Rectangle ' + str(i) + ": " + str(rect_list[i-1]))


    # Non-overlapping cases:
    non_overlapping_test_cases = [(rect_1, rect_2), (rect_2, rect_3), 
                                (rect_1, rect_5), (rect_3, rect_7), 
                                (rect_3, rect_8),  (rect_4, rect_7)]


    # Overlapping cases:
    overlapping_test_cases = [(rect_1, rect_7), (rect_6, rect_7),
                            (rect_3, rect_4), (rect_4, rect_8),
                            (rect_5, rect_6), (rect_7, rect_5)]

    # ##########

    total_score = 0.0
    counter = 0
    # Store the unique values returned by the function calls.
    # If there is only one unique value (i.e., the function always
    # returns True or always returns False, then 0 mark is awarded.)
    unique_returned_values = []

    try:
        from q4a import is_overlapping

        for (rect_a, rect_b) in non_overlapping_test_cases:

            print('\nTest Case: ' + rect_a[0] + ' and ' + rect_b[0])

            try:
                result = is_overlapping(rect_a, rect_b)
                if result not in unique_returned_values:
                    unique_returned_values.append(result)

                print('Expected output: False', )
                print('Actual output  :', result)

                if result == False:
                    counter += 1
                    print(counter, "Test case ok")
                else:
                    print("Test case incorrect")

            except:
                print('Exception:', sys.exc_info())
        

        for (rect_a, rect_b) in overlapping_test_cases:

            print('\nTest Case: ' + rect_a[0] + ' and ' + rect_b[0])

            try:
                result = is_overlapping(rect_a, rect_b)
                if result not in unique_returned_values:
                    unique_returned_values.append(result)

                print('Expected output: True', )
                print('Actual output  :', result)

                if result == True:
                    counter += 1
                    print(counter, "Test case ok")
                else:
                    print("Test case incorrect")

            except:
                print('Exception:', sys.exc_info())
              
        
        if len(unique_returned_values) == 1:
            print("\nThe function always returns the same value. Reset the total marks to 0.0.")
            total_score = 0.0
            counter = 0
        
          
        #0.25 mark if 2 to 6 test cases are correct
        #0.75 mark if 7 to 11 test cases are correct
        #1.5 marks if all 12 test cases are correct

        # compute the score    
        if counter in (2,3,4,5,6):
            total_score = 0.25
        elif counter in (7,8,9,10,11):
            total_score = 0.75
        elif counter in (12,):
            total_score = 1.5
        

    except:
        print('Exception:', sys.exc_info())


    total_score = round(total_score, 2)

    print('\nTotal Marks: ' + str(total_score) + " out of 1.5")

    return (counter, total_score)

run_test()