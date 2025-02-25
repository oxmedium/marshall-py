# Lesson 18
num = int(input("Find the factors for: "))
for i in range(1, num+1):
    if num % i == 0:
        print(f"{i} is a factor")