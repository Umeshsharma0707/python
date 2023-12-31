#Write a Python function to get the largest number, smallest
#num and sumof all from a list.

n = int(input("enter length of list :"))

list = []

for i in range(1,n+1):
    item = int(input(f"enter integer item {i} : "))
    list.append(item)

print(list)

#finding largest item in the list

def find_largest(list):
    for i in list:
        largest = i # consider largest is i 
        for j in list: # compare every element of i with j
            if largest < j: # if j is greatere means j is larger than i
                largest = j # than largest is j
        

    print("largest element : ",largest)

find_largest(list)

# find smallest
def find_smallest(list):
    for i in list:
        smallest = i
        for j in list:# compare every element of i with j
            if smallest > j: # if i is greater than j means j is smaller
                smallest = j # j is smaller

    print("smallest element is : ",smallest)

find_smallest(list)

# sum of the list elements

def sum_elements(list):
    sum = 0

    for i in list:
        sum = sum + i

    print("sum of elements of list : ",sum)

sum_elements(list)