from random import randint
from random import choice

GAME_QUESTION = 'What is the result of the expression?'


def calculate_result(first_operand, second_operand, operator):
    """Return result of expression"""
    match operator:
        case '+':
            result = first_operand + second_operand
        case '-':
            result = first_operand - second_operand
        case '*':
            result = first_operand * second_operand
    return result


def find_result():
    """Return correct answer and question for the game"""
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operator = choice(['+', '-', '*'])
    question = f'{first_number} {operator} {second_number}'
    result = calculate_result(first_number, second_number, operator)
    return result, question
