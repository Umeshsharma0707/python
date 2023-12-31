#Write a Python function that takes a list and returns a new list
#with uniqueelements of the first list.

#program

list = [100,150,"apple","cricket",100,"apple","kiwi","car"]
unique_list = []

for i in list:
    if i not in unique_list:
        unique_list.append(i)


print("old list :")
print(list)
print("unique list")
print(unique_list)

