# Lesson 17
num = int(input("What factorial would you like: "))
factorial = 1
while num > 0:
    factorial *= num
    num -= 1
print(factorial)
