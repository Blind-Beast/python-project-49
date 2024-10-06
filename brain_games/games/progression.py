from random import randint

GAME_QUESTION = 'What number is missing in the progression?'


def create_progression(start, step, length):
    """Return the progression with the specified parameters"""
    i = 0
    progression = []
    while i < length:
        progression.append(start)
        i += 1
        start = start + step
    return progression


def find_result():
    """Return correct answer and question for the game"""
    first_number = randint(1, 10)
    step = randint(1, 10)
    prog_len = randint(5, 10)
    prog = create_progression(first_number, step, prog_len)
    rand_num = randint(0, prog_len - 1)
    result = prog[rand_num]
    prog[rand_num] = '..'
    prog_str = ' '.join(str(el) for el in prog)
    question = f'Question: {prog_str}'
    return result, question
