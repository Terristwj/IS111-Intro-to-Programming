# YOUR CODE GOES HERE
length = int(input("Enter length of number list: "))
num_list = []
for i in range(1, length+1):
    num_list.append(int(input("Enter number " + str(i) + ": ")))

min = num_list[0]
max = num_list[0]
for num in num_list:
    if num < min:
        min = num
    if num > max:
        max = num

num_list.sort()
if len(num_list) % 2:
    median = num_list[len(num_list)//2]
else:
    median = (num_list[len(num_list)//2 - 1] + num_list[len(num_list)//2]) / 2

print()
print("The minimum is", min)
print("The maximum is", max)
print("The median is", median)
