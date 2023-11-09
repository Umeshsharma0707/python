
sum = 0
a = True

while a==True:
    n1 = int(input("enter any integer : "))
    n2 = int(input("enter any integer : "))
    n3 = int(input("enter any integer : "))
    if n1 == n2 or n1 == n3 or n2 == n3:
        print("two numbers are same choose different numbers!")
        print("otherwise cant't divide")
        
    else:
        sum = n1 + n2 + n3
        print(f"sum is : {sum}")

    print("do you want to try again : type [y/n] : ")    
    re = input("enter [y/n] : ")

    if re == 'y':
        a = True
    else:
        a = False
        print("ok good bye!")
