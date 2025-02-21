# Lesson 10
num = input("What is the number? ")

if num[0] in {'8', '9'}:
    if num[1] == num[2]:
        if num[-1] in {'8', '9'}:
            print("Telemarketer")
        else:
            print("Not Telemarketer")
    else:
        print("Not Telemarketer")
else:
    print("Not Telemarketer")