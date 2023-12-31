#• Write a Python program to find the second smallest
# number in a list.

# program
# sorting the list using bubble sort
def sorted_list(list):
    n = len(list)

    for i in range(n): # it iterates n times wherer n is length of list
        for j in range(0,n-i-1):
            #if nth item is greater than n+1 than swap the values
            if list[j] > list[j+1]:
                temp = list[j]
                list[j] = list[j+1]
                list[j+1] = temp
    return list
    

list = [10,50,2,60]
#sorted list
new_list = sorted_list(list)
#printing sorted list
print(new_list)

#printing the second smallest element in the list

print(new_list[1])