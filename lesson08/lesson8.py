# Lesson 8
winloss = input("Input your wins and losses: ")
wins = 0
for i in range(6):
    game = input(f"What was the results of game {i + 1} ")
    if game == "W":
        wins += 1

if wins > 4:
    print("You are in group 1")
elif wins > 2:
    print("You are in group 2")
elif wins > 0:
    print("You are in group 3")
else:
    print("You are a loser dawg")
