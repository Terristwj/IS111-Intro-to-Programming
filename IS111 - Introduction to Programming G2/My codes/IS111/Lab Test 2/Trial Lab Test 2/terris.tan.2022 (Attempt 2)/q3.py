# Name:
# Email ID:
def create_email_dict(email_list):
    # Modify the code below.
    student_emails = []
    for email in email_list:
        front = email.split("@")[0]
        last_part = front.split(".")[-1]

        # Check if is student email
        if last_part.isdigit():
            back = email.split("@")[1]
            front_part = back.split(".")[0]

            # Checks if stud_email contains school
            if front_part != "smu":
                student_emails.append(email)

    # print(email_list)
    # print(student_emails)

    my_dict = {}
    for email in student_emails:
        front = email.split("@")[0]
        year = front.split(".")[-1]

        back = email.split("@")[1]
        school = back.split(".")[0]

        school_year = school+"-"+year
        if school_year not in my_dict:
            my_dict[school_year] = [email]
        else:
            my_dict[school_year].append(email)
    
    return my_dict
    

    
