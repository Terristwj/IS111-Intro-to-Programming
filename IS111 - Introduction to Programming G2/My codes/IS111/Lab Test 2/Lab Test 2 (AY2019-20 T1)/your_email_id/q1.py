# Name:
# Email ID:

def compute_product(num_list):
    # Modify the code below.
    product = 1
    if num_list:
        for i in range(len(num_list)):
            if num_list[i] % 2 == 1:
                product *= num_list[i]
    return product
    