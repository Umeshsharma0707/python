"""Write a Python function to reverses a string if its length is a multiple of 4"""

str = input("enter a string : ")

if len(str) % 4 == 0:
    print("given string length is  multipe of 4")
    print("reversing string...")
    print(str[::-1])
else:
    print("given string length is not multipe of 4")
    print(str)
