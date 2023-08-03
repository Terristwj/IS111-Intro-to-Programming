# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg
from q2a import trim_number

def trim_number_with_list(num, num_list):
    # Replace the code below with your implementation.
    for number in num_list:
        # print(num, number)
        # print(trim_number(num, number))
        new_num = trim_number(num, number)
        # print(new_num, num)
        if new_num < num:
            return new_num
        
    return num