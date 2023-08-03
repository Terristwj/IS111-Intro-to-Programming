# Name:
# Email ID:
def process_numbers(input_filename, output_filename):
    # Modify the code below.
    with open(input_filename) as f:
        final_string = ""

        for line in f:
            big_nums = []
            line = line.rstrip("\n")
            groups = line.split("*")

            for group in groups:
                if group:
                    nums = group.split(" ")
                    my_num_list = []
                    for num in nums:
                        if num[0] == "-":
                            new_num = int(num[1:]) * -1
                        else:
                            new_num = int(num)
                        my_num_list.append(new_num)
                    big_num = max(my_num_list)
                    big_nums.append(big_num)
                else:
                    big_nums.append("NA")
            
            num_nums = len(big_nums)
            final_string += str(num_nums) + ": "

            for num in big_nums:
                final_string += str(num) + "*"

            final_string = final_string[:-1] + "\n"

        with open(output_filename, 'w') as f2:
            f2.write(final_string)

    return None
    


