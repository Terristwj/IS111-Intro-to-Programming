def get_longest_string(str_list):
    longest_count = 0
    selected_string = ""
    for string in str_list:
        if len(string) >= longest_count:
            longest_count = len(string)
            selected_string = string

    return selected_string

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