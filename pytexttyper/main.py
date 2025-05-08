from art import tprint
from time import sleep
import sys
import os

# ANSI escape codes for colors
BLACK = '\033[30m'
RED = '\033[31m'
GREEN = '\033[32m'
ORANGE = '\033[33m'
BLUE = '\033[34m'
PURPLE = '\033[35m'
CYAN = '\033[36m'
LIGHTGREY = '\033[37m'
DARKGREY = '\033[90m'
LIGHTRED = '\033[91m'
LIGHTGREEN = '\033[92m'
YELLOW = '\033[93m'
LIGHTBLUE = '\033[94m'
PINK = '\033[95m'
LIGHTCYAN = '\033[96m'

# ANSI escape codes for styles
RESET = '\033[0m'
BOLD = '\033[01m'
DISABLE = '\033[02m'
UNDERLINE = '\033[04m'
REVERSE = '\033[07m'
STRIKETHROUGH = '\033[09m'
INVISIBLE = '\033[08m'

def clear(seconds_till_clear=0):
    """
    'clear()' from the PyTextTyper package, clears the program console.

    Args:
        seconds_till_clear (int, optional): Number of seconds to wait before clearing the console. Default is 0.

    Example:
        clear(2)
    """
    sleep(seconds_till_clear)
    os.system("clear")

def color(color_code):
    """
    'color()' from the PyTextTyper package, sets the program's console text color.

    Args:
        color_code (str): Available options:
            - BLACK
            - RED
            - GREEN
            - ORANGE
            - BLUE
            - PURPLE
            - CYAN
            - LIGHTGREY
            - DARKGREY
            - LIGHTRED
            - LIGHTGREEN
            - YELLOW
            - LIGHTBLUE
            - PINK
            - LIGHTCYAN
            - RESET

    Example:
        color(GREEN)
    """
    print(color_code, end='')

def style(style_code):
    """
    'style()' from the PyTextTyper package, sets the program's console text style.

    Args:
        style_code (str): Available options:
            - BOLD
            - DISABLE
            - UNDERLINE
            - REVERSE
            - STRIKETHROUGH
            - INVISIBLE

    Example:
        style(BOLD)
    """
    print(style_code, end='')

def art(text_to_ascii):
    """
    'art()' from the PyTextTyper package, prints text as ASCII art.

    Args:
        text_to_ascii (str): The text to convert into ASCII art.

    Example:
        art("Hello")
    """
    tprint(text_to_ascii)
    sys.stdout.flush()

def text(text, type_speed=0.05):
    """
    'text()' from the PyTextTyper package, prints text with a typewriter animation.

    Args:
        text (str): The text to display.
        type_speed (float, optional): Speed of the typewriter animation in seconds. Default is 0.05.

    Example:
        text("Hello, world!", type_speed=0.1)
    """
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        sleep(type_speed)

def question(text, type_speed=0.05):
    """
    'question()' from the PyTextTyper package, prints text with a typewriter animation and waits for user input.

    Args:
        text (str): The text to display.
        type_speed (float, optional): Speed of the typewriter animation in seconds. Default is 0.05.

    Returns:
        str: The user's input.

    Example:
        answer = question("What is your name? ", type_speed=0.1)
    """
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        sleep(type_speed)
    value = input()
    return value

def hold():
    """
    'hold()' from the PyTextTyper package, waits for user input before continuing.

    Example:
        hold()
    """
    input()
    return