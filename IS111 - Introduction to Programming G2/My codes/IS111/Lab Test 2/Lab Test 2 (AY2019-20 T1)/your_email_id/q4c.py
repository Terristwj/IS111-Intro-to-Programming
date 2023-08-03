# Name:
# Email ID:

def get_relation(family_dict, p1, p2):
    # Modify the code below.
    family_members = ['A', 'B', 'C', 'D']

    pos1 = family_members.index(p1)
    pos2 = family_members.index(p2)
    # print(pos1, pos2)

    if pos1 < pos2:
        link = family_members[pos1:pos2+1]
    else:
        link = family_members[pos2:pos1+1]
        link.reverse()
    relations = []
    for i in range(len(link)-1):
        relations.append(family_dict[link[i], link[i+1]])
    # print(relations)

    while len(relations) != 1:
        with open('relation_mapping.txt') as f:
            for line in f:
                line = line.rstrip("\n")
                relationships = line.split(":")[0][1:-1].split(",")
                relationships = [relationships[0], relationships[1]]
                result = line.split(":")[1]
                
                if len(relations) == 2:
                    if relations == relationships:
                        return result
                else:
                    # print(relations[:2], relationships)
                    if relations[:2] == relationships:
                        # print(relations)
                        relations.pop(0)
                        relations.pop(0)
                        relations.insert(0, result)
                # print(relationships, result)
    return relations
    
    