print("a program to print all odd number :")


for i in range(1,10):
    if i%2==0:
        continue
    else:
        print(f"odd number : {i}")


print("a program to print all even number :")


for i in range(1,10):
    if i%2==0:
        print(f"even number : {i}")
    else:
        continue
