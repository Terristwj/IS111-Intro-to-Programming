# Name:
# Email ID:

def get_flight_durations(filename):
    # Replace the code below with your implementation.
    my_dict = {}
    with open(filename) as f:
        flight_code_dict = {}
        schedule_dict = {}
        actual_schedule_dict = {}
        for line in f:
            line = line.rstrip('\n')
            cols = line.split(' ')

            counter = 0
            index_counter = 0
            for ch in line:
                index_counter += 1
                if ch == '(':
                    counter += 1
                if counter == 2:
                    break
            airline_index_start = line.find(')') + 2
            airline_index_end = index_counter - 7


            airline = line[airline_index_start:airline_index_end]

            flight_code = cols[2]
            if flight_code not in flight_code_dict:
                flight_code_dict[flight_code] = []
            flight_code_dict[flight_code].append(line[line.find(flight_code)+len(flight_code)+1:line.find('(')-1])

            scheduled_time = cols[0]
            if cols[1] == "PM":
                scheduled_time = (int(scheduled_time.split(":")[0]) + 12) * 60 + int(scheduled_time.split(":")[1])
            else:
                scheduled_time = int(scheduled_time.split(":")[0]) * 60 + int(scheduled_time.split(":")[1])

            if flight_code not in schedule_dict:
                schedule_dict[flight_code] = []
            schedule_dict[flight_code].append(scheduled_time)

            actual_scheduled_time = cols[-2]
            if cols[-1] == "PM":
                actual_scheduled_time = (int(actual_scheduled_time.split(":")[0]) + 12) * 60 + int(actual_scheduled_time.split(":")[1])
            else:
                actual_scheduled_time = int(actual_scheduled_time.split(":")[0]) * 60 + int(actual_scheduled_time.split(":")[1])

            if flight_code not in actual_schedule_dict:
                actual_schedule_dict[flight_code] = []
            actual_schedule_dict[flight_code].append(actual_scheduled_time)
            # scheduled_arr_time = cols[0]
            # scheduled_dep_time = cols[-2]
            # scheduled_time = scheduled_arr_time - scheduled_dep_time

            
        print(schedule_dict)
        for key in flight_code_dict:
            if len(flight_code_dict[key]) == 2:
                if key not in my_dict:
                    my_dict[key] = []
                    my_dict[key].append([flight_code[key], "", "", "", ""])
                print(my_dict)
                my_dict[key][1] = flight_code_dict[key][0]
                my_dict[key][2] = flight_code_dict[key][1]

        for airline in my_dict:
            for key in schedule_dict:
                if airline == key:
                    my_dict[key][3] = schedule_dict[key][0] - schedule_dict[key][1]
            for key in actual_schedule_dict:
                if airline == key:
                    my_dict[key][4] = actual_schedule_dict[key][0] - actual_schedule_dict[key][1]
