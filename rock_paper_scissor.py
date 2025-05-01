import random

#example for modularising code, by defining smaller functions
#concept called DRY - don't repeat yourself
#choices = ("r", "p", "s")

ROCK = 'r'
PAPER = 'p'
SCISSOR = 's'
emojis = {ROCK: '🪨', PAPER: '📃', SCISSOR: '✂️'}
choices = tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice = input("Rock, paper or scissor? (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice!")

def display_choices(user_choice, computer_choice):
    print(f"You chose {emojis[user_choice]}")
    print(f"Computer chose {emojis[computer_choice]}")

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("Tie!")
    elif (
            (user_choice == ROCK and computer_choice == SCISSOR) or
            (user_choice == PAPER and computer_choice == ROCK) or
            (user_choice == SCISSOR and computer_choice == PAPER)):
        print("You win!")
    else:
        print("You lost!")

def play_game():
    while True:
        computer_choice = random.choice(choices)
        user_choice = get_user_choice()
        display_choices(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)

        continue_game = input("Continue? (y/n): ").lower()
        if continue_game == "n":
            break
        elif continue_game == "y":
            continue
        else:
            print("Invalid input")
            break

#invoking the function
play_game()


