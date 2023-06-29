import random

user_wins = 0
computer_wins = 0


def get_user_choice():
    choice = input("Enter your choice (rock, paper, or scissors): ")
    choice = choice.lower()
    while choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please try again.")
        choice = input("Enter your choice (rock, paper, or scissors): ")
        choice = choice.lower()
    return choice


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def determine_winner(user_choice, computer_choice):
    global user_wins, computer_wins
    print("You chose:", user_choice)
    print("Computer chose:", computer_choice)
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        user_wins += 1
        return "You win!"
    else:
        computer_wins += 1
        return "Computer wins!"


def play_again():
    choice = input("Do you want to play again? (yes/no): ")
    choice = choice.lower()
    while choice not in ["yes", "no"]:
        print("Invalid choice. Please try again.")
        choice = input("Do you want to play again? (yes/no): ")
        choice = choice.lower()
    if choice == "no":
        print("Final Score - You:", user_wins, "Computer:", computer_wins)
    return choice == "yes"


def play_game():
    global user_wins, computer_wins
    print("Welcome to Rock-Paper-Scissors!")
    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()
        print()
        result = determine_winner(user_choice, computer_choice)
        print(result)
        print("Current Score - You:", user_wins, "Computer:", computer_wins)
        print()
        if not play_again():
            break


play_game()
