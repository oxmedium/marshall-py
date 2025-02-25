# Lesson 20
print("All Perfect number under 10000: ")
total = 0
for num in range(1,10000):
    sum = 0
    for i in range(1,num):
        if num % i == 0:
            sum += i
    if sum == num:
        print(num)
        total += sum
print(f"{total} is the total sum of all the perfect numbers under 10000")

