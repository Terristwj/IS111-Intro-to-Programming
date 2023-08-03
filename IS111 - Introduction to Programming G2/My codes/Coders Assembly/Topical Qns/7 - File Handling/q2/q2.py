# If you are getting a "No such file or directory" error message, right click on the text file and select "Copy Path", and replace 'q1.txt' with that file path.
# In lab test, DO NOT use your copied path, just revert back to q1.txt

# YOUR CODE GOES HERE
# with open("7 - File Handling\q2\q2.txt", "r") as file:
#     item_type = ["fruits", "drinks", "protein"]
#     counter = 0
#     for line in file:
#         line = line.rstrip("\n")
#         items = line.split(" ")

#         print(f"We have the following {item_type[counter]}:")
#         for item in items:
#            if item:
#               print(item)
#         print()
#         counter += 1

reformatted_string = ""
with open("7 - File Handling\q2\q2.txt", "r") as file:
    item_type = ["fruits", "drinks", "protein"]
    counter = 0
    for line in file:
        line = line.rstrip("\n")
        items = line.split(" ")

        reformatted_string += "We have the following " + item_type[counter] + ":\n"
        for item in items:
            if item:
                reformatted_string += item + "\n"
        reformatted_string += "\n"
        counter += 1

with open("7 - File Handling\q2\q2-output.txt", "w") as file:
    file.write(reformatted_string[:-2])