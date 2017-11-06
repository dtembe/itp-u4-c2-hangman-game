from .exceptions import *
import random

# Complete with your own, just for fun :)
LIST_OF_WORDS = ["hangman", "chairs", "backpack", "bodywash", "clothing",
                 "computer", "python", "program", "glasses", "sweatshirt",
                 "sweatpants", "mattress", "friends", "clocks", "biology",
                 "algebra", "suitcase", "knives", "ninjas", "shampoo"]


def _get_random_word(list_of_words):
    if len(list_of_words) < 1:
        raise InvalidListOfWordsException()
    else:
        return random.choice(list_of_words).lower()

def _mask_word(word):
    num_char = len(word)
    if num_char > 0:
        mask_word = '*' * num_char
        return mask_word
    else:
        raise InvalidWordException()


def _uncover_word(answer_word, masked_word, character):
    if len(answer_word) < 1 or len(masked_word) < 1:
        raise InvalidWordException()

    if len(character) <= 0 or len(character) >= 2:
        raise InvalidGuessedLetterException()

    if len(answer_word) != len(masked_word):
        raise InvalidWordException()

    if answer_word == masked_word:
        raise GameFinishedException()

    if character.lower() in answer_word.lower():
        word_list = list(answer_word)
        counter = 0
        while word_list[counter] != character and counter < len(word_list):
            counter += 1
        masked_word_list = list(masked_word)
        masked_word_list[counter] = character
        masked_word = ''.join(masked_word_list)
        return masked_word
    else:
        return masked_word


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
