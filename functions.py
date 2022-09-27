import random
from PyDictionary import PyDictionary
import re

# function to select a random word from external word list
def select_word(words):
    dictionary = PyDictionary()
    i = 0
    while i < 1:
        word = random.choice(words)
        if dictionary.meaning(word, True):
            i += 1
            return word

# function to clean up dirty words from external word list
def clean_up_dirty_words(words):
    words_cleaned = []
    for word in words:
        word = str(word)
        words_cleaned.append(word[2:-1])
    return words_cleaned

# function to generate a string of blanks
def string_of_blanks(word):
    blanks = ''
    iterator = len(word)
    while iterator > 0:
        blanks += '_'
        iterator -= 1
    return blanks

# function to evaluate each guess and return appropriate output
def evaluate_guess(guess, word, incomplete_word):
    if guess in word:
        index_list = [i for i in range(len(word)) if word[i] == guess]
        for index in index_list:
            incomplete_word = incomplete_word[:index] + guess + incomplete_word[index+1:]
        return incomplete_word
    else:
        return incomplete_word







