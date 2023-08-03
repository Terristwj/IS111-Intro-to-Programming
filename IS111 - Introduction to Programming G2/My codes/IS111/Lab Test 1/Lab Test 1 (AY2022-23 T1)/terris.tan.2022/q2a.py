# Name: Tan Wei Jun, Terris
# Email ID: terris.tan.2022@scis.smu.edu.sg

def trim_number(num1, num2):
    # Replace the code below with your implementation.
    string = str(num1)
    last_num = int(string[-1])


    if num2 < last_num:
        string = string[:-1] + str(num2)
    string = int(string)

    return string