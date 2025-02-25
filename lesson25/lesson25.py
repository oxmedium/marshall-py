# Lesson 25
num = int(input("Enter a number to find its highest prime factor: "))
numcopy = num

largest = 0
while num % 2 == 0:
    num //= 2
    largest = max(largest, 2)
if num != 1:
    factor = 3
    while num != 1:
        if num % factor == 0:
            num //= factor
            largest = max(largest, factor)
        else:
            factor += 2
print(f"The highest prime factor of {numcopy} is {largest}")