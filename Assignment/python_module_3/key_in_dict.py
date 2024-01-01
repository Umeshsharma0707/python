#Write a Python script to check if a given key already
# exists in adictionary.

#program

def isKeyExists(dictionary,key):
    
    #checks if the key is in dict or not
    if key in dictionary:
        return True

#craeting a dictionary
dict = {'a':"apple","b":"banana","c":"cherry"}

#key to check is in dict or not
key1 = 'd'
key2 = 'b'


output1 = isKeyExists(dict,key1)
output2 = isKeyExists(dict,key2)
if output1 == True:
    print(f"yes \'{key1} \' is exists in dictionary")
else:
    print("not exists")

if output2 == True:
    print(f"yes \'{key2} \' is exists in dictionary")
else:
    print("not exists")