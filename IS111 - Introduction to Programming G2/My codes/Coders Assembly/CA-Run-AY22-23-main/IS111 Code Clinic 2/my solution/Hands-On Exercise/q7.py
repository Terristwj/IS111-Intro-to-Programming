def add_receipient(email, receipient_list):
    # Your code goes here (There won't be a function test because it is REALLY simple)
    return receipient_list.append(email)

## PART B Code Goes HERE
def valid_email(email):
    counter = 0
    for ch in email:
        if ch == "@":
            counter += 1
    if counter == 1:
        return True
    return False

def enter_email():
    email = input("Enter an email address: ")
    while not valid_email(email):
        print('Please enter a valid email address!')
        email = input("Enter an email address: ")
    add_receipient(email, receipient_list)

def check_valid_yesno(to_add_receipient):
    yes_no = "yesno"
    while to_add_receipient not in yes_no:
        print('Please enter a valid response!')
        to_add_receipient = input("Do you want to add more receipients? [yes or no] ")
    return to_add_receipient

receipient_list = []
enter_email()
print()

to_add_receipient = input("Do you want to add more receipients? [yes or no] ")
check_valid_yesno(to_add_receipient)

while to_add_receipient == "yes":
    enter_email()
    print()
    to_add_receipient = input("Do you want to add more receipients? [yes or no] ")
    to_add_receipient = check_valid_yesno(to_add_receipient)

print()
message = input("Please enter a message to send your receipients: ")
while not message:
    print("Your message cannot be empty!")
    message = input("Please enter a message to send your receipients: ")

print()
for i in range(len(receipient_list)):
    print(f"{i+1}. {receipient_list[i]}")
