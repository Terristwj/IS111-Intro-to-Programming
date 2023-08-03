# Name:
# Email ID:

def read_courses(filename):
    # Replace the code below with your implementation.
    my_dict = {}
    with open(filename) as f:
        for line in f:
            line = line.rstrip('\n')
            cols = line.split('|')

            year_term = cols[0].split('-')

            # print(cols)

            name = cols[1]
            subject = cols[2]
            year = int(year_term[0])
            term = int(year_term[1][1])
            credit = int(cols[3])
            score = float(cols[4])

            if name not in my_dict:
                my_dict[name] = []
            my_tuple = (subject, year, term, credit, score)
            my_dict[name].append(my_tuple)

    return my_dict
