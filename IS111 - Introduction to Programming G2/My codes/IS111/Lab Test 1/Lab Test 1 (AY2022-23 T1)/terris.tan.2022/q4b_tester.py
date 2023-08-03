import sys

def same_result(expected, actual):
    if not isinstance(actual, list):
        return False

    if len(expected) != len(actual):
        return False

    for pair in expected:
        if pair not in actual and (pair[1], pair[0]) not in actual:
            return False

    return True

def run_test():

    print('########## TESTING Q4b ##########')
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

    test_cases = [([rect_2, rect_3, rect_5, rect_7], [('R5', 'R7')], 0.25),
                ([rect_1, rect_2, rect_3, rect_4, rect_5, rect_6, rect_7, rect_8], 
                        [('R1', 'R7'), ('R3', 'R4'), ('R4', 'R8'),
                        ('R5', 'R6'), ('R5', 'R7'), ('R6', 'R7')], 0.75)]

    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q4b import find_overlapping_pairs
        
        for (rect_list, expected_result, score) in test_cases:

            print('\nTest Case: rectangles', end='')
            for rect in rect_list:
                print(' ' + rect[0], end='')
            print()

            try:
                result = find_overlapping_pairs(rect_list)

                print('Expected output:', expected_result)
                print('Actual output  :', result)

                if (same_result(expected_result, result)):
                    total_score += score
                    counter += 1
                    print(counter, "Test case ok")
                    print("+" + str(score) + "/" + str(score) + " marks")
                else:
                    print("+0.0/" + str(score) + " marks")
                    print("Test case incorrect")

            except:
                print('Exception:', sys.exc_info())


    except:
        print('Exception:', sys.exc_info())


    total_score = round(total_score, 2)

    print('\nTotal Marks: ' + str(total_score) + " out of 1.0")

    return (counter, total_score)

run_test()