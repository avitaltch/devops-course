import random
import time
import os


def generate_sequence(difficulty):
    return [random.randint(1, 101) for _ in range(difficulty)]


def get_list_from_user(difficulty):
    user_list = []
    for _ in range(difficulty):
        while True:
            try:
                number = int(input("Enter a number between 1 and 101: "))
                if 1 <= number <= 101:
                    user_list.append(number)
                    break
                else:
                    print("Please enter a number between 1 and 101.")
            except ValueError:
                print("Invalid input. Please enter a valid number.")
    return user_list


def clear_screen():
    # Clear the console screen
    os.system('cls' if os.name == 'nt' else 'clear')


def is_list_equal(list1, list2):
    return list1 == list2


def play(difficulty):
    sequence = generate_sequence(difficulty)
    print("Memorize the following sequence:")
    print(sequence)
    time.sleep(0.7)
    clear_screen()
    print("Sequence has been hidden. Now it's time to recall the numbers.")

    user_list = get_list_from_user(difficulty)

    if is_list_equal(sequence, user_list):
        print("Congratulations! You won the game.")
        return True
    else:
        print("Sorry, you lost the game.")
        return False
