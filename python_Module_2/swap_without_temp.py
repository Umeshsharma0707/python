"""Write python program that swap two number with temp variable and
without temp variable."""

n1 = int(input("enter num 1 :"))
n2 = int(input("enter num 2 :"))

print("before swap :")

print(f"Num1 = {n1}")
print(f"Num2 = {n2}")
n1 = n1+n2
n2 = n1-n2
n1 = n1-n2

print("after swap")

print(f"Num1 = {n1}")
print(f"Num2 = {n2}")
