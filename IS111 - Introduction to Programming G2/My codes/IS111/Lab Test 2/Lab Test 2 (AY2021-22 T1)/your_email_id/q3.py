# Name:
# Email ID:    
import datetime
def get_days_between(start_tup, end_tup):
    '''
    This function returns the number of days between two dates.
    Do not modify the code in this function!!!
    You're required to use this function in your code for Q3.
    
    Parameters:
        start_tup: the start date which is a tuple in the form (year, month, day).
             The year, month and day are integers.
        end_tup:   the end date. The format is the same as start_tup.

    Returns the number of days in between the 2 days (end_tuple – start_tuple).
    For example, if start_tup is (2020, 12, 1) and end_tup is (2020, 12, 3), this
    function returns the value 2.

    More examples:
    get_days_between((2021,10,15), (2021, 10, 30)) returns 15
    get_days_between((2021,8,15), (2021, 10, 11)) returns 57
    get_days_between((2021,8,15), (2021, 9, 12)) returns 28
    get_days_between((2021,10,15), (2021, 10, 29)) returns 14
    '''

    start_date = datetime.date(*start_tup)
    end_date = datetime.date(*end_tup)
    return (end_date - start_date).days

def format_date(date):
    if date == "NA":
        return date
    
    cols = date.split("/")
    day = cols[0]
    month = cols[1]
    year = cols[2]

    if len(day) == 2 and int(day[0]) == 0:
        day = day[1]
    if len(month) == 2 and int(month[0]) == 0:
        month = month[1]

    new_date = (int(year), int(month), int(day))
    return new_date

def check_vaccination(key, vaccination_records, today):
    age = vaccination_records[key][0]
    first_date = vaccination_records[key][1]
    second_date = vaccination_records[key][2]

    if int(age) < 12:
        return False
    if second_date == "NA":
        return False
    if get_days_between(first_date, second_date) < 28 or get_days_between(first_date, second_date) > 56:
        return False
    if get_days_between(second_date, today) < 13:
        return False
    return True
    
def get_vaccination_status(filename, today):
    # Write your code here.
    vaccination_status = {}
    vaccination_records = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip("\n")
            cols = line.split("|")

            id = cols[0]
            age = int(cols[1])
            first_date = format_date(cols[2])
            second_date = format_date(cols[3])

            vaccination_records[id] = [age, first_date, second_date]
    
    for key in vaccination_records:
        is_vaccinated = check_vaccination(key, vaccination_records, format_date(today))
        vaccination_status[key] = (vaccination_records[key][0], is_vaccinated)

    return vaccination_status

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, filename, today, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_vaccination_status("{filename}", "{today}")')
        print()
        print(f'Expected: {expected_output}')
        result = get_vaccination_status(filename, today)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
        
    
    expected_dict = {'S1': (22, True), 'F1': (2, False), 'G2': (35, False), 'S2': (12, True), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(1, 'record1.txt', '25/10/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'S1': (22, True), 'F1': (2, False), 'G2': (35, True), 'S2': (12, True), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(2, 'record1.txt', '15/11/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'S1': (22, False), 'F1': (2, False), 'G2': (35, False), 'S2': (12, False), 'S3': (60, False), 'S5': (62, False)}
    run_test_case(3, 'record1.txt', '15/1/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'F1': (2, False), 'S2': (11, False), 'S3': (8, False)}
    run_test_case(4, 'record2.txt', '15/10/2021' , expected_dict, "<class 'dict'>")

    expected_dict = {'G2': (35, False), 'S3': (22, False), 'S4': (62, False)}
    run_test_case(5, 'record3.txt', '1/11/2021' , expected_dict, "<class 'dict'>")
    
