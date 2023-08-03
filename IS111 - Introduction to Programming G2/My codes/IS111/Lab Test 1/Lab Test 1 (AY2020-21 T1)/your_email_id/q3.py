# Name:
# Email ID:

from re import A


def check_math(list_of_equations):
    # Replace the code below with your implementation.
    if list_of_equations:
        all_checker = []
        for eqn in list_of_equations:
            optr_list = []
            eqn = eqn.replace(" ", "")
            for i in range(len(eqn)):
                if not eqn[i].isnumeric():
                    if eqn[i] == "/":
                        if eqn[i] == eqn[i+1]:
                            optr_list.append("//")
                        elif eqn[i] != eqn[i-1]:
                            optr_list.append(eqn[i])
                    else:
                        optr_list.append(eqn[i])
            # print(optr_list)
            num_list = []
            for string in eqn.split(optr_list[0]):
                if "=" in string:
                    for string2 in string.split("="):
                        num_list.append(int(string2))
                else:
                    num_list.append(int(string))
            
            # print(num_list)
            if optr_list[0] == "+":
                if num_list[0] + num_list[1] == num_list[2]:
                    all_checker.append(True)
                else:
                    all_checker.append(False)
            elif optr_list[0] == "-":
                if num_list[0] - num_list[1] == num_list[2]:
                    all_checker.append(True)
                else:
                    all_checker.append(False)
            elif optr_list[0] == "*":
                if num_list[0] * num_list[1] == num_list[2]:
                    all_checker.append(True)
                else:
                    all_checker.append(False)
            elif optr_list[0] == "//":
                if num_list[0] // num_list[1] == num_list[2]:
                    all_checker.append(True)
                else:
                    all_checker.append(False)
            elif optr_list[0] == "/":
                if num_list[0] / num_list[1] == num_list[2]:
                    all_checker.append(True)
                else:
                    all_checker.append(False)
            elif optr_list[0] == "%":
                if num_list[0] % num_list[1] == num_list[2]:
                    all_checker.append(True)
                else:
                    all_checker.append(False)
            else:
                all_checker.append(False)
        # print(all_checker)

        if False in all_checker:
            return False
    return True