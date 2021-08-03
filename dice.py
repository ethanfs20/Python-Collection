import random # Import our python modules here.
import time

counter = 0 # Initialize our counter variable to 0

RPS = ["Rock", "Paper", "Scissors"] # Our array set to var RPS

rand = random.choice(RPS) # Initialize var rand to a random string from our array RPS

human = input("Rock, Paper, or Scissors? ") # set var human to users input.

while counter < 4: # main section that performs the counter and prints the selections.
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

if rand == "Rock": # This entire section checks for all posibilites and prints the loosing and winnings.
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
