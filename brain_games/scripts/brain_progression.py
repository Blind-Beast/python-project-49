#!/usr/bin/env python3

import prompt
import brain_games.cli
from random import randint


def progress(a, b, c):
    i = 0
    prog = []
    while i < c:
        prog.append(a)
        i += 1
        a = a + b
    return prog


def main():
    user_name = brain_games.cli.welcome_user()
    print("Find the greatest common divisor of given numbers.")
    good_tries = 0
    while good_tries < 3:
        first_number = randint(1, 10)
        step = randint(1, 10)
        prog_len = randint(5, 10)
        prog = progress(first_number, step, prog_len)
        rand_num = randint(0, prog_len - 1)
        result = str(prog[rand_num])
        prog[rand_num] = '..'
        prog_str = ' '.join(str(el) for el in prog)
        print(f'Question: {prog_str}')
        answer = prompt.string('Your answer: ')
        if answer == result:
            good_tries += 1
            print('Correct!')
        else:
            good_tries = 0
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f'Let\'s try again, {user_name}!')

    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
