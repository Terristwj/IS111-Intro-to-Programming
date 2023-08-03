def get_odd_numbers(num_list):
    odd_list = []
    for num in num_list:
        if num % 2 != 0:
            odd_list.append(num)

    return odd_list


# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = get_odd_numbers((1,5,3,10,11,13))
print("Expected: [1, 5, 3, 11, 13]" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_odd_numbers([4,6,55,30,2])
print("Expected: [55]" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_odd_numbers([2,6,10,32,40,16])
print("Expected: []" )
print("Actual:   " + str(result))
print()