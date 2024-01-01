#Write a Python script to concatenate following dictionaries to
# create anew one.

#program
#creating three dictionaries
dict1 = {
    1 : "apple",
    2 : "kiwi"
}
dict2 = {
    3 : "banana",
    4 : "papaya"
}
dict3 = {
    5 : "pinapple",
    6 : "cherry"
}

# concatinating using the update() function
new_dict = dict1.copy() # copy the first dict
new_dict.update(dict2) # then add with the dict 2
new_dict.update(dict3) # then with dict3

#printing the concatinated dict
print(new_dict)