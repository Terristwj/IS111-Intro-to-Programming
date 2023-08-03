# If you are getting a "No such file or directory" error message, right click on the text file and select "Copy Path", and replace 'q1.txt' with that file path.
# In lab test, DO NOT use your copied path, just revert back to q1.txt

# YOUR CODE GOES HERE
# with open("7 - File Handling\q1\q1.txt", "r") as file:
#     for line in file:
#         line = line.rstrip('\n')
#         for ch in line:
#             if ch in "aeiou":
#                 print("x", end="")
#             else:
#                 print(ch, end="")
#         print()
# file.close()

reformatted_string = ""
with open("7 - File Handling\q1\q1.txt", "r") as file:
    for line in file:
        line = line.rstrip('\n')
        for ch in line:
            if ch in "aeiou":
                reformatted_string += "x"
            else:
                reformatted_string += ch
        reformatted_string += "\n"

with open("7 - File Handling\q1\q1-output.txt", "w") as file:
    file.write(reformatted_string)
