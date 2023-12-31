"""Write a Python program to count the number of strings where
the string length is 2 or more and the first and last character
are same from a givenlist of strings."""

# program 


def count_string_same_letters(strings): #passing list as name string
    count = 0 # counter

    # string is a iterable variable 
    for string in strings: # strings is a list passed in the function
        #if string length is greater than 2 and
        #first and last letter is same
        if len(string) > 2 and string[0] == string[-1]: 
            count +=1

    return count



list = ["hello","1221",'abba',"tweet","three","kick"]

output = count_string_same_letters(list)

print(f"total strings with first and last same letters are :{output}")
