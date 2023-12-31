#Write a Python program to convert a list of characters into a
#string.

def list_to_string(list):
    #creating an empty string variable
    name_str = ""

    for i in list:
        name_str = name_str + i
    return name_str

# craeting a list of characters
list = ['u','m','e','s','h',' ','s','h','a','r','m','a']

# save output in the result variable
result = list_to_string(list)

print(list)
print("converting list to string")
print(result)
