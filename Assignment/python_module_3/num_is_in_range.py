#Write a Python function to check whether a number is in a given
# range Write a Python function to check whether a number is
# perfect or not.

#program

check_num = 15
start_range = 10
end_range = 20
perfect_num = 15
if check_num >= start_range and check_num <=end_range:
    print("its in range")
else:
    print("its out of range")

if check_num == perfect_num:
    print("perfect num")
else:
    print("not perfect")