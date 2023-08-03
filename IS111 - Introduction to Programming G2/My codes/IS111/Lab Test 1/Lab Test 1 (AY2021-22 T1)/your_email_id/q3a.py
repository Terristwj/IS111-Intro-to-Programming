# Name:
# Email ID:

def check_diversity(team):
    # Replace the code below with your implementation.

    # Gender
    males = 0
    females = 0
    for person in team:
        if person[1] == "M":
            males += 1
        else:
            females += 1

    gender_check = False
    if males == 3 and females == 2:
        gender_check = True
    if males == 2 and females == 3:
        gender_check = True

    # Race
    races = []
    for person in team:
        race = person[2]
        if race not in races:
            races.append(race)
    
    race_check = False
    if len(races) >= 3:
        race_check = True
    
    # Religion
    religions = []
    for person in team:
        religion = person[3]
        if religion != "Freethinker":
            if religion not in religions:
                religions.append(religion)
                
    religion_check = False
    if len(religions) >= 2:
        religion_check = True

    if gender_check and race_check and religion_check:
        return True
    return False