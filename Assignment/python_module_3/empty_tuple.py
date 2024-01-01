#Write a Python program to remove an empty tuple(s) from a list
# of tuples.

#program
#creating a list of tuples with some empty tuples 
list = [(10,20,30),(),(20,3,0),()]
print(list)

for t in list: # t is the tuples in list
    if len(t) == 0: # if length of tuple ==0
        list.remove(t) #then remove that tuple

print("\n list after removing empty tuples \n")
# now print the list
print(list)