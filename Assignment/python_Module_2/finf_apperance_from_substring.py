"""Write a Python program to find the first appearance of the substring 'not'
and 'poor' from a given string, if 'not' follows the 'poor', replace the whole
'not'...'poor'substring with 'good'. Return the resulting string.
Write a Python function that takes a list of words and returns the length of
the longest one."""

str = "the weather is not poor but the food is poor"
print("original String")
print(str)
modify_string=""
not_index = str.find('not')
poor_index = str.find('poor')

if not_index!= -1 and poor_index!=-1 and not_index<poor_index:
    modify_string = str[:not_index] + ' good ' + str[poor_index + 4:] 
else:
    modify_string = str
result = modify_string
print("modified string")
print(result)













