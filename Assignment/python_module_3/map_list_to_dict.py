# Write a Python program to map two lists into a dictionary

#program

#two list

key_list = ['a','b','c']
value_list = [1,2,3]
# zip combines element into pairs and using list comprenhsion
dict1 = {key : value for key,value in zip(key_list,value_list)}

# printing the dictionary
print(dict1)