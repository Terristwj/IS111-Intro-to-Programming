# Define your function here.
def retrieve_numbers(string):
    new_string = ""
    for ch in string:
        if ch.isnumeric():
            new_string += ch
        else:
            new_string += " "
    
    # 'avocado   banana  kiwi   apricot'
    new_string = ' '.join(new_string.split())
    # 'avocado banana kiwi apricot'
    return new_string

    # mylist = [('value1', 'value2', 'value3'), ('secval1', 'secval2', 'secval3')]
    # # Returns True
    # print('value2' in (item for sublist in mylist for item in sublist))
    # # Returns False
    # print('value5' in (item for sublist in mylist for item in sublist))

    return None
            



# The code below is to test your function definition.

print('Testcase 1')
print('=' * 10)
print('Expected: 12 600 0900 100')
print('Actual  :', retrieve_numbers("12abc600$##0900AB 100X"))

print('\nTestcase 2')
print('=' * 10)
print('Expected: 34 5689 980')
print('Actual  :', retrieve_numbers("34.5689abc980"))

print('\nTestcase 3')
print('=' * 10)
print('Expected: ""')
print('Actual  : "' + retrieve_numbers("xyz") + '"')

print('\nTestcase 4')
print('=' * 10)
print('Expected: 25')
print('Actual  :', retrieve_numbers("abc25xyz"))