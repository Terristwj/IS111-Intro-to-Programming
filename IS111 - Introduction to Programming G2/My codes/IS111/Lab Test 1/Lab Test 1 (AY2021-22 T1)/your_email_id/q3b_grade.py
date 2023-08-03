import sys

def print_test_case(team1, team2):
    print("\tswap_members(" + str(team1) + ", " + str(team2) + ")")

def match_reversed_result(my_result, result_list):
    if not (isinstance(my_result, tuple) or isinstance(my_result, list)):
        return False
    if len(my_result) != 2:
        return False
    
    new_result = (my_result[0], my_result[1])
    if new_result in result_list or (new_result[1], new_result[0]) in result_list:
        return True
    
    return False

# Test Cases
          
team_a = [('a', 'F', 'E-3', 'R-1'),
          ('b', 'F', 'E-3', 'R-1'),
          ('c', 'F', 'E-2', 'Freethinker'),
          ('d', 'F', 'E-1', 'Freethinker'),
          ('e', 'M', 'E-3', 'Freethinker')]

team_b = [('A', 'M', 'E-3', 'R-2'),
          ('B', 'M', 'E-3', 'R-1'),
          ('C', 'M', 'E-3', 'R-1'),
          ('D', 'M', 'E-1', 'Freethinker'),
          ('E', 'F', 'E-2', 'R-2')]
          
team_c = [('P1', 'M', 'E-3', 'R-2'),
          ('P2', 'M', 'E-3', 'R-1'),
          ('P3', 'M', 'E-3', 'Freethinker'),
          ('P4', 'F', 'E-2', 'Freethinker'),
          ('P5', 'F', 'E-3', 'Freethinker')]
          
team_d = [('S1', 'M', 'E-1', 'Freethinker'),
          ('S2', 'M', 'E-2', 'R-1'),
          ('S3', 'M', 'E-2', 'Freethinker'),
          ('S4', 'F', 'E-1', 'Freethinker'),
          ('S5', 'F', 'E-2', 'R-2')]

team_e = [('P1', 'M', 'E-1', 'Freethinker'),
          ('P2', 'M', 'E-3', 'Freethinker'),
          ('P3', 'M', 'E-2', 'Freethinker'),
          ('P4', 'F', 'E-3', 'R-2'),
          ('P5', 'F', 'E-3', 'Freethinker')]
          
team_f = [('S1', 'M', 'E-1', 'Freethinker'),
          ('S2', 'F', 'E-1', 'R-1'),
          ('S3', 'F', 'E-1', 'R-3'),
          ('S4', 'F', 'E-2', 'Freethinker'),
          ('S5', 'F', 'E-3', 'R-2')]

team_g = [('S1', 'F', 'E-1', 'Freethinker'),
          ('S2', 'M', 'E-1', 'R-2'),
          ('S3', 'M', 'E-1', 'R-2'),
          ('S4', 'M', 'E-2', 'R-1'),
          ('S5', 'M', 'E-3', 'R-2')]

test_cases = [(team_a, team_b, [('a', 'A'), ('b', 'A')]),
              (team_c, team_d, [('P3', 'S1'), ('P5', 'S4')]),
              (team_e, team_f, [('P1', 'S2'), ('P1', 'S3'), ('P2', 'S2'), ('P2', 'S3')]),
              (team_e, team_g, [None])]

# Counter is to record how many test cases are passed.
# Some test cases are given partial marks.
counter = 0.0

try:
    from q3b import swap_members

    tc_no = 1

    for index in range(4):
        (team1, team2, result_list) = test_cases[index]
        
        print()
        print("Test Case " + str(tc_no) + ":")
        tc_no += 1
        print_test_case(team1, team2)
        print("Expected: one of the elements in " + str(result_list))               
        
        try:
            my_result = swap_members(team1, team2)
            
            print("Actual  : " + str(my_result))
            
            # result_list contains all possible results
            if my_result in result_list:
                
                if (index == 3):
                    # The last test case is worth 0.5 mark.
                    counter += 0.5
                else:
                    counter += 1.0
                    
                print("passed")
                    
            elif index < 3 and match_reversed_result(my_result, result_list):
                # Partially correct if the returned result has the two people
                # swapped, or the result is a list instead of a tuple.
                counter += 0.5
                
                print("partially passed")
                
            else:
                print("failed")

        except:
            print('Exception:', sys.exc_info())
            print("failed")

            
except:
    print('Exception:', sys.exc_info())

# There are in total 4 test cases.
# We allocate 3.5 marks for q3b.
my_marks = counter

print("\nTotal marks: " + str(my_marks))