#!/usr/bin/env python3

import prompt
import brain_games.cli
from random import randint


def main():
    user_name = brain_games.cli.welcome_user()
    print("Answer \"yes\" if the number is even, otherwise answer \"no\".")
    good_tries = 0
    while good_tries < 3:
        random_number = randint(1, 100)
        if random_number % 2 == 0:
            is_number_even = 'yes'
        else:
            is_number_even = 'no'
        print(f'Question: {random_number}')
        answer = prompt.string('Your answer: ')
        if answer == is_number_even:
            good_tries += 1
            print('Correct!')
        else:
            good_tries = 0
            print("Let\'s try again!")
    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
