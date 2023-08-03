# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg

def construct_string(orig_str, len_list, cnct_list):
    # Replace the code below with your implementation.
    if not orig_str:
        return ""
    my_string = orig_str
    my_list = []
    for length in len_list:
        new_string = my_string[0:length]
        my_string = my_string[length:]
        my_list.append(new_string)
    
    print(my_list)
    final_str = my_list[0]
    for i in range(len(my_list)-1):
        final_str += cnct_list[i] + my_list[i+1]
        
    return final_str