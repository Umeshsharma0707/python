#Write a Python program to combine two dictionary adding
# values forcommon keys.
# o d1 = {'a': 100, 'b': 200, 'c':300} o d2 = {'a': 300, 'b':
# 200,’d’:400}

# program 

d1 = {'a': 100, 'b': 200, 'c': 300}
d2 = {'a': 300, 'b': 200, 'd': 400}

combine_dict ={}

for key in set(d1.keys()).union(d2.keys()):
    combine_dict[key] = d1.get(key,0) + d2.get(key,0)

print(d1)
print(d2)
print(combine_dict)