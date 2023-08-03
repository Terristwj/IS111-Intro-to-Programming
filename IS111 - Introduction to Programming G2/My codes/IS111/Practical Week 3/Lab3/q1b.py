# Q1b
def compare_values_1(a, b):
    if (a != b):
        return True
    else:
        return False
    
def compare_values_2(a, b, c):
    if (a == b + c):
        print("a == b + c")
    if (b == a + c):
        print("b == a + c")
    if (c == a + b):
        print("c == a + b")

# "1 + 2" != "3" -> True, print True
print(compare_values_1("1 + 2", "3"))

# '1' == '' + '1' -> True, print clause
# '' == '1' + '1' -> False, nothing happens
# '1' == '1' + '' -> True, print clause
compare_values_2('1', '', '1')

'''
My output before running:
True
a == b + c
c == a + b
'''
