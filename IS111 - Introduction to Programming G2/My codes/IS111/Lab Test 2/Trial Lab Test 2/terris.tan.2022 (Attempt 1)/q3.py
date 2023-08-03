# Name:
# Email ID:
def create_email_dict(email_list):
    # Modify the code below.
    school_list = []
    stud_email_list = []
    my_dict = {}

    # print(email_list)
    for email in email_list:
        cols = email.split("@")
        email_id = cols[0]
        domain = cols[1]

        # Student Email
        is_stud_email = False
        if email_id.split(".")[-1].isdigit():
            is_stud_email = True
        
        if is_stud_email:
            school = domain.split(".")[0]
            if school != "smu":
                school = domain.split(".")[0] + "-" + email_id.split(".")[-1]
                stud_email_list.append(email)
                if school not in school_list:
                    school_list.append(school)
        # print(email_id, domain, email_id.split(".")[-1])
        
    # print(stud_email_list)
    # print(school_list)

    for school in school_list:
        for email in stud_email_list:
            if school.split("-")[0] in email and school.split("-")[1] in email:
                if school not in my_dict:
                    my_dict[school] = [email]
                else:
                    my_dict[school].append(email)
    return my_dict
    

    
