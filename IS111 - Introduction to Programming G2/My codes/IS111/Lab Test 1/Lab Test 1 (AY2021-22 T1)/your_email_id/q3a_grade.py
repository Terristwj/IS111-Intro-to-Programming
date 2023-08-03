import sys

def print_test_case(team):
    print("\tcheck_diversity(" + str(team) + ")")

# Test Cases
          
team_1 = [('a', 'M', 'French', 'Religion1'),
          ('b', 'F', 'German', 'Religion2'),
          ('c', 'M', 'Japanese', 'Religion1'),
          ('d', 'F', 'Korean', 'Freethinker'),
          ('e', 'F', 'Chinese', 'Freethinker')]

team_2 = [('Alice', 'F', 'Chinese', 'Buddhism'),
          ('Bob', 'M', 'Indian', 'Hinduism'),
          ('Chris', 'M', 'Jew', 'Judaism'),
          ('Dylon', 'M', 'Chinese', 'Freethinker'),
          ('Eric', 'M', 'Malay', 'Islam')]
          
team_3 = [('Alice', 'F', 'Chinese', 'Buddhism'),
          ('Bob', 'M', 'Chinese', 'Buddhism'),
          ('Chris', 'M', 'Jew', 'Judaism'),
          ('Dylon', 'M', 'Chinese', 'Freethinker'),
          ('Ellen', 'F', 'Chinese', 'Buddhism')]
          
team_4 = [('Alice', 'F', 'Chinese', 'Buddhism'),
          ('Bob', 'M', 'Indian', 'Buddhism'),
          ('Chris', 'M', 'French', 'Freethinker'),
          ('Dylon', 'M', 'Chinese', 'Freethinker'),
          ('Ellen', 'F', 'Indian', 'Buddhism')]

team_5 = [('a', 'F', 'French', 'Religion1'),
          ('b', 'F', 'German', 'Religion2'),
          ('c', 'F', 'Japanese', 'Religion1'),
          ('d', 'F', 'Korean', 'Freethinker'),
          ('e', 'M', 'Chinese', 'Freethinker')]

team_6 = [('P1', 'M', 'E1', 'R1'),
          ('P2', 'F', 'E2', 'R1'),
          ('P3', 'F', 'E1', 'R2'),
          ('P4', 'F', 'E2', 'R1'),
          ('P5', 'M', 'E1', 'R1')]

team_7 = [('S1', 'F', 'E-x', 'Freethinker'),
          ('S2', 'M', 'E-y', 'Freethinker'),
          ('S3', 'M', 'E-x', 'R-x'),
          ('S4', 'F', 'E-y', 'R-x'),
          ('S5', 'F', 'E-z', 'R-x')]

test_cases = [(team_1, True),
              (team_2, False),
              (team_3, False),
              (team_4, False),
              (team_5, False),
              (team_6, False),
              (team_7, False)]

# Counter is to record how many test cases are passed.
# Some test cases are given partial marks.
counter = 0.0
# result_list is to store the unique values of returned results.
# If the function always returns True or always returns False,
# we'll give only partial marks.
result_list = []

try:
    from q3a import check_diversity

    tc_no = 1

    for (team, result) in test_cases:
    
        print()
        print("Test Case " + str(tc_no) + ":")
        tc_no += 1
        print_test_case(team)
        print("Expected: " + str(result))       
    
    
        try:
            my_result = check_diversity(team)
            
            print("Actual  : " + str(my_result))
            
            # Place unique values of the returned result
            # into result_list.
            # Later we will check if the function
            # always returns True or always returns False.
            if my_result not in result_list:
                result_list.append(my_result)
                
            if my_result == result:
                counter += 1.0
                print("passed")
            elif my_result == str(result):
                # Partially correct if the answers are strings.
                counter += 0.5
                print("partially passed because the data type of the returned value is " + str(type(my_result)))
            else:
                print("failed")
        except:
            print('Exception:', sys.exc_info())
            print("failed")
            
except:
    print('Exception:', sys.exc_info())


# If the code always returns False, then check a few 
# additional test cases that should be True.
# If indeed the code always returns False on these test cases,
# then reduce counter to 1.

team_8 = [('P1', 'M', 'E-0', 'Freethinker'), 
          ('P2', 'M', 'E-1', 'R-0'), 
          ('P3', 'M', 'E-0', 'R-1'), 
          ('P4', 'F', 'E-2', 'R-1'), 
          ('P5', 'F', 'E-0', 'Freethinker')]

team_9 = [('P1', 'F', 'E-1', 'R-0'), 
          ('P2', 'F', 'E-2', 'R-0'), 
          ('P3', 'M', 'E-3', 'R-1'), 
          ('P4', 'M', 'E-4', 'R-1'), 
          ('P5', 'F', 'E-5', 'R-2')]
          
team_10 = [('P1', 'F', 'E-0', 'R-1'), 
           ('P2', 'F', 'E-1', 'R-2'), 
           ('P3', 'M', 'E-0', 'R-3'), 
           ('P4', 'F', 'E-2', 'R-4'), 
           ('P5', 'M', 'E-1', 'R-5')]          

additional_test_cases = [(team_8, True),
                         (team_9, True),
                         (team_10, True)]

if len(result_list) == 1 and result_list[0] == False:

    print("\nYour code returned False for all the 7 test cases above.")
    print("\nCheck a few more test cases to see if your code always returns False when the correct value should be True.")

    always_false = True
    for (team, result) in additional_test_cases:
    
        print()
        print_test_case(team)
        print("Expected: True")
        my_result = check_diversity(team)
        print("Actual  : " + str(my_result))
        if my_result == True:
            always_false = False
    
    if always_false:
        counter = 1
        print("\nYour code always returns False for all the test cases we have tried. Therefore, you will receive 0.5 mark for this question.")
    else:
        print("\nYour code returned True for some test cases. You won't get penalized.")

# There are in total 7 test cases.
# We allocate 3.5 marks for q3a.
my_marks = counter / 2

print("\nTotal marks: " + str(my_marks))