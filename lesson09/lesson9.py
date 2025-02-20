# Lesson 9
from random import choice

invalid = True
player = ""
valid = ['Rock', 'Paper', 'Scissor']

while invalid:
    player = input("Rock paper scissors: ")
    if player in valid:
        invalid = False
opponent = choice(valid)
print(f"CPU chose {opponent}!")
if player == opponent:
    print("Tie Game")

else:
    if player == "Rock":
        if opponent == "Paper":
            print("CPU wins.")
        elif opponent == "Scissor":
            print("Player wins.")
    elif player == "Scissor":
        if opponent == "Rock":
            print("CPU wins.")
        elif opponent == "Paper":
            print("Player wins.")
    else:
        if opponent == "Scissor":
            print("CPU wins")
        elif opponent == "Rock":
            print("Player wins")