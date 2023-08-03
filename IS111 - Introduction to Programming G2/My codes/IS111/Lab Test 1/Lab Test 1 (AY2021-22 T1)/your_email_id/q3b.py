# Name:
# Email ID:

import q3a

def swap_members(team1, team2):
    # Replace the code below with your implementation.
    team1_copy = reset_team(team1)
    team2_copy = reset_team(team2)

    student_pair = ()
    
    for i in range(len(team1)):
        for student in team2:
            team1_copy[i] = student
            # print(1, i, q3a.check_diversity(team1_copy))
            if q3a.check_diversity(team1_copy):
                team2_copy.remove(student)
                for i2 in range(len(team2)-1):
                    for student2 in team1:
                        team2_copy[i2] = student2
                        # print(2, i2, q3a.check_diversity(team2_copy))
                        if q3a.check_diversity(team2_copy):
                            print(team1_copy)
                            print(team2_copy)
                            return (student[0], student2[0])
                    team2_copy = reset_team(team2)
        
    if student_pair:
        return (student_pair)
    else:
        return None

def reset_team(team):
    new_team = []
    for student in team:
        new_team.append(student)
    return new_team
            