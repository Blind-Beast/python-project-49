import prompt


def start_game(game):
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    print(game.intro)
    good_tries = 0
    while good_tries < 3:
        result = game.question()
        answer = prompt.string('Your answer: ')
        if answer == result:
            good_tries += 1
            print('Correct!')
        else:
            good_tries = 0
            print(f'\'{answer}\' is wrong answer ;(. Correct answer '
                  f'was \'{result}\'')
            print(f'Let\'s try again, {name}!')

    print(f'Congratulations, {name}!')
