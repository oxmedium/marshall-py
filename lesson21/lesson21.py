# Lesson 21
num = int(input("Enter the highest number to go up to: "))
high_num = 0
most = 0
for i in range(1, num):
    counter = 0
    for j in range(1, i):
        if i % j == 0:
            counter += 1
    if counter > most:
        most = counter
        high_num = i
print(f"The number with the highest amount of factors between 1 and {num} is {high_num} with {most} factors.")