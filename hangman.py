import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
lives = 6
print("****************************6 LIVES LEFT****************************")
chosen_word = random.choice(word_list)
print(chosen_word)

placeholder = ""
word_length = len(chosen_word)
for position in range(word_length):
    placeholder += "_"
print(placeholder)

game_over = False
correct_letters = []
guess_letters = []

while not game_over:
    guess = input("Guess a letter: ").lower()
    display = ""

    for letter in chosen_word:
        if letter == guess:
            display += letter
            correct_letters.append(guess)
        elif letter in correct_letters:
            display += letter
        else:
            display += "_"

    print(display)
    if guess in guess_letters:
        print(f"You have already guessed that letter: {guess}")
    else:
        if guess not in chosen_word:
            lives -= 1
            print(f"You guessed: {guess}, that's not in the word. You lose a life.")
            print(f"****************************{lives} LIVES LEFT****************************")
            print(stages[lives])


    if "_" not in display:
        game_over = True
        print("You win.")
    elif lives == 0:
        game_over = True
        print(f"IT WAS {chosen_word}! YOU LOSE")

    guess_letters.append(guess)
