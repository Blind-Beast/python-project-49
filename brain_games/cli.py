import prompt


def welcome_user():
    """Return username"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f'Hello, {name}!')
    return name
