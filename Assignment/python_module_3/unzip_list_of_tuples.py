#Write a Python program to unzip a list of tuples into individual
# lists.

#program 

list1= [("one",1),("two",2),("three",3)]

print(list1)


zipped_list = list(zip(*list1))

print(zipped_list)