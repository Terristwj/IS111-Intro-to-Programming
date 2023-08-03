def print_triangle(ch, num_rows):
    if num_rows == 1:
        print("*")
    else:
        for i in range(num_rows):
            spaces = " "*((num_rows-1)-i)
            print(spaces, end="")
            print(ch*(1+i*2), end="")
            print()

def print_frame(ch, num_rows, num_cols):
    print(ch*num_rows)
    for i in range(num_rows-2):
        print(ch, end="")
        print(" "*(num_rows-2), end="")
        print(ch, end="")
        print()
    print(ch*num_rows)

def print_diamond(ch, n):
    for i in range(1, (n*2-1)//2+1):
        spaces = n-i
        print(" "*spaces + ch, end="")
        if i != 1:
            spaces = ((i-1)*2-1)
            print(" "*spaces, end="")
            print(ch, end="")
        print()

    print(ch, end="")
    if spaces == 1:
        print(" ", end="")
    else:
        print(" "*(spaces+2), end="")
    print(ch, end="")

    print()
    for i in range(1, (n*2-1)//2+1):
        print(" "*i, end="")
        print(ch, end="")
        print(" "*spaces, end="")
        spaces -= 2
        if i != (n*2-1)//2:
            print(ch, end="")
        print()