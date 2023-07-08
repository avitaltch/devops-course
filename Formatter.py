class Color:
    PURPLE = '\033[95m'
    CYAN = '\033[96m'
    DARKCYAN = '\033[36m'
    BLUE = '\033[94m'
    GREEN = '\033[92m'
    YELLOW = '\033[93m'
    RED = '\033[91m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    END = '\033[0m'


def underline(text: str):
    return f"{Color.UNDERLINE}{text}{Color.END}"


def bold(text: str):
    return f"{Color.BOLD}{text}{Color.END}"


def blue(text: str):
    return f"{Color.BLUE}{text}{Color.END}"


def red(text: str):
    return f"{Color.RED}{text}{Color.END}"


def green(text: str):
    return f"{Color.GREEN}{text}{Color.END}"


def yellow(text: str):
    return f"{Color.YELLOW}{text}{Color.END}"


def purple(text: str):
    return f"{Color.PURPLE}{text}{Color.END}"


def cyan(text: str):
    return f"{Color.CYAN}{text}{Color.END}"


def rainbow(text: str):
    rainbow_colors = [Color.PURPLE, Color.CYAN, Color.DARKCYAN, Color.BLUE,
                      Color.GREEN, Color.YELLOW, Color.RED]
    colored_text = ''
    for i, char in enumerate(text):
        colored_text += rainbow_colors[i % len(rainbow_colors)] + char
    colored_text += Color.END  # Reset color at the end
    return colored_text
