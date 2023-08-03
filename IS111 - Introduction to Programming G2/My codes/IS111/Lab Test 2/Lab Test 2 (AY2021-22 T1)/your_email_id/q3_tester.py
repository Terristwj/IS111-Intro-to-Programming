import sys

def run_test():
    print('########## TESTING Q3 ##########')
    # Test Cases
    test_cases = [('record4.txt', '30/11/2021', {'G1': (44, False), 'G6': (12, False), 'G5': (11, False), 'F2': (12, False), 'S11': (12, True), 'S3': (60, True)}),
                ('record4.txt', '26/11/2021', {'G1': (44, False), 'G6': (12, False), 'G5': (11, False), 'F2': (12, False), 'S11': (12, True), 'S3': (60, True)}),
                ('record4.txt', '19/07/2021', {'G1': (44, False), 'G6': (12, False), 'S3': (60, False), 'G5': (11, False), 'F2': (12, False), 'S11': (12, True)}),
                ('record4.txt', '25/11/2021', {'G1': (44, False), 'G6': (12, False), 'G5': (11, False), 'F2': (12, False), 'S11': (12, True), 'S3': (60, False)}),
                ('record5.txt', '28/11/2021', {'S2': (22, True), 'S21': (23, True), 'S22': (24, False), 'G12': (12, True), 'G14': (28, True), 'G13': (18, False), 'F3': (60, False)}),
                ('record5.txt', '21/11/2021', {'S2': (22, True), 'S21': (23, True), 'S22': (24, False), 'G12': (12, True), 'G14': (28, True), 'G13': (18, False), 'F3': (60, False)}),
                ('record5.txt', '22/11/2021', {'S2': (22, True), 'S21': (23, True), 'S22': (24, False), 'G12': (12, True), 'G14': (28, True), 'G13': (18, False), 'F3': (60, False)}),
                ('record5.txt', '20/11/2021', {'S2': (22, True), 'S21': (23, True), 'S22': (24, False), 'G12': (12, False), 'G14': (28, True), 'G13': (18, False), 'F3': (60, False)}),
                ('record6.txt', '2/08/2021', {'G1': (4, False), 'S1': (10, False), 'S5': (11, False), 'S2': (1, False)}),
                ('record7.txt', '05/10/2021', {'S2': (55, False), 'S4': (62, False), 'S8': (18, False)})
                ]

    # Counter is to record how many test cases are passed.
    counter = 0
    marks = 0.0

    try:
        from q3 import get_vaccination_status

        for (filename, today, result) in test_cases:
            try:
                my_result = get_vaccination_status(filename, today)
                if my_result == result:
                    counter += 1
                else:
                    print(f'Test case failed: get_vaccination_status("{filename}", {today})')
                    print(f'Expected: {result}')
                    print(f'Actual: {my_result}')
                    print()
            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())

    # There are in total 10 test cases.
    # We allocate 5 marks for q3.
    marks = counter/2
    return (counter, marks)

if __name__ == "__main__":
    counter, marks = run_test()
    print(f'Number of test cases passed: {counter}')
    print(f'Marks awarded: {marks}')