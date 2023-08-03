# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg

def shift_string(orig_str):
    # Replace the code below with your implementation.
    str_list = []
    for ch in orig_str:
        pos = orig_str.find(ch)
        # print(pos)
        if pos > 0:
            new_string = orig_str[pos:] + orig_str[0:pos]
        else:
            new_string = orig_str[pos:]
        str_list.append(new_string)
    return str_list