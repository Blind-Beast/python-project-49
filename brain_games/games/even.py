from random import randint

GAME_QUESTION = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def is_even(number):
    """Return True for even number, otherwise return False"""
    if number % 2 == 0:
        return True
    else:
        return False


def find_result():
    """Return correct answer and question for the game"""
    question = randint(1, 100)
    result = 'yes' if is_even(question) else 'no'
    return result, question
