import random

def get_difficulty():
    levels = {
        1: ("Easy", 10),
        2: ("Medium", 5),
        3: ("Hard", 3)
    }

    print("Please select the difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)\n")

    while True:
        try:
            choice = int(input('Enter your choice > '))
            if choice in levels:
                return levels[choice]
            print("Invalid selection. Please choose 1, 2, or 3.\n")
        except ValueError:
            print("Invalid input. Please enter a valid number (1, 2, or 3).\n")

def get_user_guess():
    while True:
        try:
            return int(input('Enter your guess > '))
        except ValueError:
            print("Invalid input! Please enter a valid integer.")

def play_game():
    secret_number = random.randint(1, 100)

    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.\n")

    level_name, max_chances = get_difficulty()
    print(f"\nGreat! You have selected the {level_name} difficulty level ({max_chances} chances). Let's start the game!\n")

    won = False
    for attempt in range(1, max_chances + 1):
        guess = get_user_guess()

        if guess < secret_number:
            print('Incorrect! Your guess is too low.\n')
        elif guess > secret_number:
            print('Incorrect! Your guess is too high.\n')
        else:
            print(f'Good job! You got it in {attempt} guesses.')
            won = True
            break

    if not won:
        print(f'Nope. The secret number was {secret_number}.')

if __name__ == '__main__':
    play_game()