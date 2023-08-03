
number_count = int(input("Enter length of number list: "))

num_list = []

for i in range(1,number_count+1):
    num = int(input("Enter number " + str(i) + ": "))
    num_list.append(num)

num_list.sort()

print()
print("The minimum is " + str(num_list[0]))
print("The maximum is " + str(num_list[len(num_list)-1]))

median_index = (len(num_list) - 1) / 2
# Check if index is not a whole number by checking the decimal (e.g. 10.5, 8.5)
if (str(median_index).split('.')[1] != '0'):
    # get the middle number
    first_index_num = int(str(median_index).split('.')[0])
    second_index_num = int(str(median_index + 0.5).split('.')[0])
    median = (num_list[first_index_num] + num_list[second_index_num]) / 2
    print("The median is " + str(median))
else:
    median_index = int(str(median_index).split('.')[0])
    median = num_list[median_index]
    print("The median is " + str(median))
