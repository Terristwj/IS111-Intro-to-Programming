# Name:
# Email ID:

def check_seating_arrangement(arrangement, must_list, cannot_list):
    # Modify the code below.
    must_valid = []
    for set in must_list:
        set_string = set[0] + set[1] + "," + set[1] + set[0]
        check = False
        for i in range(len(arrangement)):
            if i != len(arrangement)-1:
                # print(arrangement[i] + arrangement[i+1], set_string)
                if arrangement[i] + arrangement[i+1] in set_string:
                    check = True
            else:
                # print(arrangement[i] + arrangement[0], set_string)
                if arrangement[i] + arrangement[0] in set_string:
                    check = True
        for i in range(len(arrangement)-1,-1):
            if i != 0:
                # print(arrangement[i] + arrangement[i-1], set_string)
                if arrangement[i] + arrangement[i-1] in set_string:
                    check = True
            else:
                # print(arrangement[i] + arrangement[-1], set_string)
                if arrangement[i] + arrangement[-1] in set_string:
                    check = True
        must_valid.append(check)

    for set in cannot_list:
        set_string = set[0] + set[1] + "," + set[1] + set[0]
        check = True
        for i in range(len(arrangement)):
            if i != len(arrangement)-1:
                if arrangement[i] + arrangement[i+1] in set_string:
                    check = False
            else:
                if arrangement[i] + arrangement[0] in set_string:
                    check = False
        for i in range(len(arrangement)-1,-1):
            if i != 0:
                if arrangement[i] + arrangement[i-1] in set_string:
                    check = False
            else:
                if arrangement[i] + arrangement[-1] in set_string:
                    check = False
        must_valid.append(check)

    # print(must_valid)
    for set in must_valid:
        if not set:
            return False
    return True
 