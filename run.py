"""
Welcome to Battleships!
The command-line version of Battleships
Developed by Dan Pearce using the Python language!
"""
# Langauge and Script imports
import os
import time
from colours import Colours as Txt

# Global Variables

# Main Functions


def title():
    """
    Display the game's main 'title' screen.
    Game name and development credit.
    """
    print(" ")
    print(Txt.MAIN + Txt.BRIGHT + "Let's Play")
    print(" ")
    print(Txt.USER + ":::::::::      ::: ::::::::::: ::::::::::: :::      " +
          "  :::::::::: ::::::::  :::    ::: ::::::::::: :::::::::   ::::::" +
          ":: ")
    print(Txt.USER + ":+:    :+:   :+: :+:   :+:         :+:     :+:      " +
          "  :+:       :+:    :+: :+:    :+:     :+:     :+:    :+: :+:    " +
          ":+:")
    print(Txt.USER + "+:+    +:+  +:+   +:+  +:+         +:+     +:+      " +
          "  +:+       +:+        +:+    +:+     +:+     +:+    +:+ +:+   " +
          "    ")
    print(Txt.NEUT + "+#++:++#+  +#++:++#++: +#+         +#+     +#+      " +
          "  +#++:++#  +#++:++#++ +#++:++#++     +#+     +#++:++#+  +#++:+" +
          "+#++")
    print(Txt.COMP + "+#+    +#+ +#+     +#+ +#+         +#+     +#+      " +
          "  +#+              +#+ +#+    +#+     +#+     +#+              " +
          " +#+")
    print(Txt.COMP + "#+#    #+# #+#     #+# #+#         #+#     #+#      " +
          "  #+#       #+#    #+# #+#    #+#     #+#     #+#        #+#   " +
          " #+#")
    print(Txt.COMP + "#########  ###     ### ###         ###     ##########" +
          " ########## ########  ###    ### ########### ###         ######## ")
    print(" ")
    print("                                                               " +
          "                                        " + f"{Txt.USER}You" +
          f" {Txt.NEUT}VS " + f"{Txt.COMP}Computer")
    print(" ")
    print(Txt.MAIN + Txt.BRIGHT + "Developed by: Dan Pearce -  https://" +
          "danpearce.software/")
    print(" ")
    new_line()


def clear():
    """
    Clears the console to be more visually appealing to the user
    """
    os.system("cls" if os.name == "nt" else "clear")


def new_line():
    """
    Prints a line, visually matching the game's title colours
    Creates more readability in the console
    """
    print((f"{Txt.USER}_ " + f"{Txt.COMP}_ ") * 26 + "\n")


def game_menu():
    """
    Displays the 'menu' to the user
    Allowing the user to either
    view the rules
    or to play the game
    """
    time.sleep(1)
    print("TEST")


def rules():
    """
    Displays to the user the rules of the game
    and how to play the game.
    """


def start_game():
    """
    When called, this function will start the game
    and initiate the relevent functions as the
    game progresses.
    """


title()
clear()
new_line()
game_menu()
