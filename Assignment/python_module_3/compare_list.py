#How will you compare two lists?

"""
we will compare two list by comparing their elements 
if both list have same elements on same indexes 
then both lists are same.
but in both list the elements are same but their index are different,
than we have to sort both the list and then compare  
"""
#program

n = int(input("enter the size of list1 : "))
list1 = []
list2 = []

for i in range(1,n+1):
    item = input(f"enter item {i} : ") 
    list1.append(item)

n = int(input("enter the size of list2 : "))
for i in range(1,n+1):
    item = input(f"enter item {i} : ") 
    list2.append(item)

print(list1)
print(list2)

#sorting the list
list1.sort()
list2.sort()
print("after sorting")
print(list1)
print(list2)

if list1 == list2: # comparing both the list
    print("both are same")
else:
    print("both are not same")