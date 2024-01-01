#Write a Python function that checks whether a passed string is
# palindromeor not

#program 

def palidrome(str):

    clean_str = (str.replace(" ","")).lower()
    revers_str = clean_str[::-1]

    return clean_str == revers_str

str = input("enter string : ")

if palidrome(str):
    print("yes")
else:
    print("no")