# Name: 
# Email ID:

# Ver 1
# def add_first_odd_digits(str_list):
#     sum = 0
#     if str_list:
#         for string in str_list:
#             # print(string)
#             num = get_first_odd(string)
#             sum += num
#     return sum

# def get_first_odd(string):
#     for ch in string:
#         if ch.isnumeric():
#             if int(ch) % 2 != 0:
#                 return int(ch)
#     return 0

# Ver 2
# def add_first_odd_digits(str_list):
#     sum = 0
#     if str_list:
#         for string in str_list:
#             # print(string)
#             num_string = ""
#             for ch in string:
#                 if ch.isnumeric():
#                     if int(ch) % 2 != 0:
#                         num_string += ch
#             if num_string:
#                 sum += int(num_string[0])
#     return sum

# Ver 3
def add_first_odd_digits(str_list):
    sum = 0
    for string in str_list:
        sum += get_first_odd(string)
    return sum

def get_first_odd(string):
    for ch in string:
        if ch in "13579":
            return int(ch)
    return 0