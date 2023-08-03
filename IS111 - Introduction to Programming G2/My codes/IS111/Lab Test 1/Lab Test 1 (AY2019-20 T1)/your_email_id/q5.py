# Name:
# Email ID:

def transform(str1, str2):
    # Modify the code below.
    my_list = []
    string = str1
    my_list.append(str1)

    for i2 in range(len(str2)):
        for i in range(len(str1)):
            if string[i] != str2[i2]:
                cur_i = string.find(str2[i2])
                while cur_i != str2.find(str2[i2]):
                    string = string[:cur_i-1] + string[cur_i] + string[cur_i-1] + string[cur_i+1:]
                    my_list.append(string)
                    cur_i = string.find(str2[i2])
                    # print(my_list)
                    # print(my_list[-1])
                    if my_list[-1] == str2:
                        return my_list
    return my_list
        
    