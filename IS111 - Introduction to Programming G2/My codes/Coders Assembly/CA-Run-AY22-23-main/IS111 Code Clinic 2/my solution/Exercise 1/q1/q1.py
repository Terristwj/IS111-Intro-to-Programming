##
# This question was adapted from SPM Programming Exercise, Roman Numerals
# Author : Stephen Pang Qing Yang
# Created : August 30, 2021
# Last Updated : August 30, 2021
#
# Copyright (C) 2021 Stephen Pang Qing Yang
##

def get_highest_score(name,file):
    # YOUR CODE GOES HERE
    highest_score = 0
    with open(file) as f:
        for line in f:
            line = line.rstrip('\n')
            cols = line.split(' ')

            if name == cols[0]:
                highest_score = cols[1]
                for i in range(2, len(cols)):
                    if cols[i] > highest_score:
                        highest_score = cols[i]
                break
    return highest_score

# DO NOT MODIFY THE CODE BELOW
# If you are getting a "No such file or directory" error, ensure that you open the q1 folder directly in your VSC, instead of the entire resource folder.

print('----Test Case 1----')
result = get_highest_score('Dana','q1.txt')
print("Expected: 50" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_highest_score('Jennifer','q1.txt')
print("Expected: 50" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_highest_score('Kristin','q1.txt')
print("Expected: 90" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_highest_score('Meese','q1.txt')
print("Expected: 80" )
print("Actual:   " + str(result))
print()

