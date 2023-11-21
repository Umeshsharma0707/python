"""Write a Python program to get the Fibonacci series of given range."""

n = int(input("enter any number : "))

a,b = 1,1
c = 1
print(f"{a} {b}",end=" ")
for i in range(0,n-2):
    c = a + b
    print(f"{c}",end = " ")
    a = b
    b = c 
    
            
