from q3a import check_diversity

print()
print('-' * 20)
print()

team = [('Xavier', 'M', 'Chinese', 'Freethinker'), 
        ('Noah', 'M', 'Jew', 'Judaism'),
        ('Hui Ling', 'F', 'Chinese', 'Buddhism'),
        ('Siti', 'F', 'Malay', 'Islam'),
        ('Aryan', 'M', 'Indian', 'Hinduism')]

print("Test Case 1: check_diversity(team) where")
print("\tteam = " + str(team))

print()

result = check_diversity(team)
print('Expected: True')
print('Actual:   ' + str(result))

print("Expected type of returned value: <class 'bool'>")
print('Actual type of returned value:   ' + str(type(result)))

print()
print('-' * 20)
print()

team = [('Xavier', 'M', 'Chinese', 'Freethinker'), 
        ('Faith', 'F', 'Chinese', 'Christianity'),
        ('Li Wen', 'F', 'Chinese', 'Freethinker'),
        ('Siti', 'F', 'Malay', 'Islam'),
        ('Nicholas', 'M', 'Chinese', 'Freethinker')]


print("Test Case 2: check_diversity(team) where")
print("\tteam = " + str(team))

print()

result = check_diversity(team)
print('Expected: False')
print('Actual:   ' + str(result))

print()
print('-' * 20)
print()