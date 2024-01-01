#Write a Python function to calculate the factorial of a
# number (anonnegative integer)

def factorial(n):
    if n < 0:
        return "not defined"
    elif n ==0 or n ==1: #factorial of 1 is 1
        return 1
    else:
        ans = 1
        for i in range(2,n+1):
            ans = ans*i
            
        return ans
    

n = int(input("enter any number : "))

result = factorial(n)
print("factorial : ",result)