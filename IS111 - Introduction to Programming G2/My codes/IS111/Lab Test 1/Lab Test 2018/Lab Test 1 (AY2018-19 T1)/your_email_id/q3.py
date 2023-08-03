#
# Name: 
# Email ID: 
#
def mask_out(sentence, banned, substitutes):
    # write your answer between #start and #end
    #start
    new_substitutes = substitutes
    if len(banned) > len(new_substitutes):
        
        for i in range(len(new_substitutes), len(banned)):
            if i < len(substitutes):
                # print(2)
                new_substitutes += substitutes[i]
            else:
                # print(1)
                new_substitutes += substitutes[0]
            # print(new_substitutes)

    # string = sentence.replace(banned, new_substitutes)
    string = ""
    for ch in sentence:
        if ch in banned:
            # .find() function
            ###################
            for i in range(len(banned)):
                if banned[i] == ch:
                    ban_index = i
            ####################
            string += new_substitutes[ban_index]
        else:
            string += ch

            
    return string
    #end


print('Test 1')
print('Expected:abcd#')
print('Actual  :' + mask_out('abcde', 'e', '#'))
print()

print('Test 2')
print('Expected:#$solute')
print('Actual  :' + mask_out('absolute', 'ab', '#$'))
print()

print('Test 3')
print('Expected:121hon')
print('Actual  :' + mask_out('python', 'pyt', '12'))
print()





