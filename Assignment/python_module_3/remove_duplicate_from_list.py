# Write a Python program to remove duplicates from a list.

# program 

# creating a list of fruits 
list = ['apple',"banana","pineapple","strawberry",'apple',"banana"]

# creating an empty list in which we add unique elements of duplicate list
unique_list = [] 

# fruit is an iterable variable 
for fruit in list:
    # when the fruit is not in unique list we add that fruit in the unique list
    if fruit not in unique_list:
        unique_list.append(fruit)


print(list)
print(unique_list)
