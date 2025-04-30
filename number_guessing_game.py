import random

random_number = random.randint(1, 100)
while True:
    try:
        number_to_guess = int(input("Guess the number between 1 and 100: "))
        if number_to_guess < random_number:
            print("You guessed too low.")
        elif number_to_guess > random_number:
            print("You guessed too high.")
        else:
            print("You guessed the number.")
            break
    except ValueError:
        print("Please enter a valid number.")
