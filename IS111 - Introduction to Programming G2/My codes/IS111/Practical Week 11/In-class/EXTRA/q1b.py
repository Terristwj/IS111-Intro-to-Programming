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

    col_left_num = int(seat[1:]) - 1
    seat_left = seat[0] + str(col_left_num)
    if col_left_num > 0:
        if seat_left in my_dict:
            print("The person seating on the left side of that person is", my_dict[seat_left])
        else:
            print("Seat not taken on the left side")
    else:
        print("There is no seat at the left side")
    
    col_right_num = int(seat[1:]) + 1
    seat_right = seat[0] + str(col_right_num)
    if col_right_num < 26:
        if seat_right in my_dict:
            print("The person seating on the right side of that person is", my_dict[seat_right])
        else:
            print("Seat not taken on the right side")
    else:
        print("There is no seat at the right side")

else:
    print("Seat not taken")
