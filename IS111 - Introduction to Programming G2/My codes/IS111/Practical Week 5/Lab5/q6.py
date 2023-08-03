
# Put your code below
######################
def get_all_combinations(str_list, num_list):
    combo_list = []
    for string in str_list:
        for num in num_list:
            combo_list.append((string, num))
    return combo_list

def get_larger_numbers(num_list1, num_list2):
    larger_nums = []
    for num1 in num_list1:
        isLarger = True
        for num2 in num_list2:
            if num1 < num2:
                isLarger = False
        if isLarger:
            larger_nums.append(num1)
    return larger_nums

def get_non_common_strings(str_list1, str_list2):
    common_list = []
    uncommon_list = []
    for string in str_list1:
        if string in str_list2:
            common_list.append(string)
        if string not in common_list:
            uncommon_list.append(string)
    for string in str_list2:
        if string not in common_list and string not in uncommon_list:
            uncommon_list.append(string)
    return uncommon_list
# Test Cases to test your code
##############################

r_list = get_all_combinations(["a", "b"], [1, 2, 3])
print("Expected: [('a', 1), ('a', 2), ('a', 3), ('b', 1), ('b', 2), ('b', 3)]")
print("Actual  : " + str(r_list))
print()

r_list = get_larger_numbers([4, 6, 10], [1, 3, 5])
print("Expected: [6, 10]")
print("Actual  : " + str(r_list))
print()

r_list = get_non_common_strings(["a", "b", "c", "d"], ["b", "d", "e", "f"])
print("Expected: ['a', 'c', 'e', 'f']")
print("Actual  : " + str(r_list))
print()