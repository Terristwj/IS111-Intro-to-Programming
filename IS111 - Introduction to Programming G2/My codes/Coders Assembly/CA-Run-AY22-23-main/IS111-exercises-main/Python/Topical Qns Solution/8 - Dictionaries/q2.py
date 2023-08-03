def contains_value(d1,d2,value):
    # INITIALIZE TRUE AND FALSE VALUES FOR d1 AND d2
    in_d1 = False
    in_d2 = False

    # SEARCH FOR THE VALUES in d1
    for key1 in d1:
        if d1[key1] == value:
            in_d1 = True
    # SEARCH FOR THE VALUES in d2
    for key2 in d2:
        if d2[key2] == value:
            in_d2 = True

    # Return True or False depending on whether the value is in both d1 and d2
    return in_d1 and in_d2


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