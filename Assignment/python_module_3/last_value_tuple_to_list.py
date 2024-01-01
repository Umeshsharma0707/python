#Write a Python program to replace last value of tuples in a list.

#program 

# creating a list of tuples 
list = [(1,2,3),(10,20,30),(5,6,7)]

replace_value = 45 # value to be replaced with the -1 element
# creating new list using list comprenhension
replaced_value_list = [(t[:-1]+ (replace_value,)) for t in list]

#printing the repaced list of tuples
print(replaced_value_list)