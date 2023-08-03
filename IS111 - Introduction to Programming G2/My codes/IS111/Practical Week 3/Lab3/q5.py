# Q5
# The following function is provided to you.
# Do not modify the function definition!
def get_user_info():
    """
    This function prompts the user for his/her name, gender, age and whether
    or not he/she is a student.
    The function returns a tuple that contains all the information entered
    by the user.
    """
    name = input("What's your name? ")
    gender = input("What's your gender? [M|F] ")
    age = int(input("What's your age? "))
    is_student = input("Are you a student? [yes|no] ")
    return (name, gender, age, is_student == 'yes')

# Write your code below:
user_info = get_user_info()

if user_info[2] > 6:
    name_title = "Mr." if user_info[1] == 'M' else "Mrs."
    name = name_title + " " + user_info[0]
    
    if user_info[2] >= 60:
        print(name + ", you can get concessionary fare for senior citizens.")
    else:
        if user_info[3]:
            print(name + ", you can get concessionary fare for students.")
        else:
            print(name + ", you need to pay full fare.")
else:
    print(user_info[0] + ", you can travel for free")

