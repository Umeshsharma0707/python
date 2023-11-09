"""
Write a Python program to check if a number is positive, negative or zero
"""

print("this program helps you to find number is positive,negative or zero")

n = int(input("enter any number "))

if n<0:
    print(f"{n} : is negative number")
elif n==0:
    print(f"{n} : is a zero")
elif n>0:
    print(f"{n} : is positive number")
