import sys

def convert_list(lst):
    return [int(e) for e in lst]

def run_test():
    print('########## TESTING Q2a ##########')
    
    # Test Cases
    test_cases = [(('sample2.txt', 2), [101, 31], 0.5),
                (('sample2.txt', 100), [101, 31, 1811, 33, 5567, 4663], 0.5),
                (('sample2.txt', 1), [101], 0.5),
                (('sample2.txt', 0), [], 0.5),
                (('sample2.txt', 5), [101, 31, 1811, 33, 5567], 0.5),
                (('sample2.txt', 6), [101, 31, 1811, 33, 5567, 4663], 0.5)
                ]
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q2a import get_n_odd_numbers

        for (params, expected_result, score) in test_cases:

            print("\nTest Case: get_n_odd_numbers('" + str(params[0]) + "', " + str(params[1]) + ")")

            try:
                result = get_n_odd_numbers(params[0], params[1])

                print('Expected output:', expected_result)
                print('Actual output  :', result)

                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score) + " marks")
                elif convert_list(result) == expected_result:
                    total_score += score/2
                    counter += 0.5
                    print("+" + str(score/2) + "/" + str(score) + " marks, as the returned list does not contain the correct data type.")
                else:
                    print("+0.0/" + str(score) + " marks")

            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())


    total_score = round(total_score, 2)
    print('\nTotal Marks: ' + str(total_score) + " out of 3.0")

    return (counter, total_score)

if __name__ == "__main__":
    run_test()