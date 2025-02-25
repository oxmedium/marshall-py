# Lesson 23
loop = True

total = 0
counter = 0

while loop:
    user = input("Enter Exit to stop, Enter the mark: ")
    if user.lower().capitalize() == "Exit":
        loop = False
        break
    else:
        mark = int(user)
        if 0 <= mark <= 100:
            total += mark
            counter += 1
        else:
            print("Invalid Mark")
if counter == 0:
    print("There are no marks inputted")
else:
    average = total / counter
    print(f"The average of the marks is {average}")
