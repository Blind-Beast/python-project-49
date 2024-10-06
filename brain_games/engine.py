import prompt


def start_game(game):
    """Launch a specific game"""
    print("Welcome to the Brain Games!")
    user_name = prompt.string("May I have your name? ")
    print(f'Hello, {user_name}!')
    print(game.GAME_QUESTION)
    good_tries = 0
    while good_tries < 3:
        result, question = game.find_result()
        print(question)
        answer = prompt.string('Your answer: ')
        if answer == str(result):
            good_tries += 1
            print('Correct!')
        else:
            good_tries = 0
            break
    if good_tries == 3:
        print(f'Congratulations, {user_name}!')
    else:
        print(f'\'{answer}\' is wrong answer ;(. Correct answer '
              f'was \'{result}\'')
        print(f'Let\'s try again, {user_name}!')
