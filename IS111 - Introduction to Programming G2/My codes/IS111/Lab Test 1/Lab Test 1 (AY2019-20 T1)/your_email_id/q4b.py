# Name:
# Email ID:

import itertools
import q4a

def get_seating_arrangement(female_list, male_list, must_list, cannot_list):
    # Modify the code below.
    new_list = []
    for item in female_list:
        new_list.append(item)
    for item in male_list:
        new_list.append(item)
    my_permutations = list(itertools.permutations(new_list))
    for perm in my_permutations:
        print(perm)
        if q4a.check_seating_arrangement(perm, must_list, cannot_list):
            return perm
    return None