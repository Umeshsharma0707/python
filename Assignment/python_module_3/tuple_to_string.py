#Write a Python program to convert a tuple to a string

#program
#creating tuple
t1 = ('u','m','e','s','h') #tuple

str = ""  #empty string variable
for i in t1: # i is the items of tuple
    str = str + i # concatinating the string 

print(type(str)) # type of str
print(str) # printing the string
