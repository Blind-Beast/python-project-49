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
    random_number = randint(1, 100)
    question = f'Question: {random_number}'
    if is_even(random_number) is True:
        result = 'yes'
    else:
        result = 'no'
    return result, question
