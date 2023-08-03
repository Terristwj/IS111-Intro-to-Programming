def display_fibonacci(n):               # Memory State Diagram
    cur_num = 1                         # cur_num: 1
    old_num = 0                         # old_num: 0
    
    for i in range(n):                  # Memory State Diagram
        print(cur_num, end=' ')         # output:  1, 1, 2, 3, 5 ...
        cur_num += old_num              # cur_num: 1, 2, 3, 5 ...
        old_num = cur_num - old_num     # old_num: 1, 1, 2, 3 ...
        
    print()