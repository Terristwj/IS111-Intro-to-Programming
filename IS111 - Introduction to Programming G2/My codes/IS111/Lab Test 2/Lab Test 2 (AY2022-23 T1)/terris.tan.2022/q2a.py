# Name:
# Email ID:

def get_n_odd_numbers(filename, n):
    # Replace the code below with your implementation.
    my_odd_nums = []
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            num = int(line)
            if num % 2 != 0:
                my_odd_nums.append(num)
            
            if len(my_odd_nums) == n:
                break
                
    return my_odd_nums
