def contains_key(d1,d2,key):
    # YOUR CODE GOES HERE
    try:
        if d1[key] and d2[key]:
            return True
        return False
    except:
        return False

# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = contains_key({'metals':['silver','gold'],'potatos':1,'scallops':2},{'potatos':2,'scallops':5},'scallops')
print("Expected: True" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = contains_key({'cactus':[],'salad':100,'saraf':'s'},{'sennie':2,'pieces':'leftbehind'},'toenail')
print("Expected: False" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = contains_key({'cactus':[],'salad':100,'saraf':'s'},{'sennie':2,'pieces':'leftbehind'},'cactus')
print("Expected: False" )
print("Actual:   " + str(result))
print()
