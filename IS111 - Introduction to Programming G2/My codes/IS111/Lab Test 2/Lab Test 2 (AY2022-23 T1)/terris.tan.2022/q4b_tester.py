import sys

def run_test():

    print('########## TESTING Q4b ##########')
    # Test Cases
    test_cases = [((['the', 'one', 'ring', 's'], 'theoneringis', 1), [[0,1,2],[3,4,5], [6,7,8,9], [11]],0.75), # step 1
                # step 2
                ((['star', 'wars', 'luke', 'sky', 'walker'], 'wwarrrslukettttarrrskyywwaallkkeersr', 2), [[6, 11, 15, 17], [0, 2, 4, 6], [], [6, 9, 21], [0, 2, 7, 9, 31, 33]], 0.75),
                # step 3
                ((['y', 'nope', 'nope', 'ne', 'z'], 'nnnnoooopnnnne', 3), [[], [0, 4, 8, 13], [0, 4, 8, 13], [0, 13], []], 0.75),
                # big step
                ((['y', 'nope', 'nope', 'ne', 'z'], 'nnnnoooopnnnne', 13), [[], [], [], [0, 13], []], 0.75),]

    # ##########
    
    total_score = 0.0
    counter = 0
    
    try:
        from q4b import find_words

        for (params, expected_result, score) in test_cases:
            
            print("\nTest Case: find_words" + str(params))

            try:
                result = find_words(params[0], params[1], params[2])

                print("Expected output: " , expected_result)
                print("Actual output  : " , result)

                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score) + " marks")
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