"""
The Colours.py script is used to enhance
the user experience of the game by
adding colours using Colorama.
The colours are intended to make the game
more visually appealing and to create
a unique experience for the user.
"""
# Language and Script imports
import colorama
from colorama import Fore, Style


# Sets the colours to auto-reset at the end of each stage
colorama.init(autoreset=True)


class Colours:
    """
    Gives the colours in colorama a set class
    allowing to easily chaneg the colour
    of text in the game.
    """
    USER = Fore.BLUE + Style.BRIGHT
    COMP = Fore.RED + Style.BRIGHT
    NEUT = Fore.WHITE + Style.BRIGHT
    MAIN = Fore.CYAN + Style.NORMAL
    ERROR = Fore.RED
    BRIGHT = Style.BRIGHT
