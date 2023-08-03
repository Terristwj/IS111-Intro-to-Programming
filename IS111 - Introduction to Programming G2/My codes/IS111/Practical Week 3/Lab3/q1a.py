# Q1a
def perform_magic1(condition, output):
    if (condition):
        print(output)

def perform_magic2(condition, output):
    if (condition):
        print(output)
    else:
        print("The condition is false!")

def perform_magic3(a, b):
    if (a >= b):
        print("a >= b")
 
    if (a <= b):
        print("a <= b")

a = 12
b = 15

# a == b -> False, nothing happens
perform_magic1(a == b, "a == b")

# a >= b -> False, print else clause
perform_magic2(a > b, "a > b")

# a+3 == b -> True, print both clauses
perform_magic3(a + 3, b)

'''
My output before running:
The condition is false!
a >= b
a <= b
'''