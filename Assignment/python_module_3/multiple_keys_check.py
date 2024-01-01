#Write a Python program to check multiple keys exists in a
# dictionary

#program

#creating a list of  50 keys 

def check_key(dict1,key):
    if key in dict1:
        return True
    else:
        return False

dict1 = {key : f"value {key}" for key in range(1,51)}


# getting key from user



re = True

while re==True:
    key = input("enter key to serch if its exists or not : ")
    result = check_key(dict1,key)
    if result == True:
        print(f"yes \'{key}\' is exists ")
    else:
        print(f"No \'{key}\' is not exists")

    user = input("do you want to serch again [y/n] :")

    if user == 'y' or "Y":
        re = True
    else:
        re = False
        print("bye")