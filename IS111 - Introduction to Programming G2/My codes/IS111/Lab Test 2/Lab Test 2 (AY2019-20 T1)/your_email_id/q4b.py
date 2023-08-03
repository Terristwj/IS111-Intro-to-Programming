# Name:
# Email ID:

def get_relation_through_link(family_dict, link):
    # Modify the code below.
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
    