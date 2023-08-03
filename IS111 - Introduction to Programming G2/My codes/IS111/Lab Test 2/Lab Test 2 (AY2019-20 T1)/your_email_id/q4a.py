# Name:
# Email ID:

def store_family_relations(family_file):
    # Modify the code below.
    not_allowed_relations = ["fathermother","motherfather","sonson","daughterdaughter","sondaughter","daughterson"]
    relationship = {}
    with open(family_file) as f:
        for line in f:
            line = line.rstrip("\n")
            cols = line.split(":")
            
            parents = cols[0][1:-1].split(',')
            father = [parents[0], "father"]
            mother = [parents[1], "mother"]
            parents = [father, mother]

            children = cols[1].split(';')
            for i in range(len(children)):
                children[i] = children[i][1:-1].split(',')

                child_name = children[i][0]
                if children[i][1] == "M":
                    children[i] = [child_name, "son"]
                else:
                    children[i] = [child_name, "daughter"]

            family_list = parents + children
            for person in family_list:
                for another_person in family_list:
                    if person != another_person:
                        if person[1]+another_person[1] not in not_allowed_relations:
                            relation = person[1]
                            # print(person[0], another_person[0], person[1]+another_person[1])
                            relationship[person[0], another_person[0]] = relation

            # relationship = {}
            # for parent_index in range(len(parents)):
            #     for child_index in range(len(children)):
            #         parent = parents[parent_index]
            #         child = children[child_index]
            #         relation = (parent, child)

                    
            #         relationship[relation] = relationship_type
    return relationship
    