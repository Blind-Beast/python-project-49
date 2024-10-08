from random import randint

GAME_QUESTION = "Answer \"yes\" if given number is prime."\
                " Otherwise answer \"no\"."


def is_prime(number):
    """Return True for prime number, otherwise return False"""
    if number == 1:
        return False
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            return False
        else:
            continue
    return True


def find_result():
    """Return correct answer and question for the game"""
    question = randint(1, 100)
    result = 'yes' if is_prime(question) else 'no'
    return result, question
