from random import randint

intro = 'Answer \"yes\" if the number is even, otherwise answer \"no\".'


def question():
    random_number = randint(1, 100)
    if random_number % 2 == 0:
        result = 'yes'
    else:
        result = 'no'
    print(f'Question: {random_number}')
    return result
