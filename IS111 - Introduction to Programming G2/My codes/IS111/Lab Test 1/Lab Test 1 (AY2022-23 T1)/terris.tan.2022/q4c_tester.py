import sys


def run_test():
        
    print('########## TESTING Q4c ##########')
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

    test_cases = [(rect_7, rect_1, 1, 0.25), (rect_7, rect_5, 2, 0.25), 
                (rect_1, rect_2, 0, 0.25), (rect_3, rect_2, 0, 0.25),
                (rect_4, rect_3, 5, 0.25), (rect_6, rect_5, 6, 0.25),
                (rect_8, rect_4, 1, 0.25), (rect_6, rect_1, 0, 0.25),
                (rect_3, rect_8, 0, 0.25), (rect_3, rect_7, 0, 0.25)]

    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q4c import find_overlap_size

        # If the function always returns the same value, then 0 mark is awarded.
        same_value = []
        
        for (rect_a, rect_b, expected_size, score) in test_cases:

            print('\nTest Case: rectangles', rect_a[0], rect_b[0])

            try:
                size = find_overlap_size(rect_a, rect_b)
                if size not in same_value:
                    same_value.append(size)
        
                print('Expected output:', expected_size)
                print('Actual output  :', size)

                if size == expected_size:
                    counter += 1
                    print(counter, "Test case ok")
                else:
                    print("Test case incorrect")

            except:
                print('Exception:', sys.exc_info())

        if len(same_value) == 1:
            print('\nThe function always returns the same value. Reset total marks to 0.0.')
            total_score = 0.0
            counter = 0
        
        # compute the score - must pass all test cases!!!
        if counter == 10:
            total_score = 2.5
        else:
            total_score = 0  
     

    except:
        print('Exception:', sys.exc_info())


    total_score = round(total_score, 2)

    print('\nTotal Marks: ' + str(total_score) + " out of 2.5")

    return (counter, total_score)

run_test()