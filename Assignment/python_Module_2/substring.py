s1 = input("enter a string")
s2 = input("enter a substring")

s = s1.split()

count = 0
for i in s:
    if s2 ==i:
        count+=1


print(f"total no : {count}")
