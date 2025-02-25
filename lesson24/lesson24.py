# Lesson 24
temp = ""
while True:
    user = input("Input names, X to stop: ")
    if user.capitalize() == "X":
        break
    elif len(user) > len(temp):
        temp = user
print(f"The longest name inputted was {temp}")