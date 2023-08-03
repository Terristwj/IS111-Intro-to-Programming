from q3b import swap_members

print()
print('-' * 20)
print()

team1 = [('Xavier', 'M', 'Chinese', 'Freethinker'), 
         ('Faith', 'F', 'Chinese', 'Christianity'),
         ('Li Wen', 'F', 'Chinese', 'Freethinker'),
         ('Siti', 'F', 'Malay', 'Islam'),
         ('Nicholas', 'M', 'Chinese', 'Freethinker')]
team2 = [('Ismail', 'M', 'Malay', 'Islam'),
         ('Boon Kiat', 'M', 'Chinese', 'Freethinker'),
         ('Julian', 'M', 'Chinese', 'Freethinker'),
         ('Sajid', 'M', 'Indian', 'Islam'),
         ('Aisha', 'F', 'Malay', 'Islam')]

print('Test Case 1: swap_members(team1, team2) where')
print('\tteam1 = ' + str(team1))
print('\tteam2 = ' + str(team2))

print()

result = swap_members(team1, team2)
print('Expected: None')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'NoneType'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

team1 = [('Xavier', 'M', 'Chinese', 'Freethinker'), 
         ('Faith', 'F', 'Chinese', 'Christianity'),
         ('Li Wen', 'F', 'Chinese', 'Freethinker'),
         ('Siti', 'F', 'Malay', 'Islam'),
         ('Nicholas', 'M', 'Chinese', 'Freethinker')]
team2 = [('Ismail', 'M', 'Malay', 'Islam'),
         ('Boon Kiat', 'M', 'Chinese', 'Christianity'),
         ('Benjamin', 'M', 'Eurasian', 'Christianity'),
         ('Sajid', 'M', 'Indian', 'Islam'),
         ('Aisha', 'F', 'Malay', 'Islam')]

print('Test Case 2: swap_members(team1, team2) where')
print('\tteam1 = ' + str(team1))
print('\tteam2 = ' + str(team2))

print()

result = swap_members(team1, team2)
print("Expected: ('Faith', 'Benjamin') or ('Li Wen', 'Benjamin') or ('Li Wen', 'Sajid')")
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'tuple'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

