def get_average(num_tuple):
    total_num = 0
    for num in num_tuple:
        total_num += num
    
    average = total_num / len(num_tuple)

    return average

# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = get_average((1,5,3))
print("Expected: 3.0" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_average((4,6,55,30,21))
print("Expected: 23.2" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_average((8,2))
print("Expected: 5.0" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_average((2,500))
print("Expected: 251.0" )
print("Actual:   " + str(result))
print()