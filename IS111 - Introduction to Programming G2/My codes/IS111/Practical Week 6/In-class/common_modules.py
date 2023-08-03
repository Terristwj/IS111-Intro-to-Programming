# Name: 
# Email ID:

def check_common_modules(student_list):
    for i in range(len(student_list)):
        student_name = student_list[i][0]
        student_compared = ""
        for module in student_list[i]:
            if module in student_list[i+1][1]:
                i += 1
                student_compared = student_list[i+1][0]

            

    # Modify the code below
    return None