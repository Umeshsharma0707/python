#Write a Python program to check whether a list contains a sub
#list

#program 

list = [10,25,36,86,45,35]
sub_list = [25,36]
result = False
for i in range(len(list) - len(sub_list)+1):
    if list[i:i + len(sub_list)] == sub_list:
        result = True
        break

print(result)
