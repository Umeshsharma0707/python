"""Write a Python function to insert a string in the middle of a string"""

str ="one three"
insert_str = "two"
print("original string")
print(str)
print(f"insert string : {insert_str}")
mid_point = len(str)//2

modified_string = str[:mid_point] + insert_str + " " + str[mid_point:]
print("""modified string :

""")
print(modified_string)
