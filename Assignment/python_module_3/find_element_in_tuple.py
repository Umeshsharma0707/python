#Write a Python program to check whether an element
#exists within a tuple.

#program 

def find_element(element):
    serch_item = element.lower()

    for i in t1:
        if i == serch_item:
            return True      
            break
        


#creating a tuple
t1 = ("apple","banana","pineapple","kiwi","papaya","icecream")
element = input("enter name you want to search : ")
output = find_element(element)

if output == True:
    print("item is present")
else:
    print("item is not present")