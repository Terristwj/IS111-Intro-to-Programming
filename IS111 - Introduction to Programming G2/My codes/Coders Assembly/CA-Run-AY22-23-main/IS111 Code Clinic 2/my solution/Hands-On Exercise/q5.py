## ENTER YOUR CODE BELOW ##

file = 'bingo_book.txt'
# name, village, gender, description, status, signature
# Optional: deserted (last col)

name = input("Please enter a ninja's name: ")

titles = ["Name: ", "Village: ", "Gender: ", "Description: ", "Status: ", "Signature Move: "]

with open(file) as f:
    for line in f:
        line = line.rstrip('\n')
        cols = line.split(',')

        if name.lower() == cols[0].lower():
            for i in range(len(cols)):
                if cols[i] != "Deserted":
                    print(titles[i] + cols[i])
                else:
                    print()
                    print("This ninja has deserted his or her village!")