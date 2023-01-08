from colorama import init, Fore
from art import tprint
from time import sleep
import sys
import os

init()
class colour:
    BLACK = Fore.BLACK
    RED = Fore.RED
    GREEN = Fore.GREEN
    YELLOW = Fore.YELLOW
    BLUE = Fore.BLUE
    MAGENTA = Fore.MAGENTA
    CYAN = Fore.CYAN
    WHITE = Fore.WHITE
    RESET = Fore.RESET

def twsleep(seconds):
    """
    'twsleep' rests program for a specified amount of time. Required parameter 'seconds'.
    """
    sleep(seconds)

def twclear(seconds_till_clear = 0):
    """
    'twclear' clears program console. Optional parameter 'seconds_till_clear'.
    """
    sleep(seconds_till_clear)
    os.system("clear")

def twcolour(colour):
    """
    'twcolour' sets program's console text colour. Required parameter 'colour'. BLACK, RED, GREEN, YELLOW, BLUE, MAGENTA, CYAN, WHITE, RESET.
    """
    print(colour, end = '')

def twart(text_to_ascii):
    """
    'twart' Prints text as ASCII art. Required parameter 'text_to_ascii'.
    """
    tprint(text_to_ascii)
    sys.stdout.flush()

def twtext(text, type_speed = 0.05):
    """
    'twtext' prints text with typewriter animation with optional ajustable speed. Required parameter 'text'. Optional parameter 'type_speed', default = 0.05.
    """
    for char in text:
        print(char, end = '')
        sys.stdout.flush()
        twsleep(type_speed)

def twinput(text, type_speed = 0.05):
    """
    'twinput' prints text with typewriter animation with optional ajustable speed then waits for user input which it returns. Required parameter 'text'. Optional parameter 'type_speed', default = 0.05.
    """
    for char in text:
        print(char, end='')
        sys.stdout.flush()
        sleep(type_speed)
    value = input()  
    return value