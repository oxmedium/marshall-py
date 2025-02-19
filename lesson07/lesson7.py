# Lesson 7
import random 

dc = int(input("Enter the difficulty level: "))
num = random.randrange(1, 21)
print(f"The player has rolled a {num}!")
if dc > num:
    print("Fail..")
elif dc <= num:
    print("Success!")