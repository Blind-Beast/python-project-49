from random import randint

intro = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    while a != b:
        if a > b:
            a = a - b
        else:
            b = b - a
    return b


def question():
    first_number = randint(1, 100)
    second_number = randint(1, 100)
    result = str(gcd(first_number, second_number))
    print(f'Question: {first_number} {second_number}')
    return result
