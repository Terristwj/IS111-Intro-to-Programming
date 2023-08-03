from q3b import construct_string

print()
print('-' * 20)
print()

orig_str = 'ABCDEFGHIJKLMN'
len_list = [2, 5, 3, 1, 2, 1]
cnct_list = ['-', '$', '', '123', ' ']

print("Test Case 1: construct_string('" + orig_str + "', "
	+ str(len_list) + ", " + str(cnct_list) + ")")

print()

result = construct_string(orig_str, len_list, cnct_list)
print("Expected: AB-CDEFG$HIJK123LM N")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()


orig_str = '*******'
len_list = [3, 3, 1]
cnct_list = ['1', '2']

print("Test Case 2: construct_string('" + orig_str + "', "
	+ str(len_list) + ", " + str(cnct_list) + ")")

print()

result = construct_string(orig_str, len_list, cnct_list)
print("Expected: ***1***2*")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

orig_str = 'SMU'
len_list = [3]
cnct_list = []

print("Test Case 3: construct_string('" + orig_str + "', "
	+ str(len_list) + ", " + str(cnct_list) + ")")

print()

result = construct_string(orig_str, len_list, cnct_list)
print("Expected: SMU")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

orig_str = ''
len_list = []
cnct_list = []

print("Test Case 4: construct_string('" + orig_str + "', "
	+ str(len_list) + ", " + str(cnct_list) + ")")

print()

result = construct_string(orig_str, len_list, cnct_list)
print("Expected: ")
print("Actual:   " + str(result))

print("Expected type of returned value: <class 'str'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()
