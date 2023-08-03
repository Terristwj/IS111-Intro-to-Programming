# Name:
# Email ID:

def reformat_time(time):
    if "AM" in time:
        return int(time.rstrip("AM"))
    elif "PM" in time and int(time.rstrip("PM")) < 12:
        return int(time.rstrip("PM")) + 12
    else:
        return int(time.rstrip("PM"))

def read_schedule(filename):
    # Write your code here.
    days_recorded = []
    staff_recorded = []
    working_times = {}

    with open(filename) as f:
        for line in f:
            line = line.rstrip("\n")
            cols = line.split("|")

            day = cols[0]
            time_start = reformat_time(cols[1])
            time_end = reformat_time(cols[2])
            staffs = cols[3].split(" ")
            
            if day not in days_recorded:
                days_recorded.append(day)
                working_times[day] = []

            for staff in staffs:
                formatted_staff = (time_start, time_end, staff)
                # Ignore entries with same timeslot
                if formatted_staff not in working_times[day]:
                    if (day, staff) not in staff_recorded:
                        staff_recorded.append((day, staff))
                        working_times[day].append(formatted_staff)

                    # When the staff have multiple timeslots in the same day
                    else:
                        current_time_diff = time_end - time_start
                        for i in range(len(working_times[day])):
                            if working_times[day][i][2] == staff:
                                index = i
                                dict_time_diff = working_times[day][i][1] - working_times[day][i][0]
                                break
                        if current_time_diff <= dict_time_diff:
                            # print(staff, day, index, working_times[day])
                            # print(working_times[day][index])
                            working_times[day][index] = formatted_staff

    return working_times

    

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, filename, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: read_schedule("{filename}")')
        print()
        print(f'Expected: {expected_output}')
        result = read_schedule(filename)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        print(f'Is the returned dictionary the same as expected? {expected_output == result}')
    
    expected_dict =  {'Mon': [(9, 10, 'ahbeng'), (9, 16, 'donta'), (10, 17, 'starkov'), (9, 16, 'leongben')], 'Tue': [(12, 17, 'jingjiang'), (12, 17, 'michellekan'), (9, 17, 'leongben'), (9, 17, 'darkling'), (14, 16, 'markloh'), (14, 16, 'angelwong')], 'Wed': [(9, 12, 'markloh'), (9, 12, 'vandana'), (13, 14, 'wendytan'), (9, 12, 'ylee'), (9, 12, 'wangyong'), (13, 14, 'joelle')], 'Fri': [(14, 17, 'tonytan'), (14, 17, 'jessicali')]}
    run_test_case(1, 'schedule1.txt' , expected_dict, "<class 'dict'>")

    expected_dict = {'Mon': [(9, 11, 'ahbeng'), (9, 11, 'donta')], 'Thu': [(12, 17, 'qianru')], 'Sat': [(9, 12, 'markloh'), (9, 12, 'haewoon')], 'Sun': [(13, 17, 'wangyong')]}
    run_test_case(2, 'schedule2.txt' , expected_dict, "<class 'dict'>")
