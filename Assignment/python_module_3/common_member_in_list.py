#Write a Python function that takes two lists and returns true if
#they have at least one common member

# program 

list1 = ["apple","kiwi","pineapple"]
list2 = ["potato","onion","kiwi","apple","banana"]

# if same elemnts in both the list then we change the value as True
result = False


for i in list1: # loop for list1
    for j in list2: # loop for list2
        if i == j: # comparing items of both list
            result = True # if same returns true

#printing the output 
print("Output : ",result)
        