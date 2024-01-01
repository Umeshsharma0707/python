#How Do You Traverse Through A Dictionary Object In Python?

#program

# CRAETING A DICT

dict = {
    1 : "apple",
    2 : "banana",
    3 : "cherry",
    4 : "mango"
}

# traversing the dictionary using for lop

for key,value in dict.items():
    print(f"key : {key}, value : {value}")