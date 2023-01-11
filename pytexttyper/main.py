from art import tprint
from time import sleep
import sys
import os

class colors:
    """
    'colors' from PyTextTyper, selection of colors to use with color().
    """
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
    RESET = '\033[0m'

class styles:
    """
    'styles' from PyTextTyper, selection of styles to use with style().
    """
    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISIBLE = '\033[08m'

def wait(seconds):
    """
    'wait' from PyTextTyper, rests program for a specified amount of time. Required parameter 'seconds'.
    """
    sleep(seconds)

def clear(seconds_till_clear = 0):
    """
    'clear' from PyTextTyper, clears program console. Optional parameter 'seconds_till_clear', default = 0.
    """
    sleep(seconds_till_clear)
    os.system("clear")

def color(colors):
    """
    'color' from PyTextTyper, sets program's console text colour. Required parameter 'colour'. BLACK, RED, GREEN, ORANGE, BLUE, PURPLE, CYAN, LIGHTGREY, DARKGREY, LIGHTRED, LIGHTGREEN, YELLOW, LIGHTBLUE, PINK, LIGHTCYAN, RESET.
    """
    print(colors, end = '')

def style(styles):
    """
    'style' from PyTextTyper, sets program's console text style. Example: twstyle(style.BOLD) Required parameter 'style'. RESET, BOLD, DISABLE, UNDERLINE, REVERSE, STRIKETHROUGH, INVISIBLE.
    """
    print(styles, end = '')

def art(text_to_ascii):
    """
    'art' from PyTextTyper, Prints text as ASCII art. Required parameter 'text_to_ascii'.
    """
    print('\n')
    tprint(text_to_ascii)
    sys.stdout.flush()

def text(text, type_speed = 0.05):
    """
    'text' from PyTextTyper, prints text with typewriter animation with optional ajustable speed. Required parameter 'text'. Optional parameter 'type_speed', default = 0.05.
    """
    for char in text:
        print(char, end = '')
        sys.stdout.flush()
        sleep(type_speed)

def input(text, type_speed = 0.05):
    """
    'input' from PyTextTyper, prints text with typewriter animation with optional ajustable speed then waits for user input which it returns. Required parameter 'text'. Optional parameter 'type_speed', default = 0.05.
    """
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        sleep(type_speed)
    value = input()
    return value

def hold():
    """
    'hold' from PyTextTyper, waits for user input before it continues.
    """
    input()
    return