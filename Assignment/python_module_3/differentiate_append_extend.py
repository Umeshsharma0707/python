# Differentiate between append () and extend () methods?
"""
ans : 
both methods are used to add the elements in the list but,
append() is used to add single elment at the end of the list
and
extend() method is used to add the all elements of the list or an iterable tuple 
at the end of the list 
"""

# example :

list = [10,30,50,60]
print(list)
# we need to add 70 in the above list at the end
#using the append method

list.append(70) # add the element at the end of list

print(list) # printing list again

# example of extend :

l1 = [10,20,30]
l2 = [40,50,60]

# add the l2 element with l1

l1.extend(l2) # extends the list2 with l1
print(l1)