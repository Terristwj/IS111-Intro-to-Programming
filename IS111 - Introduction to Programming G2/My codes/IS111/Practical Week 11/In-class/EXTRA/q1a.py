my_dict = {}

with open("seating_plan.txt") as f:
    for line in f:
        line = line.rstrip("\n")
        cols = line.split(",")
        my_dict[cols[0]+cols[1]] = cols[2]
# print(my_dict)

seat_row = input("Enter a letter (from A to E) :")
seat_col = input("Enter a seat number (from 1 to 25) :")
seat = seat_row + seat_col
print()

if seat in my_dict:
    print("The person seated at the seat " + seat + " is " + my_dict[seat])
else:
    print("Seat not taken")