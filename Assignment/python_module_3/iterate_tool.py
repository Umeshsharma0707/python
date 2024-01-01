import itertools # it is a tool for creating and for using iterate

my_dict = {
    '1': ['a', 'b'], 
    '2': ['c', 'd']
    }
# creates a list of strings by 
#joining each combination of letters
for x, y in itertools.product(*my_dict.values()):
    print(x + y)