"""Write a Python program to generate and print a list of first
and last 5 elements where the values are square of
numbers between 1 and 30."""

# we can generate square list of 1 to 30 
#by using the list comprenhesion

start_value = 1 # range start value
end_value = 30 # range end value

# x is an iterable variable 
square_list = [x**2 for x in range(start_value,end_value+1)]

# printing the square list
print(square_list)