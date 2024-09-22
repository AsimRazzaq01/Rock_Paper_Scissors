import random

user_wins = 0
computer_wins = 0
options = ["rock","paper","scissors"]

while True:
    user_input = input("Choose Rock/Paper/Scissors  or Q to quit game: ").lower()
    if user_input == 'q':
        break
    
    if user_input not in options:
        continue

    random_number = random.randint(0, 2)
    # rock = 0 , paper = 1 , scissors = 2

    computer_turn = options[random_number]
    print("Computer has chosen: ", computer_turn +".")

    # rock scenarios
    if user_input == "rock" and computer_turn == "scissors":
        print("You Won!")
        user_wins +=1
    elif user_input == "rock" and computer_turn == "paper":
        print("Computer Won!")
        computer_wins +=1
    elif user_input == "rock" and computer_turn == "rock":
        print("its a Tie!")
        continue
    # paper scenarios
    elif user_input == "paper" and computer_turn == "rock":
        print("You Won!")
        user_wins +=1
    elif user_input == "paper" and computer_turn == "scissors":
        print("Computer Won!")
        computer_wins +=1
    elif user_input == "paper" and computer_turn == "paper":
        print("its a Tie!")
        continue
    # scissors scenarios
    elif user_input == "scissors" and computer_turn == "paper":
        print("You Won!")
        user_wins +=1
    elif user_input == "scissors" and computer_turn == "rock":
        print("Computer Won!")
        computer_wins +=1
    elif user_input == "scissors" and computer_turn == "scissors":
        print("its a Tie!")
        continue
    else:
        print("Game Over !")


print("ScoreBoard : ")
print("You Won :", user_wins, "times.")
print("The Computer Won :", computer_wins, "times.")
print("Goodbye !")