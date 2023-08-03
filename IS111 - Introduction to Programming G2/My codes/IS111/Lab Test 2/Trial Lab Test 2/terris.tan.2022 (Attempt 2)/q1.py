# Name:
# Email ID:
def get_ppl_with_fever(ppl_list):

    # Modify the code below.
    limit = 37.5
    sick_people = []
    for person in ppl_list:
        avg = 0
        for temp in person[1]:
            avg += temp
        avg = avg / len(person[1])
        
        if avg > limit:
            sick_people.append(person[0])
    return sick_people

