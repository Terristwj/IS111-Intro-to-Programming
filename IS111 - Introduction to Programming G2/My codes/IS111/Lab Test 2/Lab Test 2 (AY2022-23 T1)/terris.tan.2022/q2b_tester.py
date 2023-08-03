import sys


def run_test():
    print('########## TESTING Q2b ##########')
    # Test Cases
    test_cases = [(('w_sample2.txt', 'e'), ['chocolate', 'phone'], 0.5),
                (('w_sample2.txt', 'r'), ['car', 'par', 'temper', 'wonder', 'par'], 0.5),
                (('w_sample2.txt', 'm'), ['arm', 'form', 'museum', 'foam', 'cam', 'alarm', 'atom', 'beam'], 0.5),
                (('w_sample2.txt', 'a'), ['dia', 'sea'], 0.5),
                (('w_sample2.txt', 's'), ['famous'], 0.5),
                (('w_sample2.txt', 'd'), [], 0.5)]
                
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q2b import filter_words

        for (params, expected_result, score) in test_cases:

            list_num_string = ''
            for i in params[1]:
                list_num_string = list_num_string+", "+str(i)

            print("\nTest Case: filter_words('" + params[0] + "', '" + params[1] + "')")

            try:
                result = filter_words(params[0], params[1])

                print('Expected output:', expected_result)
                print('Actual output  :', result)

                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score)
                            + " marks")
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