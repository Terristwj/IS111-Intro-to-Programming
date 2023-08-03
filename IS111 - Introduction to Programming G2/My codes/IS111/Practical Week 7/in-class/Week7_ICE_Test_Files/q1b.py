def do_trick(a_list):
    a_list.append(a_list[1:3] + [a_list[3]])
    print(a_list)

my_list = ['a', 'b', 'c', 'd']
do_trick(my_list)
print(my_list)

# My Output:
# ['a', 'b', 'c', 'd', 'b', 'c', 'd']
# [a, b, c, d]

# Answer:
# ['a', 'b', 'c', 'd', ['b', 'c', 'd']]
# ['a', 'b', 'c', 'd', ['b', 'c', 'd']]

# Solution
# a_list[1:3] = [ "b", "c" ]
# a_list[3] = "d"
# [a_list[3]] = [ "d" ]

# .append(a_list[1:3] + [a_list[3]])
# .append( [ "b", "c" ] + ["d"] )
# .append( [ "b", "c", "d"] )