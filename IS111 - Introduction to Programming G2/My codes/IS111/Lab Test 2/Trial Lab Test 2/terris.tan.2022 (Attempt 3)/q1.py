# Name:
# Email ID:
def get_ppl_with_fever(ppl_list):
    # Modify the code below.
    sick_people = []
    if ppl_list:
        for person in ppl_list:
            avg_temp = 0
            for temp in person[1]:
                avg_temp += temp
            avg_temp /= len(person[1])
            if avg_temp > 37.5:
                sick_people.append(person[0])
    return sick_people

