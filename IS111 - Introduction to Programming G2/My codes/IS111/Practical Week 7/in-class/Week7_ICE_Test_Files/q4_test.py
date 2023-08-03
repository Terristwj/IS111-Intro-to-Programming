import q4

# Test case 1
my_list = ['abc', 'a', 'xy', '12', 'x']
sorted_list = q4.sort_strings(my_list)

print("After sorting " + str(my_list)) # This should give ['abc', 'a', 'xy', '12', 'x']
print("we get " + str(sorted_list)) # This should give ['a', 'x', 'xy', '12', 'abc']
print()

# Test case 2
my_list = ['111', '11', '1', '', '2', '22', '222']
sorted_list = q4.sort_strings(my_list)

print("After sorting " + str(my_list)) # This should give ['111', '11', '1', '11', '111']
print("we get " + str(sorted_list)) # This should give ['', '1', '2', '11', '22', '111', '222']

