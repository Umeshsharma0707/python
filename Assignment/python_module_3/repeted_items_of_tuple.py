#Write a Python program to find the repeated items of a tuple.

#progarm

tuple1 = (10,20,10,36,12,12,45,35,45,36,1,20)
print(tuple1) 
repeted_items = [] #empty list used to store repeated items of tuple

for item in tuple1:
    #count is a pre-built function that counts how many time
    # an element is present in a list or tuple  
    if tuple1.count(item) > 1:  #if count > 1
        if item not in repeted_items: #items stores in repeated list
            repeted_items.append(item)
    
#prints the repeted_items list
print("repeated elements are :",repeted_items)
