#Strings
def strings ():
    string = ""
    for ch in string:
        ch.isdigit() #check if digit
        ch.isupper() #check if uppercase
        ch.islower() #check if lowercase
        ch.isspace() #check if space
        ch.isalpha() #check if alphabet from (a-z)
    
    string.find("") #Returns the lowest index in the string where substring substr is found. Returns -1 if substr is not found.
    string.split("") #Returns a list of the words in the string,    
                   #using sep as the delimiter string. If the delimiter sep is not provided, then the delimiter by default is a space.
                   #if sep is "@", split the string into two parts, before and after the "@"
    
    name = ""
    name_in_lowercase = name.lower() #lowercase string
    name_in_uppercase = name.upper() #uppercase string

    string[-1].isdigit()
    #checks if last character in the string is a digit

    for line in string.split('\n'):
        ...
    #goes through each line in a string

    from random import shuffle
    chars = list(string)
    shuffle(chars)
    result = ''.join(chars)
    #eg.
    #string = "yuika"
    #result = "ukayi"

    s = 'abc12321cba'
    s.replace('a', '')
    #bc12321cb

    my_str = "SMU SIS"
    for ch in my_str:
        print(ch, end=' ')
    #S M U S I S

    for ch in my_str:
        if (ch == "S"):
            ch = "*"
        print(ch, end=" ")
    #* M U   * I * 

    word = "stressed"
    reversed_word = word[::-1] #reversing word

    s = 'abcdefg'
    print(s[6:0:-1]) #gfedcb
    print(s[6:0:-2]) #gec
    print(s[6::-1])  #gfedcba
    print(s[6::-2])  #geca

    my_string = ""
    word = ""
    
    my_string += word + ";"
    my_string[0:len(my_string)-1]
    #tommy.goh@sis.smu.edu.sg;alan_wong@gmail.com
    my_string[0:len(my_string)]
    #tommy.goh@sis.smu.edu.sg;alan_wong@gmail.com;

    num = 20.4454
    num = str(round(num, 2))
    #20.45

#Lists and Tuples
def lists_tuples ():
    new_list = [int(i) for i in new_list] 
    #Changing every element to int in list

    tuple_of_strings = ("1", "2", "3")
    tuple_of_integers = tuple(int(item) for item in tuple_of_strings)
    #Changing every element to int in tuple

    my_tuple = (0, 1, 2)    
    my_list = list(my_tuple)
    my_list[1] = 100
    t_change = tuple(my_list)
    # (0, 100, 2)
    #To change values of an element in a tuple, convert tuple to list, update it, and turn it back into tuple.

    word_list = [("the", 1), ("check", 1), ("brown", 2), ("gary", 5)]
    if any(word[0] == "the" for word in word_list):
        ...
    #if the word "the" is in the first element of the word_list

    mylist = [4, 1, 7]
    mylist.sort()
    #Sort a list
    #[1, 4, 7]

    mylist.sort(reverse=True)
    #Reverse sort a list
    #[7, 4, 1]
    #if print(list1[-1]), it will print the last number which is 1

    mylist.sort(key=len)
    #Reverse sort a list by length
    #[ef, 123, ghikl]

    mytuple = (1, 11, 2)
    sortedTuple = sorted(mytuple)
    #Sort a tuple
    #[1, 2, 11]
    #Syntax: sorted(iterable, key=None, reverse=False)
    #returns a list

    mytuple = (1, 11, 2)
    reversed_tup = mytuple[::-1]
    #Use this to reverse tuple
    #(2, 11, 1)

    word_list = [('a', 14), ('the', 46), ('singpass', 18), ('on', 16), ('of', 15), ('to', 29)] 
    sorted_list = sorted(word_list, key = lambda x: x[1], reverse=True)
    #Sorting the tuple by the second element
    #[('the', 46), ('to', 29), ('singpass', 18), ('on', 16), ('of', 15), ('a', 14)]

    myList =["abc", "efg", "abc"]
    myList = [*set(myList)]
    #Remove any duplicates in the list

    myList = list(set(myList))
    #Remove any tuple duplicates in the list

    result =  max(myList, key=len)
    #Returns the longest element in a list
    result =  min(myList, key=len)
    #Returns the shortest element in a list

    list = []
    added_item = ""
    for i in range (len(list)):
        list = list[0:i] + [added_item] + list[i:]
    #Add a string/number/tuple into a certain position within the list

    list.insert(0, 10)
    #Syntax: list.insert(index, element)
    # Parameters: 
    # index: the index at which the element has to be inserted.
    # element: the element to be inserted in the list.

#File Handling
def file_handling():
    with open ("test.txt", "r") as file:
        for line in file:
            pass
        file.seek(0)
        for line in file:
            pass
    #This is to set the pointer index back to line 0 in order to read through the file again
    #0: sets the reference point at the beginning of the file  
    #1: sets the reference point at the current file position 
    #2: sets the reference point at the end of the file 
        
        line.lstrip("suffix") 
        #The rstrip() method removes any trailing characters (characters at the end a string), space is the default trailing character to remove.
        line.rstrip("suffix") 
        #The lstrip() method removes any leading characters (space is the default leading character to remove)
        line.startswith("suffix")
        #Check if the string starts with "suffix":
        line.endswith("suffix")
        #Check if the string ends with "suffix":

#Dictionaries
def dictionaries():
    from collections import defaultdict

    my_dict = {}
    reversed_dict = defaultdict(list)
    for key, value in my_dict.items():
        reversed_dict[value].append(key)
    #Reverse a dictionary that has repeated values

    sorted_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1])}
    #Sort a dictionary by value ascending
    reversed_dict = {k: v for k, v in sorted(my_dict.items(), key=lambda item: item[1], reverse=True)}
    #Sort a dictionary by value descending

    print(list(items = my_dict.items())[:5])
    #Returns the first 10 items in the dictionary
    #[('to', 684), ('a', 375), ('call', 336), ('your', 258), ('you', 237)]

#Other useful tools
def extras():
    data = []
    if isinstance(data[0], list): #this can check list/tuple/etc.
        pass
        #check if the current element is a list

    import itertools
    list(itertools.permutations([1, 2, 3]))
    #returns
    #[1, 2, 3]
    #[1, 3, 2]
    #[2, 1, 3]
    #[2, 3, 1]
    #[3, 1, 2]
    #[3, 2, 1]

    alphabets = 'abcdefghijklmnopqrstuvwxyz'