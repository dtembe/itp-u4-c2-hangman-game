from .exceptions import *
import random

# Complete with your own, just for fun :)
list_of_words = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]


def _get_random_word(list_of_words):
    if len(word) < 1:
        raise InvalidListOfWordsException
    else:
        return random.choice(list_of_words).lower()

def _mask_word(word):
    numchar = len(list_of_words)
    if numchar > 0:
        mask_word = '*' * numchar
        return mask_word
    else:
        raise InvalidWordException


def _uncover_word(answer_word, masked_word, character):
    pass


def guess_letter(game, letter):
    pass


def start_new_game(list_of_words=None, number_of_guesses=5):
    if list_of_words is None:
        list_of_words = LIST_OF_WORDS

    word_to_guess = _get_random_word(list_of_words)
    masked_word = _mask_word(word_to_guess)
    game = {
        'answer_word': word_to_guess,
        'masked_word': masked_word,
        'previous_guesses': [],
        'remaining_misses': number_of_guesses,
    }

    return game
