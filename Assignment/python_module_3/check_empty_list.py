#Write a Python program to check a list is empty or not.

#program 

# creatiuing a function 
def is_list_empty(list): # passing list as parameter
    #checking if the length of list is equal to 0 or not
    if len(list) == 0:
        return True # gets result as boolean 
    else:
        return False


non_empty_list = [10,30,30] # non empty list
empty_list = [] # empty list

# storing output of empty list
empty_list_output = is_list_empty(empty_list)

# storing output of non empty list
non_empty_list_output = is_list_empty(non_empty_list)

# if list is empty
if empty_list_output == True:
    print("list is empty ")
else:
    print("list is not empty")

if non_empty_list_output == True:
    print("list is empty ")
else:
    print("list is not empty")
