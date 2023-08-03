import sys

def is_two_dicts_of_list_of_tuples_equal(dict1, dict2):
    if sorted(dict1) != sorted(dict2):
        return False
    
    for key in dict1:
        course_list1 = dict1[key]
        course_list2 = dict2[key]

        if sorted(course_list1) != sorted(course_list2):
            return False
    
    return True

def convert_dict(input_dict):
    d = {}
    for key in input_dict:
        d[key] = []
        value = input_dict[key]
        for tup in value:
            d[key].append((tup[0], int(tup[1]), int(tup[2]), int(tup[3]), float(tup[4])))
    return d


def run_test():
    print('########## TESTING Q3a ##########')
    # Test Cases
    test_cases = [
        ('course_score_1.txt', 
            {'Andy': [('IS100', 2016, 1, 1, 3.6), ('IS300', 2017, 1, 3, 3.0), ('IS600', 2018, 1, 6, 3.3)], 'Bob': [('IS200', 2016, 1, 2, 2.9), ('IS200', 2016, 2, 2, 3.9), ('IS300', 2017, 2, 3, 2.2), ('IS600', 2018, 2, 6, 3.7)], 'Carrie': [('IS200', 2016, 2, 2, 2.4), ('IS300', 2017, 1, 3, 3.1), ('IS500', 2018, 1, 5, 2.3)], 'David': [('IS100', 2016, 1, 1, 4.0), ('IS400', 2017, 2, 4, 4.0), ('IS500', 2018, 1, 5, 3.6)]},
            1.5),

        ('course_score_2.txt', 
            {'stu1': [('C1', 2020, 2, 1, 3.6), ('C2', 2019, 2, 2, 2.8), ('C3', 2018, 2, 3, 2.7), ('C4', 2018, 1, 4, 3.7)], 'stu2': [('C1', 2020, 2, 1, 4.0), ('C3', 2020, 2, 3, 3.6), ('C2', 2019, 1, 2, 3.1), ('C4', 2018, 2, 4, 3.6)], 'stu3': [('C4', 2020, 2, 4, 3.1), ('C3', 2019, 2, 3, 3.0), ('C2', 2018, 2, 2, 2.9), ('C1', 2018, 1, 1, 2.6)], 'stu4': [('C3', 2020, 2, 3, 2.9), ('C1', 2019, 1, 1, 2.2), ('C2', 2018, 2, 2, 4.0), ('C4', 2018, 2, 4, 3.5), ('C5', 2018, 1, 3, 3.4)], 'stu5': [('C3', 2020, 2, 3, 3.3), ('C4', 2019, 2, 4, 3.7), ('C5', 2018, 1, 3, 3.4)]},
            1.5)
        ]
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q3a import read_courses

        for (filename, expected_result, score) in test_cases:

            print("\nTest Case: read_courses('" + filename + "')")

            try:
                result = read_courses(filename)

                print('Expected output:', expected_result)
                print('Actual output  :', result)

                if is_two_dicts_of_list_of_tuples_equal(result, expected_result):
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score)  + " marks")
                elif is_two_dicts_of_list_of_tuples_equal(convert_dict(result), expected_result):
                    total_score += score/2
                    counter += 0.5
                    print("+" + str(score/2) + "/" + str(score) + " marks, as the return dict does not contain the correct data types.")
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

