import Formatter as Text


def welcome(name: str):
    return f"Hello {Text.underline(name)} and welcome to the World of Games (WoG).\n" \
           "Here you can find many cool games to play."


def load_game():
    game_options = get_game_options()
    difficulty_options = get_difficulty_options()

    print("Please choose a game to play:")
    print_options(game_options)
    game_selection = select_menu(game_options)
    print()

    print("Please choose game difficulty:")
    print_options(difficulty_options)
    game_difficulty = select_menu(difficulty_options)
    print()

    print(game_selection, game_difficulty)


def validate_selection(value, minimum_value: int, maximum_value: int):
    return value.isdigit() and minimum_value <= int(value) <= maximum_value


def select_menu(options: dict):
    selection = -1
    while selection == -1:
        selection = input("Your selection: ")
        if validate_selection(selection, 1, len(options)):
            return selection
        elif selection == 'q':
            print("Bye bye...")
            return exit(0)
        else:
            print("You've selected an invalid option.\nPlease select a number, or 'q' to exit.")
            selection = -1


def get_game_options():
    return {
        1: f"{Text.bold('Memory Game')} - a sequence of numbers will appear for 1 second and you have to guess it back",
        2: f"{Text.bold('Guess Game')} - guess a number and see if you chose like the computer",
        3: f"{Text.bold('Currency Roulette')} - try and guess the value of a random amount of USD in ILS"
    }


def get_difficulty_options():
    return {
        1: f"{Text.green('Very Easy')}",
        2: f"{Text.blue('Easy')}",
        3: f"{Text.cyan('Medium')}",
        4: f"{Text.yellow('Hard')}",
        5: f"{Text.red('Extreme')}",
        6: f"{Text.rainbow('Impossible')}"
    }


def print_options(options):
    for key in options.keys():
        print(f"[{Text.blue(key)}]", options[key])
