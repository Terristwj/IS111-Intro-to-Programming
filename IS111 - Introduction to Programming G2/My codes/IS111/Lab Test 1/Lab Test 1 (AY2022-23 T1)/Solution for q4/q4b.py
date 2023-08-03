from q4a import is_overlapping

# def find_overlapping_pairs(mylist): 
#     results = [] 
#     for i in mylist: 
#         for j in mylist: 
#             if i != j and is_overlapping(i,j):
#                 if (i[0],j[0]) not in results and (j[0],i[0]) not in results: 
#                     results.append((i[0],j[0]))

#     return results 

def find_overlapping_pairs(mylist): 
    results = [] 
    for i in range(len(mylist)): 
        for j in range(i+1, len(mylist)): 
            if is_overlapping(mylist[i], mylist[j]): 
                results.append((mylist[i][0],mylist[j][0]))
    return results 