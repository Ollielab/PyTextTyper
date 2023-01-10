from art import tprint
from time import sleep
import sys
import os

class color:
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

class style:
    RESET = '\033[0m'
    BOLD = '\033[01m'
    DISABLE = '\033[02m'
    UNDERLINE = '\033[04m'
    REVERSE = '\033[07m'
    STRIKETHROUGH = '\033[09m'
    INVISIBLE = '\033[08m'

def psleep(seconds):
    """
    'psleep' rests program for a specified amount of time. Required parameter 'seconds'.
    """
    sleep(seconds)

def pclear(seconds_till_clear = 0):
    """
    'pclear' clears program console. Optional parameter 'seconds_till_clear'.
    """
    sleep(seconds_till_clear)
    os.system("clear")

def pcolor(color):
    """
    'pcolor' sets program's console text colour. Required parameter 'colour'. BLACK, RED, GREEN, ORANGE, BLUE, PURPLE, CYAN, LIGHTGREY, DARKGREY, LIGHTRED, LIGHTGREEN, YELLOW, LIGHTBLUE, PINK, LIGHTCYAN, RESET.
    """
    print(color, end = '')

def pstyle(style):
    """
    'pstyle' sets program's console text style. Example: twstyle(style.BOLD) Required parameter 'style'. RESET, BOLD, DISABLE, UNDERLINE, REVERSE, STRIKETHROUGH, INVISIBLE.
    """
    print(style, end = '')

def part(text_to_ascii):
    """
    'part' Prints text as ASCII art. Required parameter 'text_to_ascii'.
    """
    print('\n')
    tprint(text_to_ascii)
    sys.stdout.flush()

def ptext(text, type_speed = 0.05):
    """
    'ptext' prints text with typewriter animation with optional ajustable speed. Required parameter 'text'. Optional parameter 'type_speed', default = 0.05.
    """
    for char in text:
        print(char, end = '')
        sys.stdout.flush()
        psleep(type_speed)

def pinput(text, type_speed = 0.05):
    """
    'pinput' prints text with typewriter animation with optional ajustable speed then waits for user input which it returns. Required parameter 'text'. Optional parameter 'type_speed', default = 0.05.
    """
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        sleep(type_speed)
    value = input()
    return value

def phold():
    """
    'phold' waits for user input before it continues.
    """
    input()
    return