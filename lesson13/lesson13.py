# Lesson 13
invalid = True
while invalid:
    month = int(input("What is the month, then date: "))
    day = int(input())
    if month == 2 and day > 29:
        print("Invalid Day")
    elif month > 12 or month < 0 or day > 31 or day < 0:
        print("Invalid month or day")
    else:
        invalid = False

if month < 2:
    print("Before")
elif month > 2:
    print("After")
else:
    if day > 18:
        print("After")
    elif day < 18:
        print("Before")
    else:
        print("Special")