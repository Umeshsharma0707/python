"""Write a Python program to get a single string from two given strings,
separated by a space and swap the first two characters of each string."""

s1 = input("enter a string : ")
s2 = input("enter a string : ")

str1 = s1[2:] +s2[2:]
str2 = s2[2:] +s1[2:]

result = str1 +' ' + str2

print(result)


