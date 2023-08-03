# Name:
# Email ID:
def get_ppl_with_fever(ppl_list):
    
    # Modify the code below.
    name_list = []
    for person_temps in ppl_list:
        avg_temp = 0
        for temp in person_temps[1]:
            avg_temp += temp
        avg_temp = avg_temp / len(person_temps[1])

        if avg_temp > 37.5:
            name_list.append(person_temps[0])

    return name_list

