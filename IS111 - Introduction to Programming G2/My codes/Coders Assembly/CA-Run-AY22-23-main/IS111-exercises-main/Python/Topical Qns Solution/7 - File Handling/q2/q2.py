# If you are getting a "No such file or directory" error message, right click on the text file and select "Copy Path", and replace 'q1.txt' with that file path.
# In lab test, DO NOT use your copied path, just revert back to q2.txt

with open('q2.txt','r') as input_file:
    # INITIALIZING INDEX AND GROUPING LIST
    index = 0
    group_list = ['fruits','drinks','proteins']

    for line in input_file:
        line = line.rstrip('\n')
        columns = line.split(" ")
        print("We have the following " + group_list[index] + ":")
        for col in columns:
            print(col)
        index += 1
        print()


