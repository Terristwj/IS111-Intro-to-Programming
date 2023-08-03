def get_longest_string(str_list):
    # YOUR CODE GOES HERE
    longest_string = str_list[0]
    for string in str_list[1:]:
        # If comparing word has same length, take that word
        if len(string) >= len(longest_string):
            longest_string = string
    return longest_string

# DO NOT MODIFY THESE TEST CASES
print('----Test Case 1----')
result = get_longest_string(['sara','watercress','Areoni','hello','meh'])
print("Expected: watercress" )
print("Actual:   " + str(result))
print()
print('----Test Case 2----')
result = get_longest_string(['Lucy Heartfilia','Erza Scarlet','Natsu Dragneel','Gray Fullbuster','Wendy Marvell'])
print("Expected: Gray Fullbuster" )
print("Actual:   " + str(result))
print()
print('----Test Case 3----')
result = get_longest_string(['loser','poser','noob','doser','woser'])
print("Expected: woser" )
print("Actual:   " + str(result))
print()
print('----Test Case 4----')
result = get_longest_string(['I am a poor little string all by myself'])
print("Expected: I am a poor little string all by myself" )
print("Actual:   " + str(result))
print()