# Name:
# Email ID:

def trace_contacts(patient, history):
    # Replace the code below with your implementation.
    if patient and history:
        infected = []
        infected_names = []
        for rec in history:
            if patient in rec:
                if rec[2] > -6:
                    if rec[0] == patient:
                        infected.append([rec[1], rec[2] + 2])
                    else:
                        infected.append([rec[0], rec[2] + 2])
        
        for list in infected:
            infected_names.append(list[0])


        for rec in history:
            for infect in infected:
                if infect[0] in rec:
                    if rec[2] >= infect[1]:
                        if rec[0] == infect[0]:
                            if rec[1] not in infected_names:
                                infected.append([rec[1], rec[2] + 2])
                                infected_names.append(rec[1])
                        else:
                            if rec[0] not in infected_names:
                                infected.append([rec[0], rec[2] + 2])
                                infected_names.append(rec[0])
        
        print(infected)

        for list in infected:
            if list[0] not in infected_names:
                infected_names.append(list[0])

        return infected_names
    else:
        return []