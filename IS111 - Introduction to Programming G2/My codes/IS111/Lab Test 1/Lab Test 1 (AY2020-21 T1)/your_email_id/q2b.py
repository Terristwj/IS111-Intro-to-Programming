# Name:
# Email ID:

def get_max_of_min(list_of_num_tuples):
    # Replace the code below with your implementation.
     # Note: You’re NOT allowed to use either min()or max()to solve this problem.
    if list_of_num_tuples:
        mins_list = []
        for tuple in list_of_num_tuples:
            smallest = tuple[0]
            for num in tuple:
                if num < smallest:
                    smallest = num
            mins_list.append(smallest)

        max_min = mins_list[0]
        for num in mins_list:
            if num > max_min:
                max_min = num
        return max_min
    return None