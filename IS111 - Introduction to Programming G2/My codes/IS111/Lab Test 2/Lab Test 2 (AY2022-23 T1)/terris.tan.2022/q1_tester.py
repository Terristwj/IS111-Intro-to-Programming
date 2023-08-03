import sys

def run_test():
    print('########## TESTING Q1 ##########')
    # Counter is to record how many test cases are passed.
    # Some test cases are given partial marks.
    counter = 0.0
    # Test Cases
    test_cases = [(('abc', 3, 51), True, 1),
                (('apple', 5, 3), False, 1),
                (('news', 0, 0), False, 1),
                (('', 0, 1), True, 1),
                (('!@#%%#', 5, 5), False, 1),
                (('', 0, 0), False, 1),
                (('1234567890', 10, 11), True, 1)
                ]
    
    # ##########

    total_score = 0.0
    # Store the unique values returned by the function calls.
    # If there is only one unique value (i.e., the function always
    # returns True or always returns False, then 0 mark is awarded.)
    unique_returned_values = []


    try:
        from q1 import check_record

        for (record, expected_result, score) in test_cases:

            print("\nTest Case: check_record(" + str(record) + ")")

            try:
                result = check_record(record)

                if result not in unique_returned_values:
                    unique_returned_values.append(result)

                print('Expected output:', expected_result)
                print('Actual output  :', result)

                if result == expected_result:
                    counter += 1
                    total_score += score
                    print("+" + str(score) + "/" + str(score)
                            + " marks")
                elif str(result).lower() == str(expected_result).lower():
                    total_score += round(score/2, 2)
                    counter += 0.5
                    print("+" + str(round(score/2, 2)) + "/" + str(score)
                              + " marks, as the returned data type is not correct.")

                else:
                    print("+0.0/" + str(score) + " marks")

            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    if len(unique_returned_values) == 1:
        print("\nThe function always returns the same value. Reset the total marks to 0.0.")
        total_score = 0.0
        counter = 0

    total_score = round(total_score, 2)
    print('\nTotal Marks: ' + str(total_score) + " out of 7.0")
    
    return (counter, total_score)

if __name__ == "__main__":
    run_test()