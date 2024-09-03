import random

still_playing = True
player_score = 0
computer_score = 0

def play_game():
    global still_playing, player_score, computer_score  # Declare the variables as global

    player_choice = input("Enter your choice (rock, paper, or scissors): ")

    while player_choice.lower() not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please choose either rock, paper, or scissors.")
        player_choice = input("Enter your choice (rock, paper, or scissors): ")

    if player_choice.lower() == "rock":
        print("You chose rock!")
    elif player_choice.lower() == "paper":
        print("You chose paper!")
    elif player_choice.lower() == "scissors":
        print("You chose scissors!")

    computer_choice = random.choice(["rock", "paper", "scissors"])

    if computer_choice == "rock":
        print("The computer chose rock!")
    elif computer_choice == "paper":
        print("The computer chose paper!")
    elif computer_choice == "scissors":
        print("The computer chose scissors!")

    if player_choice.lower() == computer_choice:
        print("It's a tie!")
    elif (player_choice.lower() == "rock" and computer_choice == "scissors") or (player_choice.lower() == "scissors" and computer_choice == "paper") or (player_choice.lower() == "paper" and computer_choice == "rock"):
        print("You win this round!")
        player_score += 1
    else:
        print("Computer wins this round!")
        computer_score += 1

    play_again = input("Do you want to play again? (yes/no): ")

    while play_again.lower() not in ["yes", "no"]:
        print("Invalid choice. Please choose either yes or no.")
        play_again = input("Do you want to play again? (yes/no): ")

    if play_again.lower() == "yes":
        print("Let's play again!")
        play_game()
    else:
        print("Final score:")
        print("Player: ", player_score)
        print("Computer: ", computer_score)
        still_playing = False

while still_playing:
    play_game()
