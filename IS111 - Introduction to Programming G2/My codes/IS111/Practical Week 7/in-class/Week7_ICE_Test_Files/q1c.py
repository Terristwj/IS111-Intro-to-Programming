my_str = '123'

for index in range(0, len(my_str)-1):
    n = int(my_str[index] + my_str[index+1])
    print(n)
    m = int(my_str[index:index+2])
    print(m)

# For iterates 2 times -> 0, 1

# My Output:
# 12
# 123
# 23
# error

# Answer:
# 12
# 12
# 23
# 23

# Solution
# range(0, len(my_str)-1):
# range(0, 3-1):
# range(0, 2):
# ranges -> 0, 1

# Index = 0
    # int(my_str[index] + my_str[index+1])
    # int( "1" + "2" )
    # 12

    # int(my_str[index:index+2])
    # int ( "12" )
    # 12

# Index = 1
    # int(my_str[index] + my_str[index+1])
    # int( "2" + "3" )
    # 23

    # int(my_str[index:index+2])
    # int ( "23" )
    # 23