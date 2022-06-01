import random
import time

random.seed(time.time())

positions = ["Rock", "Paper", "Scissors"]

playerChoice = int(input("What do you choose? [0] for Rock, [1] for Paper, or [2] for Scissors. "))
computerChoice = int(random.randint(0, len(positions) - 1))

print(f"You chose {positions[playerChoice]}")
print(f"The computer chose {positions[computerChoice]}")

if playerChoice == computerChoice:
    print("It's a tie!")
elif playerChoice == computerChoice + 1 or playerChoice == computerChoice - 2:
    print("You win!")
else:
    print("You lose!")
