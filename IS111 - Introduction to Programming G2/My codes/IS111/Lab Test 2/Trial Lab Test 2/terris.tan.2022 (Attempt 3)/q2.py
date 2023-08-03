# Name:
# Email ID:
def process_numbers(input_filename, output_filename):
    # Modify the code below.
    with open(input_filename) as f:
        my_final_string = ""
        lines = f.read().split('\n')
        for line in lines:
            groups = line.split('*')
            num_groups = len(groups)

            if line:
                biggest_nums = []
                for group in groups:
                    if group:
                        nums = group.split(' ')
                        biggest_num = int(nums[0])
                        for num in nums:
                            num = int(num)
                            if num > biggest_num:
                                biggest_num = num
                        biggest_nums.append(biggest_num)
                    else:
                        biggest_nums.append('NA')
                
                my_string = ''
                for num in biggest_nums:
                    my_string += str(num) + "*"
                my_string = my_string[:-1]

                my_final_string += str(num_groups) + ": " + my_string + "\n"
    
    with open(output_filename, 'w') as f:
        f.write(my_final_string)
    


