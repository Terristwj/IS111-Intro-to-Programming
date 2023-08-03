import sys

def print_test_case(country, language):
    print("\tis_official_language('" + country + "', '" + language + "')")


languages = ['Chinese', 'Dutch', 'English', 'Filipino', 'French', 'German', 'Malay', 'Tamil']
lang_dict = {'Belgium':['Dutch', 'French', 'German'],
             'Canada':['English', 'French'],
             'Philippines':['English', 'Filipino'],
             'Singapore':['Chinese', 'English', 'Malay', 'Tamil'] }

# Test Cases
test_cases = []
for country in lang_dict:
    official_languages = lang_dict[country]
    for language in languages:
        is_official = False
        if language in official_languages:
            is_official = True
        test_cases.append( (country, language, is_official) )

# Counter is to record how many test cases are passed.
# Some test cases are given partial marks.
counter = 0.0

# result_list is to store the unique values of returned results.
# If the function always returns True or always returns False,
# we'll give only partial marks.
result_list = []

try:
    from q1b import is_official_language

    tc_no = 1
    # Test case 1 to 3: Check whether the returned value's type is correct.
    for i in range(3):
        try:
            (c, l, result) = test_cases[i]
            
            print()
            print("Test Case " + str(tc_no) + ": check the data type of the returned value")
            tc_no += 1
            print_test_case(c, l)
            print("Expected: <class 'bool'>")
            
            my_result = is_official_language(c, l)
            
            print("Actual  : " + str(type(my_result)))
            
            if isinstance(my_result, bool):
                counter += 1.0
                print("passed")
            else:
                print("failed")
        except:
            print('Exception:', sys.exc_info())
            print("failed")

    # Other 32 test cases:
    for (c, l, result) in test_cases:
    
        print()
        print("Test Case " + str(tc_no) + ":")
        tc_no += 1
        print_test_case(c, l)
        print("Expected: " + str(result))    
    
        try:
            my_result = is_official_language(c, l)

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
                print("partially passed")
            else:
                print("failed")

        except:
            print('Exception:', sys.exc_info())
            print("failed")
            
except:
    print('Exception:', sys.exc_info())

# If the code always returns the same value, change counter to 10, 
# i.e., give 1 mark.
if len(result_list) == 1 and isinstance(result_list[0], bool):
    counter = 10
    print("\nYour code always returns True or always returns False!")

# There are in total 35 test cases.
# We allocate 3.5 marks for q1b.
my_marks = round(counter / 5, 0) / 2

print("\nTotal marks: " + str(my_marks))