import random


def get_money_interval(difficulty, total_value):
    min_value = total_value - (5 - difficulty)
    max_value = total_value + (5 - difficulty)
    return (min_value, max_value)


def get_guess_from_user():
    while True:
        try:
            guess = float(input("Enter your guess for the amount in USD: "))
            if guess >= 0:
                return guess
            else:
                print("Please enter a non-negative value.")
        except ValueError:
            print("Invalid input. Please enter a valid number.")


def play(difficulty):
    total_value = random.randint(1, 100)
    interval = get_money_interval(difficulty, total_value)
    print(f"Guess the amount in USD. The interval is: {interval}")

    guess = get_guess_from_user()

    if interval[0] <= guess <= interval[1]:
        print("Congratulations! Your guess is within the interval.")
        return True
    else:
        print("Sorry, your guess is outside the interval.")
        return False