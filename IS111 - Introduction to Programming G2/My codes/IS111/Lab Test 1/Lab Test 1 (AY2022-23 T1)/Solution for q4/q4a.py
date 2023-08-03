rect1 = ("A", -4, 1, 3, 2)
rect2 = ("B", -1, -2, 4 ,3)

def is_overlapping(rect1, rect2):
    rect1_coords = [] 
    for w in range(rect1[3]):
        for h in range(rect1[4]): 
            rect1_coords.append((rect1[1]+w, rect1[2]+h))
    for w in range(rect2[3]): 
        for h in range(rect2[4]): 
            if (rect2[1]+w, rect2[2]+h) in rect1_coords: 
                return True 

    return False 

print(is_overlapping(rect1, rect2))
