from random import randint

intro = 'What is the result of the expression?'


def question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    operator = randint(1, 3)
    match operator:
        case 1:
            result = str(first_number + second_number)
            print(f'Question: {first_number} + {second_number}')
        case 2:
            result = str(first_number - second_number)
            print(f'Question: {first_number} - {second_number}')
        case 3:
            result = str(first_number * second_number)
            print(f'Question: {first_number} * {second_number}')
    return result
