import random


def generate_number(difficulty):
    return random.randint(1, difficulty)


def get_guess_from_user(difficulty):
    while True:
        try:
            guess = int(input(f"Guess a number between 1 and {difficulty}: "))
            if 1 <= guess <= difficulty:
                return guess
            else:
                print(f"Please enter a number between 1 and {difficulty}.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def compare_results(number, guess):
    if guess == number:
        return 0  # Correct guess
    elif guess < number:
        return -1  # Guess is too low
    else:
        return 1  # Guess is too high


def play(difficulty):
    number = generate_number(difficulty)
    attempts = 0

    while True:
        guess = get_guess_from_user(difficulty)
        result = compare_results(number, guess)
        attempts += 1

        if result == 0:
            print(f"Congratulations! You guessed the secret number {number} correctly.")
            print(f"It took you {attempts} attempts.")
            return True
        elif result == -1:
            print("Too low. Guess a higher number.")
        else:
            print("Too high. Guess a lower number.")