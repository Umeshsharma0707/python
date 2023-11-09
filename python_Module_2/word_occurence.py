"""Write a Python program to count the occurrences of each word in a given
sentence
"""

str = input("enter a string : ")
s = str.split()
print(s)
word_counter = {}

for word in s:
    if word in word_counter:
        word_counter[word]+=1
    else:
        word_counter[word]=1

        
for word,count in word_counter.items():
    print(f"{word} : {count}")

