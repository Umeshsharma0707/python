#• Write a Python program to print all unique values in a dictionary

#program 

dict1 = {
    1 : 'a',
    2 : 'c',
    3 : 'd',
    4 : 'a',
    5 : 'c'
}

#converting the values into set
unique_values = set(dict1.values())

# printing the unique values

print(unique_values)


