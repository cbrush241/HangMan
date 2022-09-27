import requests
from functions import clean_up_dirty_words
from functions import select_word
from functions import string_of_blanks
from functions import evaluate_guess
from hangman_pics import hangman_pics

# Get list of words from external website
word_site = "https://www.mit.edu/~ecprice/wordlist.10000"
response = requests.get(word_site)
dirty_words = response.content.splitlines()

# function call to clean the external word list
external_cleaned = clean_up_dirty_words(dirty_words)

# manage input/output
print('Welcome to Hangman!')
would_you_like_to_play = input('\nWould you like to play hangman? (y/n)')

# while loop to initiate game upon user request
while would_you_like_to_play == 'y':

    # function call to pick word
    selected_word = select_word(external_cleaned)

    # define hangman picture index variable
    wrong_guesses = 0

    # create empty list of guesses
    used_guesses = []

    # function call to create string with blanks to be filled
    incomplete_word = string_of_blanks(selected_word)

    # while loop to keep gameplay running
    game_on = True
    while game_on == True:
        print('\nHint: The word is ' + str(len(selected_word)) + ' letters long.')
        print('What you have: ' + incomplete_word)
        print(hangman_pics[wrong_guesses])
        print('Used Guesses: ' + str(used_guesses))
        current_guess = input('Guess a letter here: ')

        # conditional that user wins if they guess correct word
        if current_guess == selected_word:
            print('Congratulations! You guessed the correct word: ' + selected_word + '. You win!')
            game_on = False

        # conditional to increment picture index by one if guess was incorrect
        if current_guess not in selected_word:
            wrong_guesses += 1
            used_guesses.append(current_guess)

        # break loop when man is hanged
        if wrong_guesses == 6:
            print('\n')
            print(hangman_pics[6])
            print('You are out of guesses. The correct word was: ' + selected_word)
            print('You lose.')
            game_on = False

        # function call to evaluate each guess
        incomplete_word = evaluate_guess(current_guess, selected_word, incomplete_word)

        # end game if user guesses the correct word
        if incomplete_word == selected_word:
            print('Congratulations! You guessed the correct word: ' + selected_word + '. You win!')
            game_on = False

    # ask user if they would like to re-initiate gameplay
    would_you_like_to_play = input('\nWould you like to play hangman? (y/n)')
















