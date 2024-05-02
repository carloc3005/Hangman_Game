import random
import hangman_art
import hangman_words

chosen_word = random.choice(hangman_words.word_list)    # the computer will make a random choice from the word_list

display = []    # Create an empty list

word_len = len(chosen_word)    # Counting the len of the chosen_word

lives = 6   # Declaring 6 lives for the game

end_of_game = False    # Declaring a variable to end game

print(hangman_art.logo)

for _ in range(word_len):    # Counting the range of word_len and displays it as "_"
    display += "_"

while not end_of_game:    # While it is not the end of game keep user guessing
    guess = input("Enter a letter to guess: ").lower()

    if guess in display:
        print(f"You already guess this letter {guess}")

    for position in range(word_len):    # Counting the position of the word_len
        letter = chosen_word[position]  # letter is now the chosen_word with index
        if letter == guess:    # checking if the letter matches with the guess
            display[position] = letter  # Reveal the letter guess at the correct index

    if guess not in chosen_word:
        print(f"You guessed {guess}, that not in the letter word")
        lives -= 1    # -1 for every wrong guess
        if lives == 0:    # if lives = 0 then end of game
            end_of_game = True
            print("You lose!")

    print(f"{' '.join(display)}")    # joining all the elements and turning it into a string

    if "_" not in display:
        end_of_game = True
        print("You won the game")    # If there is no more "_" you won the game

    print(hangman_art.stages[lives])    # Prints the stages

