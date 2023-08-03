# Name:
# Email ID:    
def calculate_term_gpa(term_grades, mapping):
    # Write your code here.
    if len(term_grades) != 1:
        # Get non_special grades
        non_special_grades = []
        for grade_map in mapping:
            if len(grade_map) == 1 and grade_map not in non_special_grades:
                non_special_grades.append(grade_map)
        # print(non_special_grades)

        counter = 0
        term_gpa = 0
        for i in range(len(term_grades)):
            if term_grades[i] not in non_special_grades:
                continue
            try:
                if term_grades[i+1] in non_special_grades:
                    term_gpa += mapping[term_grades[i]]
                    counter += 1
                else:
                    term_gpa += mapping[term_grades[i] + term_grades[i+1]]
                    counter += 1
            except:
                term_gpa += mapping[term_grades[i]]
                counter += 1
        term_gpa /= counter
    else:
        term_gpa = mapping[term_grades[0]]
    return term_gpa

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    print(f"Test {tc_num} : calculate_term_gpa('ACAC', {{'A':4, 'B':3, 'C':2, 'F':0}})")
    result = calculate_term_gpa('ACAC', {'A': 4, 'B': 3, 'C': 2, 'F': 0})
    print("Expected : 3.0")
    print(f"Actual   : {result}")
    print()

    print("Expected return type : <class 'float'>")
    print(f"Actual return type   : {type(result)}")  

    tc_num += 1
    print('-' * 40)
    
    print(f'''Test {tc_num}: calculate_term_gpa('A+AA-',
            {{'A+':4.3, 'A':4, 'A-':3.7, 'B+':3.3, 'B':3.0, 'B-':2.7,
            "'C+':2.3,'C':2.0, 'C-':1.7, 'D+':1.3, 'D':1.0, 'F':0}})''')
    result = calculate_term_gpa('A+AA-',
                                {'A+': 4.3, 'A': 4, 'A-': 3.7, 'B+': 3.3, 'B': 3.0, 'B-': 2.7,
                                 'C+': 2.3, 'C': 2.0, 'C-': 1.7, 'D+': 1.3, 'D': 1.0, 'F': 0})
    print("Expected:4.0")
    print(f"Actual  :{result}")
    print()

    tc_num += 1
    print('-' * 40)
    
    print(f"Test {tc_num}:calculate_term_gpa('A*AA',{{'A*':4, 'A':3.5, 'B*':3, 'B':2.5, 'C':2, 'F':0}})")
    result = calculate_term_gpa('A*AA',
                                {'A*': 4, 'A': 3.5, 'B*': 3, 'B': 2.5, 'C': 2, 'F': 0})
    print("Expected:3.6666666666666665")
    print(f"Actual  :{result}")
    print()
