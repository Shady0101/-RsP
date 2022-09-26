import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)
    player = None

    while player not in choices:
        player = input("rock, paper, or scissors?: ")

    if player == computer:
        print("computer: ",computer)
        print("player: ",player)
        print("Tie!")

    elif player == "rock":
        if computer == "paper":
            print("computer: ", computer)
            print("player: ", player)
            print("You lose!")
        if computer == "scissors":
          print("computer : ",computer )
          print("player : ",player)
          print("You win!")
          
    elif player == "paper":
      if computer == "scissors":
        print("computer : ",computer)
        print("player : ",player)
        print("You lose!")
      if computer == "rock":
        print("computer: ",computer)
        print("player : ",player)
        print("You Win!")
         

    elif player == "scissors":
      if computer == "rock":
        print("computer : ",computer)
        print("computer : ",player)
        print("You lose!")
      if computer == "paper":
        print("compouter : ",computer)
        print("player : ",player)
        print("You Win!")

    play_again = input("play again ? (yes/no) : ").lower()
  
    if play_again != "yes":
      break

