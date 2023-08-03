def get_all_multiples(start, end, divisor):
    for i in range(start,end+1):
        if i % divisor == 0:
            print(i)


# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = get_all_multiples(1,30,7)
print()
print('----Test Case 2----')
result = get_all_multiples(1,10,2)
