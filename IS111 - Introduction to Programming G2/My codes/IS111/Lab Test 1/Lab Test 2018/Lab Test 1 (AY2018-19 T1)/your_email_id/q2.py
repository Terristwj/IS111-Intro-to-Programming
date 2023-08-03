#
# Name: 
# Email ID: 
#
def represent_numbers (start, end):
    # write your answer between #startcode and #endcode
    #startcode
    string = ""

    # Solution 1
    # for i in range(start, end+1):
    #     for x in range(abs(i)):
    #         string += "-"
    #     string += "#"

    # Solution 2
    for i in range(start, end+1):
        string += "-"*abs(i)+"#"

    return string[:len(string)-1]
    #endcode


print('Test 1')
print('Expected:-#--#---#----#-----')
print('Actual  :' + represent_numbers(1, 5))
print()

print('Test 2')
print('Expected:---#----#-----')
print('Actual  :' + represent_numbers(3, 5))
print()

print('Test 3')
print('Expected:-')
print('Actual  :' + represent_numbers(1, 1))
print()

print('Test 4')
print('Expected:[]')
print('Actual  :[' + represent_numbers(4, 1) + ']')
print()

print('Test 5')
print('Expected:----#---#--#-##-')
print('Actual  :' + represent_numbers(-4, 1))
print()
