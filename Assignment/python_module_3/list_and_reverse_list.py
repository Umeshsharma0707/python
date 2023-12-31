# que : What is List? How will you reverse a list?
# ans :
"""
-> List is a built-in datatype used to store collection of data
of different datatypes in a single variable.
-> it can store multiple items 
-> it is denoted by square brackets eg. list = [item1,items2...]

"""
# program to reverse an list

list = [1,2,3,4,5] # creating a list
print(list)
new_list = list[::-1] # using slicing technique
print(new_list) # printing reverse list
