# Write a Python program to find the highest 3 values in a
# dictionary
#program

#creating simple dict
my_dict = {'a': 10, 'b': 30, 'c': 20, 'd': 40, 'e': 15}

#get value in list
value_list = list(my_dict.values())
#print value list
print(value_list)
#short values of list
value_list.sort()
#printing the highest values
print(value_list[-3:])