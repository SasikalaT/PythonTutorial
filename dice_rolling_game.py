import random

while True:
    roll_the_dice = input("Roll the dice? (y/n): ").upper()
    if roll_the_dice == "Y":
        # get input of number of dice
        number_of_dice = int(input("Enter number of dice you want to roll: "))
        if number_of_dice <= 0:
            print("Please enter a number greater than 0")
        else:
            game_outcome = []
            for dice_roll in range(number_of_dice):
                #print(dice_roll)
                dice1 = random.randint(1, 6)
                game_outcome.insert(dice_roll, dice1)
                #dice2 = random.randint(1, 6)
            formated_list = ", ".join(map(str, game_outcome))
            print(f"({formated_list})")
    elif roll_the_dice == "N":
        print("Thanks for playing the game")
        break
    else:
        print("Invalid choice, try again.")

