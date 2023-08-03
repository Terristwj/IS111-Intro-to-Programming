# Name:
# Email ID:

from q3a import read_courses

def calculate_student_gpa(filename, start_term, end_term):
    # Replace the code below with your implementation.
    stud_scores = read_courses(filename)
    # print(stud_scores)
    my_dict = {}
    for name in stud_scores:
        # (year, term)
        total_gpa_score = 0
        credit_counter = 0
        subject_counter = 0
        for subject in stud_scores[name]:
            gpa_score = subject[3] * subject[4]

            start_year = start_term[0]
            start_term_num = start_term[1]

            end_year = end_term[0]
            end_term_num = end_term[1]
            # print(name, gpa_score)
            # print(start_year, subject[1], start_term_num , subject[2])
            # print(end_year, subject[1], end_term_num , subject[2])
            if (subject[1] == start_year and subject[2] >= start_term_num) or subject[1] >= start_year:
                if (subject[1] == end_year and subject[2] <= end_term_num) or subject[1] <= end_year:
                    total_gpa_score += gpa_score
                    credit_counter += 1 * subject[3]
                    subject_counter += 1
        if total_gpa_score > 0:
            final_gpa = round(total_gpa_score/credit_counter, 1)
            my_dict[name] = (subject_counter, final_gpa)
                    
    return my_dict 

