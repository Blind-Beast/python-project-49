from random import randint

GAME_QUESTION = 'Find the greatest common divisor of given numbers.'


def calculate_gcd(first_number, second_number):
    """Return greatest common divisor"""
    while first_number != second_number:
        if first_number > second_number:
            first_number = first_number - second_number
        else:
            second_number = second_number - first_number
    return second_number


def find_result():
    """Return correct answer and question for the game"""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    result = calculate_gcd(first_number, second_number)
    question = f'Question: {first_number} {second_number}'
    return result, question
