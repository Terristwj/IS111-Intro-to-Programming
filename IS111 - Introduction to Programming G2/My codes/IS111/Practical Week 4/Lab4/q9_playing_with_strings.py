def part_i(msg):
    for i in range(len(msg)+1):
        print(msg[:i])

def part_ii(msg):
    for i in range(len(msg), -1, -1):
        print(msg[:i])

msg = input("Enter a message :")
part_i(msg)
print()
part_ii(msg)