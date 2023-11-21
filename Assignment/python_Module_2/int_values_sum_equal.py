"""Write a Python program that will return true if the two given
integervalues are equal or their sum or difference is 5."""

n1 = int(input("enter a number : "))
n2 = int(input("enter second number : "))

if n1 == n2 or (n1-n2)==5 or (n1+n2) == 5:
    result = True
    print(result)
else:
    result = False
    print(result)
