# What is a Fibonacci?

# What is the return value of the question?
# - Final Fibonacci
# - Sequence Fibonacci
#    = List
#    - String cont


def fibonacci(num:int):

    # Edge cases
    # Case 1: num = 1
    if num == 1:
        return [0]
    # Case 2: num = 2
    if num == 2:
        return [0, 1]

    # Normal case
    my_list = [0, 1]
    while(num>2):
        num -= 1
        last_num = my_list[-2]
        my_list.append(my_list[-1]+last_num)
    
    return my_list


print(fibonacci(1))
# 0

print(fibonacci(2))
# 0 1

print(fibonacci(5))
# 0 1 1 2 3

print(fibonacci(10))
# 0 1 1 2 3