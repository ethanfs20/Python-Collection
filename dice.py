import random
import time

counter = 0

RPS = ["Rock", "Paper", "Scissors"]

rand = random.choice(RPS)

human = input("Rock, Paper, or Scissors? ")

while counter < 4:
    counter = counter + 1
    if counter == 1:
        time.sleep(1)
        print("Rock!")
    elif counter == 2:
        time.sleep(1)
        print("Paper!")
    elif counter == 3:
        time.sleep(1)
        print("Scissors!")
else:
    time.sleep(1)
    print("SHOOT!")
    time.sleep(1.2)
    print(f"AI: I choose {rand}")
    time.sleep(0.3)
    print(f"You: I choose {human}")

if rand == "Rock":
    if human == "Scissors":
        print("You lost!")
    elif human == "Paper":
        print("You won!")
    elif human == "Rock":
        print("Its a draw!")
if rand == "Paper":
    if human == "Rock":
        print("You lost!")
    elif human == "Scissors":
        print("You won!")
    elif human == "Paper":
        print("Its a draw!")
if rand == "Scissors":
    if human == "Paper":
        print("You lost!")
    elif human == "Rock":
        print("You won!")
    elif human == "Scissors":
        print("Its a draw!")