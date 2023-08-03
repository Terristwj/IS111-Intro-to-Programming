def contains_value(d1,d2,value):
    # YOUR CODE GOES HERE
    present1 = False
    present2 = False
    for key1 in d1:
        if d1[key1] == value:
            present1 = True
    for key2 in d2:
        if d2[key2] == value:
            present2 = True
    if present1 and present2:
        return True
    return False

# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = contains_value({'metals':'tea','potatos':1,'scallops':2},{'potatos':2,'scallops':5},2)
print("Expected: True" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = contains_value({'cactus':[],'salad':100,'saraf':'s'},{'sennie':2,'pieces':'leftbehind'},'s')
print("Expected: False" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = contains_value({'cactus':[],'salad':100,'saraf':'s'},{'sennie':2,'pieces':'leftbehind'},'henna')
print("Expected: False" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = contains_value({'cactus':[],'salad':100,'saraf':'Free'},{'sennie':'Free','pieces':'leftbehind'},'Free')
print("Expected: True" )
print("Actual:   " + str(result))
print()