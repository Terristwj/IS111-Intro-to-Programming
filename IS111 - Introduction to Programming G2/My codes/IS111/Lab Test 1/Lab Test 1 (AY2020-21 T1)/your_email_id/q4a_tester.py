
try:
    from q4a import trace_contacts
except:
    pass

########  Internal  ########
filename = 'q4a.csv'

# find the username
import os
cwd = os.path.dirname(__file__)
username = cwd.split("/")[-1]

def append_to_file(content):
    with open(filename, 'a') as f:
        f.write(username + content + '\n')
########  Internal  ########


count_correct = 0

test_cases = [
            # TC1
            ('X', 
            [("X", "A", -7), 
            ("X", "B", -6), 
            ("B", "G", -4), 
            ("C", "D", -4), 
            ("E", "F", -1),     # X -> C -> E -> F
            ("E", "C", -3),     # X -> C -> E
            ("C", "X", -5),     # X -> C
            ("F", "A", -2), 
            ("F", "G", -3)],
            ['C', 'E', 'F']),

                #TC2
                ('J',
               [
                 ("Z", "Y", -3),
                ( "B", "G", -1), 
                ("E", "Z", -3),
                ("C", "G", -2),
                ("J", "V", -6),     
                ('S', 'R', -1),      # J -> D -> S -> R
                ("D", "S", -3),      # J -> D -> S
                ("D", "T", -1),      # J -> D -> T
                ("D", "J", -5),      # J -> D 
                ("J", "Z", -3),      # J -> Z
                ("J", "G", -3)       # J -> G
                 ],    
               ['B', 'Z', 'D', 'G', 'T', 'S','R' ]),
               
               #TC3: deliberately sorted in order (-7, -6, ..., -1)
              ('J',
               [("T", "J", -7),
                ("G", "J", -6),
                ("S", "V", -4),
                ("Z", "J", -3),    # J -> Z
                ("S", "J", -2),    # J -> S
                ("J", "S", -1),    # J -> S [ repeated ]
                ("J", "A", -1),     # J -> A 
                ("Z", "E", -1)    # J -> Z -> E
                ],
                ['A', 'S', 'Z', 'E']),
                
            #TC4
            ('B', [
            ('D', 'G', -1),   # B -> D -> G 
            ("D", "A", -1),   # A -> D [repeated]
            ("E", "F", -1),   # B -> E -> F
            ("B", "E", -5),   # B -> E
            ("B", "C", -2),   # B -> C
            ("D", "B", -3),   # B -> D
            ("B", "A", -5)    # B -> A
            ], ['A', 'C', 'D', 'E', 'F', 'G']),

            #TC5
            ('B', [
            ("Y", "A", -6),
            ("A", "C", -5),
            ("Z", "X", -4),
            ("A", "X", -4),  
            ("E", "D", -2), 
            ("D", "F", -1),  # B -> A -> D -> F
            ('C', 'G', -1),  # B -> A -> C  -> G
            ("A", "D", -3),  # B -> A -> D
            ("A", "C", -3),  # B -> A -> C
            ("B", "A", -5),  # B -> A
            ("X", "B", -6)   
            ], ['A', 'C', 'D', 'F', 'G']),


            # TC6
            ('Gideon', [
            ("Zac", "Jack", -3),      
            ("Cindy", "Jason", -4), 
            ("Vivien", "Jason", -3), 
            ("Gideon", "Darren", -7),
            ("Jason", "Gideon", -4),    # Gideon -> Jason  (repeated)  
            ("Gideon", "Jason", -5),    # Gideon -> Jason                 
            ("Gideon", "Vivien", -1)    # Gideon -> Viven  
            ],
            ['Jason', 'Vivien'])


 ]
            



num = 0
for patient, history, result in test_cases:
    try:
        num += 1
        print(f'TC {num}:trace_contacts("{patient}", {history})')
        print(f'Expected:{result}')
        print(f'Actual  :{trace_contacts(patient, history)}')


        if sorted(trace_contacts(patient, history)) == sorted(result):           
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
if count_correct in (1,):
    marks = 0.5
elif count_correct in (2,):
    marks = 1.5   
elif count_correct in (3,):
    marks = 2    
elif count_correct in (4,):
    marks = 2.5
elif count_correct in (5,):
    marks = 3
elif count_correct in (6,):
    marks = 4

print(f'{count_correct} of {num} passed.')
print(f'{marks} marks awarded.')


########  Internal  ########
append_to_file(f',{marks},{count_correct}')
########  Internal  ########