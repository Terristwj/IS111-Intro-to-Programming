weapons_dict = {
    "kunai": 5,
    "shuriken": 20,
    "hammer": 2,
    "spiked ball": 24,
    "metal spear": 4,
    "senbon": 84,
    "six-edged disc": 42,
    "crossbow": 1,
    "dual-swords": 3,
    "kunai chains": 2,
    "iron fan": 5,
    "scythe": 9,
    "scimitar": 12
}

# YOUR PROGRAM CODE GOES HERE
action = input("What would you like to do? [take/add] ")
action_list = ["take", "add"]
while action not in action_list:
    action = input("What would you like to do? [take/add] ")

if action == "take":
    input_weapon = input("Enter the name of the weapons: ")
    while input_weapon not in weapons_dict:
        print("\nWeapons not found in stocks!")
        input_weapon = input("Enter another weapon: ")
    
    print()
    number_taken = int(input("Enter the number of weapons you would like to take: "))
    while number_taken > weapons_dict[input_weapon]:
        print("The amount of weapons you are trying to take exceeds what you have already!")
        number_taken = int(input("Enter the number of weapons you would like to take: "))
    weapons_dict[input_weapon] -= number_taken
    if weapons_dict[input_weapon] == 0:
        print(f"\nYou have no more {input_weapon} left in the stocks.")
    else:
        print(f"\nYou are left with {weapons_dict[input_weapon]} of the following weapon: {input_weapon}")
else:
    input_weapon = input("Enter the name of the weapons: ")
    number_add = int(input("Enter the number of weapons you would like to add to the stocks: "))
    if input_weapon in weapons_dict:
        weapons_dict[input_weapon] += number_add
    else:
        weapons_dict[input_weapon] = number_add
    print(f"You have a total of {weapons_dict[input_weapon]} {input_weapon} left in the stock.")
