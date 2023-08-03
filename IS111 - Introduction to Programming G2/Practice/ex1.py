scores = {'amy':80, 'bob':75, 'claire':34, 'donald': 90}

# print bob's score 
print("Bob's score is " + str(scores["bob"]))
print()

# print out the sum of claire and amy's scores 
print("The sum of Claire and Amy's scores are " + str(scores["claire"] + scores["amy"]))
print()

# find the average score
avg = 0
size = 0
for key in scores:
    size += 1
    avg += scores[key]
print("The average score is " + str(avg/size))
print()

# find the lowest score (bonus: find the name of the person with the lowest score)

# score_low = min(scores.values())
# for key in scores.keys():
#     if scores[key] == score_low:
#         name_low = key

score_list = list(scores.keys())
score_low = scores[score_list[0]]
name_low = score_list[0]

for key in scores.keys():
    if scores[key] < score_low:
        score_low = scores[key]
        name_low = key

print("The lowest score is " + str(score_low) + ". And it is from " + name_low)
print()

# edwin has a score of 63, add him into scores dictionary 
scores["edwin"] = 63
print("Edwin scored " + str(scores["edwin"]))
print()

# print out the list of students in this class
print("Student List:")
count = 1
for key in scores:
    print(str(count) + " " + key)
    count+=1

