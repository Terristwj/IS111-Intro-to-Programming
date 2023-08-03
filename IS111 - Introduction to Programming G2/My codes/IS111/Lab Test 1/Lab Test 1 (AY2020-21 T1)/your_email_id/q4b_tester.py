

try:
    from q4b import trace_contacts_2
except:
    pass

########  Internal  ########
filename = 'q4b.csv'

# find the username
import os
cwd = os.path.dirname(__file__)
username = cwd.split("/")[-1]

def append_to_file(content):
    with open(filename, 'a') as f:
        f.write(username + content + '\n')
########  Internal  ########

count_correct = 0

test_cases =[ 
            # TC1
            ('A', 
            [
            ("Z", "X", -4),
            ("D", "F", -1),     # A -> C -> D -> F
            ("C", "D", -3),     # A -> C -> D
            ("A", "C", -5),     # A -> C
            ("B", "A", -5),     # A -> B
            ("A", "X", -4),     # A -> X
            ("E", "D", -2), 
            ("X", "A", -6),
            ("Y", "A", -6)
            ],    
            5,7,['B', 'C', 'D', 'F', 'X']),
            # TC2
            ("A",
            [
            ("A","C", -8),    # A -> C
            ("A","B", -9),
            ("C","D", -6),    # A -> C -> D
            ("F","D", -4),    # A -> C -> D -> F
            ("F","E", -2),    # A -> C -> D -> F -> E
            ],
            8,
            10, ['C', 'D', 'F', 'E']),
            # TC3
            ("Jason",
             [("Jason", "Aaron", -1),     # Jason -> (Aaron)
            ("Zac", "Jack", -3), 
            ("Sarah", "Vivien", -2),      # Jason -> Sarah -> (Viven)
            ("Sarah", "Jason", -4),       # Jason -> (Sarah)
            ("Gideon", "Evil", -5),       # Jason -> Gideon -> (Evil)
            ("Gideon", "Jason", -6)],     # Jason -> (Gideon)
            6,
            7, 
            ['Aaron', 'Gideon', 'Sarah', 'Vivien', 'Evil']),
            # TC4
            ("A", [
            ("Z", "X", -4),
            ("C", "D", -3),
            ("X", "D", -2), 
            ("F", "X", -1),    # A -> (F)
            ("X", "A", -6),
            ("Y", "A", -6),
            ("B", "A", -5),
            ("A", "C", -5),
            ("A", "X", -4)],   # A -> (X)
            4,7, ['F', 'X']),
            # TC5
            ("B", [
            ("Z", "U", -3),     # B -> X -> Z -> (U)
            ("D", "C", -2),
            ("Z", "D", -2),     # B -> X -> Z -> (D)
            ("U", "V", -2),     # B -> X -> Z -> U -> (V)     
            ("D", "F", -1),     # B -> X -> Z -> D -> (F)
            ("C", "B", -7),        
            ("X", "B", -6),     # B -> (X)
            ("Y", "A", -6),    
            ("B", "A", -5),     # B -> (A)
            ("A", "C", -5),
            ("Z", "X", -4),     # B -> X -> (Z)
            ("A", "X", -4),     # B -> X -> (A) 3 repeated
            ("C", "D", -3)
            ], 
            6, 
            7, ['A', 'D', 'F', 'U', 'V', 'X', 'Z'])]


num = 0
for patient, history, n, m, result in test_cases:
    num += 1

    try:
        print(f'TC {num}:trace_contacts_2("{patient}", {history}, {n}, {m})')
        print(f'Expected:{result}')
        print(f'Actual  :{trace_contacts_2(patient, history, n, m)}')


        if sorted(trace_contacts_2(patient, history, n, m)) == sorted(result):
            count_correct += 1
            print('Result  :Pass')
            print()
        else:
            print('Result  :Fail')
            print()
    except:
        print('Result  :Fail')
        print()

marks = 0
print(f'Correct results for {count_correct}')
if count_correct == 1:
    marks = 0.5
elif count_correct == 2:
    marks = 1
elif count_correct == 3:
    marks = 1.5
elif count_correct == 4:
    marks = 2
elif count_correct == 5:
    marks = 3


print(f'{count_correct} of {num} passed.')
print(f'{marks} marks awarded.')


########  Internal  ########
append_to_file(f',{marks},{count_correct}')
########  Internal  ########