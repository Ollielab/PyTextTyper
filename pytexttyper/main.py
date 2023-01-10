from art import tprint
from time import sleep
from styling import color, style
import sys
import os

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