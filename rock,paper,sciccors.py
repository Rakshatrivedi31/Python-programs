import random
choices = ["rock", "paper", "scissors"]
computer = random.choice(choices)
user = input("Enter rock, paper, or scissors: ")
if user == computer:
    print("Tie!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("You win!")
else:
    print("Computer wins!")