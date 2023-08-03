# Name:
# Email ID:
def create_email_dict(email_list):
    # Modify the code below.
    my_dict = {}
    if email_list:
        for email in email_list:
            cols = email.split('@')
            email_id = cols[0]
            email_domain = cols[1]

            year = email_id.split('.')[-1]
            school = email_domain.split('.')[0]

            if year.isnumeric():
                if school != 'smu':
                    sch_yr = school + "-" + year
                    if sch_yr not in my_dict:
                        my_dict[sch_yr] = []
                    if email not in my_dict[sch_yr]:
                        my_dict[sch_yr].append(email)
    return my_dict
    

    
