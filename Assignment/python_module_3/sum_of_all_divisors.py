#Write a Python program to returns sum of all divisors of a
# number

def sum_of_divisors(number):
    sum = 0

    for i in range(1, number + 1):
        if number % i == 0:
            sum += i

    return sum

num = 5

output = sum_of_divisors(num)

print(output)