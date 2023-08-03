import sys

def round_gpas(gpa_dict):
    d = {}
    for key in gpa_dict:
        gpa = gpa_dict[key]
        rounded_gpa = (gpa[0], round(gpa[1],1))
        d[key] = rounded_gpa
    return d

def run_test():
    print('########## TESTING Q3b ##########')
    # Test Cases
    test_cases = [
                # easy test case 1
                (('course_score_1.txt',  (2016, 1), (2017,1)), {'Andy': (2, 3.1), 'Bob': (2, 3.4), 'Carrie': (2, 2.8), 'David': (1, 4.0)}, 0.5 ),

                (('course_score_1.txt',(2016,2),(2017,2)), {'Andy': (1, 3.0), 'Bob': (2, 2.9), 'Carrie': (2, 2.8), 'David': (1, 4.0)}, 0.5),

                (('course_score_1.txt',(2017,2),(2018,1)), {'Andy': (1, 3.3), 'Bob': (1, 2.2), 'Carrie': (1, 2.3), 'David': (2, 3.8)}, 0.5),

                (('course_score_1.txt',(2016,1),(2018,2)), {'Andy': (3, 3.2), 'Bob': (4, 3.3), 'Carrie': (3, 2.6), 'David': (3, 3.8)}, 0.5),

                (('course_score_2.txt',(2018,1),(2020,2)), {'stu1': (4, 3.2), 'stu2': (4, 3.5), 'stu3': (4, 3.0), 'stu4': (5, 3.3), 'stu5': (3, 3.5)}, 0.5),

                (('course_score_2.txt',(2016,2),(2019,1)), {'stu1': (2, 3.3), 'stu2': (2, 3.4), 'stu3': (2, 2.8), 'stu4': (4, 3.4), 'stu5': (1, 3.4)}, 0.5),

                (('course_score_2.txt',(2018,2),(2020,1)), {'stu1': (2, 2.7), 'stu2': (2, 3.4), 'stu3': (2, 3.0), 'stu4': (3, 3.5), 'stu5': (1, 3.7)}, 0.5),

                # easy test case 2
                (('course_score_2.txt',(2020,2),(2020,2)), {'stu1': (1, 3.6), 'stu2': (2, 3.7), 'stu3': (1, 3.1), 'stu4': (1, 2.9), 'stu5': (1, 3.3)}, 0.5)
                ]
    # ##########

    total_score = 0.0
    counter = 0

    try:
        from q3b import calculate_student_gpa
        
        for (input_tuple, expected_result, score) in test_cases:

            print('\nTest Case: calculate_student_gpa', input_tuple)
            

            filename = input_tuple[0]
            start_term = input_tuple[1]
            end_term = input_tuple[2]

            try:
                result = calculate_student_gpa(filename, start_term, end_term)

                print("Expected output: " , expected_result)
                print("Actual output  : " , result)

                if result == expected_result:
                    total_score += score
                    counter += 1
                    print("+" + str(score) + "/" + str(score) + " marks")
                elif round_gpas(result) == expected_result:
                    total_score += score/2
                    counter += 0.5
                    print("+" + str(score/2) + "/" + str(score) + " marks, as GPA values were not rounded properly.")

                else:
                    print("+0.0/" + str(score) + " marks")

            except:
                print('Exception:', sys.exc_info())
                
    except:
        print('Exception:', sys.exc_info())
    
    total_score = round(total_score, 2)
    print('\nTotal Marks: ' + str(total_score) + " out of 4.0")
   
    return (counter, total_score)

if __name__ == "__main__":
    run_test()