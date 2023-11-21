"""Write a python program to sum of the first n positive integers."""

n = int(input("enter how many numbers you want to add : "))
sum = 0
a = True
for i in range(1,n+1):
        num = int(input("enter a number to sum : "))
        if num<=0:
            print("entered number is negative")
            break

        
        else:
            sum  = sum + num
            print(f"sum : {sum}")
            


    
