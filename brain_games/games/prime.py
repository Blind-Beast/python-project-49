from random import randint

intro = 'Answer \'yes\' if given number is prime. Otherwise answer \'no\''


def question():
    number = randint(3, 100)
    for i in range(2, number // 2 + 1):
        if number % i == 0:
            result = 'no'
            break
        else:
            result = 'yes'
    print(f'Question: {number}')
    return result
