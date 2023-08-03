# Name:
# Email ID:
def process_numbers(input_filename, output_filename):
    # Modify the code below.
    final_format = ""
    with open(input_filename) as f:
        for line in f:
            max_nums = []
            line = line.rstrip("\n")
            groups = line.split("*")
            # print(line)
            for group in groups:
                # print(group)
                numbers = group.split(" ")
                if numbers[0]:
                    max_num = int(numbers[0])
                    for num in numbers:
                        if int(num) > max_num:
                            max_num = int(num)
                    max_nums.append(max_num)

            # print(max_nums)
            format = ""
            for num in max_nums:
                if num != 0:
                    format += str(num) + "*"
                else:
                    format += "NA" + "*"
            format = format[:-1]
            # print(format)
            
            format = str(len(groups)) + ": " + format
            # print(format)
            final_format += format + "\n"
    
    with open(output_filename, 'w') as f2:
        f2.write(final_format)
    return None
    


