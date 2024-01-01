#Write a Python script to print a dictionary where the keys are
# numbersbetween 1 and 15.

#program 
#generating keys using dict comprehension
dict = {key : f"value {key}" for key in range(1,16)}

print(dict)