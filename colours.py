"""
The Colours.py script is used to enhance
the user experience of the game by
adding colours using Colorama.
The colours are intended to make the game
more visually appealing and to create
an unique experience for the user.
"""
# Language and Script imports
import colorama
from colorama import init, Fore, Back, Style

"""
Sets the colours to auto-reset at each stage
"""
colorama.init(autoreset=True)

class Colours:
    """
    Gives the colours in colorama a set class
    allowing to easily chaneg the colour
    of text in the game.
    """
    