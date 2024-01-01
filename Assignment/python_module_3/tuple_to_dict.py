#How will you create a dictionary using tuples in python?
#ans :
"""
when a tuple contains a key-value pair then we can easily
convert the tuple to diuctionary using the dict constructor

"""

# for example
# creating three tuple each contains key value pair elemnets

t1 = (1,"apple")
t2 = (2,"kiwi")
t3 = (3,"mango")

#now converting the tuples into dictionary
#using the dict constructor
#passsing list of tuple 
dict1 = dict([t1,t2,t3])

#printing the dict
print(dict1)