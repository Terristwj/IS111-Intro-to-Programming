# Name:
# Email ID:
import math

def get_all_tank_sizes(tanks):
    # Write your code here.
    tank_records = []
    for tank in tanks:
        absolute_gallon = 231
        volume = 1
        for measure in tank:
            volume *= measure
        volume /= absolute_gallon
        volume = math.floor(volume)
    
        if volume < 20:
            tank_records.append("S")
        elif volume < 50:
            tank_records.append("M")
        else:
            tank_records.append("L")
            
    return tank_records

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    tc_num = 0

    tc_num += 1
    print('-' * 40)
    
    tanks = [(12, 6, 8), (24, 12, 18), (36.375, 18.375, 19)]
    print(f'Test Case {tc_num} : get_all_tank_sizes ({tanks})')
    result = get_all_tank_sizes (tanks)
    print("Expected : ['S', 'M', 'L']")
    print(f"Actual   : {result}")
    
    print()
    
    print("Expected return type : <class 'list'>")
    print(f"Actual return type   : {type(result)}")

    print()
    print("Expected return type of the first element of the list : <class 'str'>")
    print("Actual return type of the first element of the list   : ", end="")
    if (isinstance(result, list)):
        print(type(result[0]))
    else:
        print("N/A")
    
    print()

    tc_num += 1
    print('-' * 40)
    
    tanks = []
    print(f'Test Case {tc_num} : get_all_tank_sizes ({tanks})')
    result = get_all_tank_sizes (tanks)
    print("Expected : []")
    print(f"Actual   : {result}")
    print()


