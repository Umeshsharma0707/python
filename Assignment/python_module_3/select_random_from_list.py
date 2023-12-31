import random

#Write a Python program to select an item randomly from a list.

#program
#creating list
list = [10,20,"two",30,40]

print("original list : ",list)
#using random.choice method to choose randomly from list
random_select = random.choice(list)
#printing the random select
print("random select from list : ",random_select)