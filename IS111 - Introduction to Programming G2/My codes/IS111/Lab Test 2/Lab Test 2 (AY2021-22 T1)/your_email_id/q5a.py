# Name:
# Email ID:
    
def get_persons(person_list, n):
    # Write your code here.
    enclosed_people = []
    if n < len(person_list):
        for i in range(len(person_list)):
            current_gender = person_list[i][1]
            clockwise_starting_index = i + 1
            anticlockwise_starting_index = i - 1
            
            total_opposite_genders = 0
            # Moving clockwise
            while clockwise_starting_index <= i + n - 1:
                # print(clockwise_starting_index, i + n - 1, len(person_list))
                if clockwise_starting_index >= len(person_list):
                    # print(len(person_list)-clockwise_starting_index)
                    next_person_gender = person_list[len(person_list)-clockwise_starting_index][1]
                else:
                    next_person_gender = person_list[clockwise_starting_index][1]
                if next_person_gender != current_gender:
                    total_opposite_genders += 1
                else:
                    break
                clockwise_starting_index += 1
            
            # Moving anti-clockwise
            while anticlockwise_starting_index >= i - n + 1:
                # print(anticlockwise_starting_index, i - n + 1, len(person_list))
                next_person_gender = person_list[anticlockwise_starting_index][1]
                if next_person_gender != current_gender:
                    total_opposite_genders += 1
                else:
                    break
                anticlockwise_starting_index -= 1

            # print(total_opposite_genders)

            if total_opposite_genders >= n:
                enclosed_people.append(person_list[i])
    return enclosed_people

# DO NOT MODIFY THE CODE BELOW!
if __name__ == "__main__":
    def run_test_case(tc_num, person_list, n, expected_output, expected_type):
        print('*'*40)
        print(f'Test Case {tc_num}: get_persons("{person_list}", {n})')
        print()
        print(f'Expected (in any order): {expected_output}')
        result = get_persons(person_list, n)
        print(f'Actual:   {result}')
        print()
        print(f'Expected return type : {expected_type}')
        print(f"Actual return type   : {type(result)}")
        print()
        
    person_list = [('john', 'M'), ('alex', 'F'), ('don', 'M'), ('val', 'F'), ('ann', 'F')]
    expected_list = [('don', 'M'), ('john', 'M'), ('alex', 'F')]
    run_test_case(1, person_list, 2, expected_list, "<class 'list'>")

    person_list = [('john', 'M'), ('alex', 'F'), ('don', 'M'), ('val', 'F'), ('ann', 'F')]
    expected_list = [('john', 'M'), ('don', 'M')]
    run_test_case(2, person_list, 3, expected_list, "<class 'list'>")

    person_list = [('a', 'M'), ('b', 'F'), ('c', 'M'), ('d', 'M'), ('e', 'M'), ('f', 'M'), ('g', 'M'), ('h', 'M')]
    expected_list = [('b', 'F')]
    run_test_case(3, person_list, 7, expected_list, "<class 'list'>")

    person_list = [('a', 'M'), ('b', 'F'), ('c', 'M'), ('d', 'M'), ('e', 'M'), ('f', 'M'), ('g', 'M'), ('h', 'M')]
    expected_list = []
    run_test_case(4, person_list, 8, expected_list, "<class 'list'>")
    

