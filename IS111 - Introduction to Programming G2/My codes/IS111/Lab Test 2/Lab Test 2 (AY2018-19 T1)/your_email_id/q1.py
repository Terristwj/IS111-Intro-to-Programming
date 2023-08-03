#
# Name: 
# Email ID: 
#
def count_names_with_space(name_list):
    # Modify the code below
    count = 0
    for name in name_list:
        if ' ' in name:
            count += 1
    return count
