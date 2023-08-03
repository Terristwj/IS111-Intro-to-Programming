def get_odd_numbers(num_list):
    # YOUR CODE GOES HERE
    odd_nums = []
    for num in num_list:
        if num % 2:
            odd_nums.append(num)
    return odd_nums


# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = get_odd_numbers((1,5,3,10,11,13))
print("Expected: [1, 5, 3, 11, 13]" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_odd_numbers([4,6,55,30,2])
print("Expected: 23.2" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_odd_numbers([2,6,10,32,40,16])
print("Expected: 5.0" )
print("Actual:   " + str(result))
print()