def read_items_from_file(file_name):
    """
    This function processes the given file and returns 
    a list of tuples containing all the items found
    in the given file. 
    Each tuple in the returned list contains the following elements:
    (1) title (2) library (3) format (4) language (5) status (6) borrower (7) due date. Note that it is possible for borrower and due date to be empty strings.
    """
    
    # The code below shows a list containing only one tuple.
    # You need to modify the code so that the returned list 
    # contains all the items found in the given file.
    with open(file_name) as f:
        my_list = []
        for line in f:
            line = line.rstrip("\n")
            cols = line.split("\t")
            if len(cols) > 4:
                my_tuple = [cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6]]
            else:
                my_tuple = [cols[0], cols[1], cols[2], cols[3]]
            my_list.append(my_tuple)
    return my_list
    # return [("About a Boy", "Bishan Public Library", "Books", "Chinese", "On Loan", "Liam", "12/11/2017")]
    
    
def read_items_of_given_library_from_file(file_name, library):
    """
    This function processes the given file and returns 
    a list of tuples containing only the items from the specified
    library. 
    Each tuple in the returned list contains the following elements:
    (1) title (2) library (3) format (4) language (5) status (6) borrower (7) due date. Note that it is possible for borrower and due date to be empty strings.
    """
    
    # You need to modify the code below.
    with open(file_name) as f:
        my_list = []
        for line in f:
            line = line.rstrip("\n")
            cols = line.split("\t")
            if cols[1] == library:
                if len(cols) > 4:
                    my_tuple = [cols[0], cols[1], cols[2], cols[3], cols[4], cols[5], cols[6]]
                else:
                    my_tuple = [cols[0], cols[1], cols[2], cols[3]]
                my_list.append(my_tuple)
    return my_list
    # return [("About a Boy", "Bishan Public Library", "Books", "Chinese", "On Loan", "Liam", "12/11/2017")]
    
def get_item_counts_by_x(file_name, num):
    with open(file_name) as f:
            my_dict = {}
            my_list = []
            for line in f:
                line = line.rstrip("\n")
                cols = line.split("\t")
                if cols[num] not in my_dict:
                    my_dict[cols[num]] = 1
                else:
                    my_dict[cols[num]] += 1

            for key in my_dict:
                my_list.append([key, my_dict[key]])
    return my_list

def get_item_counts_by_library(file_name):
    """
    This function processes the given file and returns
    a list of tuples. Each tuple contains two elements:
    (1) the name of a library (2) the number of items 
    from that library.
    Basically the function counts the number of items from
    each library and finally returns all the counts.
    """
    
    # You need to modify the code below.
    return get_item_counts_by_x(file_name, 1)
    # return [('Bishan Public Library', 1)]
    
   

def get_item_counts_by_format(file_name):
    """
    This function processes the given file and returns
    a list of tuples. Each tuple contains two elements:
    (1) a format (2) the number of items of that format.
    Basically the function counts the number of items 
    of each format and finally returns all the counts.
    """
    
    # You need to modify the code below.
    return get_item_counts_by_x(file_name, 2)
    # return [('Books', 1)]
    
    
def get_item_counts_by_language(file_name):
    """
    This function processes the given file and returns
    a list of tuples. Each tuple contains two elements:
    (1) a language (2) the number of items in that language.
    Basically the function counts the number of items 
    in each language and finally returns all the counts.
    """
    
    # You need to modify the code below.
    return get_item_counts_by_x(file_name, 3)
    # return [('English', 1)]
    
    
def read_loans_from_file_to_dict(file_name):
    """
    This function reads a file that contains the loan history
    of many items. The function returns a dictionary where
    the keys are the titles of items and the values are lists of loan records of the corresponding items.
    Specifically, for each item, we use the title of the item as its 
    key. The value associated with the title is a list of tuples.
    Each tuple contains the following pieces of information: 
    (1) borrower (2) borrowed date (3) returned date.
    Note that the returned date could be empty if the item has not
    been returned by that borrower.
    """
    
    # You need to modify the code below.
    with open(file_name) as f:
            my_dict = {}
            # Key = title
            # Value = list of tuple of loan records

            for line in f:
                line = line.rstrip("\n")
                cols = line.split("\t")
                if cols[0] not in my_dict:
                    my_dict[cols[0]] = [(cols[1], cols[2], cols[3])]
                else:
                    my_dict[cols[0]].append((cols[1], cols[2], cols[3]))

    return my_dict
    # return {"About a Boy":[("Liam", "09/10/2017", "11/10/2017")]}
    
    