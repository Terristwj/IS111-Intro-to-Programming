# If you are getting a "No such file or directory" error message, right click on the text file and select "Copy Path", and replace 'q1.txt' with that file path.
# In lab test, DO NOT use your copied path, just revert back to q1.txt
with open('q1.txt','r') as input_file:
    for line in input_file:
        line = line.rstrip('\n')
        new_line = ""
        for ch in line:
            if ch in 'aeiou':
                new_line += 'x'
            else:
                new_line += ch
        print(new_line)



