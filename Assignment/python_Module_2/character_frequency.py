"""Write a Python program to count the number of characters (character
frequency) in a string"""

str = input("enter a string : ")

char_freq={}

for char in str:
    if char in char_freq:
        char_freq[char] +=1
    else:
        char_freq[char]=1


for char,freq in char_freq.items():
    print(f"{char} : {freq}")

