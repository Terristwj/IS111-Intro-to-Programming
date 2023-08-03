def seven_up(num):
    # YOUR CODE GOES HERE
    for i in range(1, num+1):
        if i % 14 == 0:
            print("Double 7-UP")
        elif i % 7 == 0:
            print("7-UP")
        else:
            print(i)
    pass

# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = seven_up(12)
print()
print('----Test Case 2----')
result = seven_up(16)

print()
print('----Test Case 3----')
result = seven_up(30)

print()        
