#!/usr/bin/env python3

import prompt
import brain_games.cli
from random import randint


def main():
    user_name = brain_games.cli.welcome_user()
    print("What is the result of the expression?")
    good_tries = 0
    while good_tries < 3:
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
        answer = prompt.string('Your answer: ')
        if answer == result:
            good_tries += 1
            print('Correct!')
        else:
            print(f'{answer} is wrong answer ;(. Correct answer was {result}')
            print(f'Let\'s try again, {user_name}!')

    print(f'Congratulations, {user_name}!')


if __name__ == '__main__':
    main()
