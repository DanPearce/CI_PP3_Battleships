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
    print(Txt.MAIN + "Please choose an option:")
    game_options = Txt.MAIN + "1) Play the game\n2) View the rules\n\n"
    user_option = input(game_options)

    while user_option not in ("1", "2"):
        print(Txt.ERROR + "Please choose a correct option, either '1' or '2'")
        user_option = input(game_options)
    if user_option == "1":
        start_game()
    elif user_option == "2":
        clear()
        title()
        rules()


def rules():
    """
    Displays to the user the rules of the game
    and how to play the game.
    """
    print(Txt.MAIN + Txt.BRIGHT + "Game Rules: ")
    new_line()
    print(Txt.MAIN + "The objective of the game: ")
    time.sleep(1.5)
    print(Txt.MAIN + "- Destroy all of the computer's ships!")
    time.sleep(1.5)
    print(Txt.MAIN + "- Before it destroys all of yours!")
    new_line()
    time.sleep(1.5)
    print(Txt.MAIN + "You will play against the computer on an 8 x 8 board.")
    time.sleep(1.5)
    print(Txt.MAIN + "You will be instructed to place 5 ships onto the board.")
    time.sleep(1.5)
    print(Txt.MAIN + "The computer will also select five locations of ships.")
    time.sleep(1.5)
    print(Txt.MAIN + "You will then turn by turn aim and place bombs onto " +
          "the computer's board to see if you have hit one of its ships.")
    time.sleep(1.5)
    print(Txt.MAIN + "The computer wil randomly do the same to your board.")
    new_line()
    time.sleep(1.5)
    print(Txt.MAIN + "Can you beat the machine?")
    new_line()
    time.sleep(1.5)
    print(Txt.MAIN + "What would you like to do?")
    game_options = Txt.MAIN + "1) Play the game\n2) Return to the game menu\n"
    user_option = input(game_options)

    while user_option not in ("1", "2"):
        print(Txt.ERROR + "Please choose a correct option, either '1' or '2'")
        user_option = input(game_options)

    if user_option == "1":
        start_game()

    elif user_option == "2":
        clear()
        title()
        game_menu()


def start_game():
    """
    When called, this function will start the game
    and initiate the relevent functions as the
    game progresses.
    """
    clear()
    title()


def init_program():
    """
    Starts the python code.
    """
    title()
    game_menu()


# Initiates the program upon loading - Also Script Guard
if __name__ == "__main__":
    init_program()
