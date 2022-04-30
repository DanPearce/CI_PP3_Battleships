"""
Welcome to Battleships!
The command-line version of Battleships
Developed by Dan Pearce using the Python language!
"""
# Language and Script imports
import os
import time
import random
import login
from colours import Colours as Txt

# Global Variables
LETTER_NUMBER = {
    "A": 0,
    "B": 1,
    "C": 2,
    "D": 3,
    "E": 4,
    "F": 5,
    "G": 6,
    "H": 7
}
SHIPS = [1, 2, 3, 4, 5]
USER_PLACE_BOARD = [[" "] * 8 for x in range(8)]
USER_GUESS_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_PLACE_BOARD = [[" "] * 8 for x in range(8)]
COMPUTER_GUESS_BOARD = [[" "] * 8 for x in range(8)]

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


def mid_game_title():
    """
    Displays the games title at the top of the game throughout the
    course of the game.
    """
    print(f"{Txt.USER}B " + f"{Txt.COMP}A " + f"{Txt.USER}T " +
          f"{Txt.COMP}T " + f"{Txt.USER}L " + f"{Txt.COMP}E " +
          f"{Txt.USER}S " + f"{Txt.COMP}H " + f"{Txt.USER}I " +
          f"{Txt.COMP}P " + f"{Txt.USER}S")
    print(" ")
    print(Txt.MAIN + Txt.BRIGHT + "Developed by: Dan Pearce -  https://" +
          "danpearce.software/")


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
    print((f"{Txt.USER}_ " + f"{Txt.COMP}_ ") * 28 + "\n")


def game_menu():
    """
    Displays the 'menu' to the user
    Allowing the user to either
    view the rules
    or to play the game
    """
    time.sleep(1)
    print(" ")
    print(Txt.MAIN + "Please choose an option:")
    print(" ")
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
    time.sleep(1)
    print(Txt.MAIN + Txt.BRIGHT + "Game Rules: ")
    time.sleep(1.5)
    new_line()
    print(Txt.MAIN + "The objective of the game: ")
    time.sleep(1.5)
    print(Txt.MAIN + "- Destroy all of the computer's ships!")
    time.sleep(1.5)
    print(Txt.MAIN + "- Before it destroys all of yours!")
    time.sleep(1.5)
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
    print(Txt.MAIN + "The computer will randomly do the same to your board.")
    time.sleep(1.5)
    new_line()
    time.sleep(1.5)
    print(Txt.MAIN + "Can you beat the machine?")
    time.sleep(1.5)
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
    and initiate the relevant functions as the
    game progresses.
    """
    clear()
    title()
    place_ships(COMPUTER_PLACE_BOARD)
    print(Txt.MAIN + Txt.BRIGHT + "Welcome to Battleships!")
    print(Txt.MAIN + "This is your board:")
    display_board(USER_PLACE_BOARD)
    print(Txt.MAIN + "Please place your ships:")
    place_ships(USER_PLACE_BOARD)
    new_line()
    while True:
        while True:
            print(Txt.MAIN + "Your guessing board:\n")
            display_board(USER_GUESS_BOARD)
            move(USER_GUESS_BOARD)
            break
        if ships_hit(USER_GUESS_BOARD) == 15:
            increment_score()
            new_line()
            time.sleep(1.5)
            new_line()
            time.sleep(1.5)
            print(Txt.USER + "Congratulations, you have won!")
            time.sleep(1)
            new_line()
            new_line()
            time.sleep(1.5)
            clear()
            title()
            new_line()
            game_options = Txt.MAIN + "1) Return to game menu\n2) Quit\n\n"
            user_option = input(game_options)
            while user_option not in ("1", "2"):
                print(Txt.MAIN + "Please choose an option")
                user_option = input(game_options)
            if user_option == "1":
                reset_boards()
                clear()
                title()
                time.sleep(1.5)
                game_menu()
            elif user_option == "2":
                new_line()
                print(Txt.MAIN + Txt.BRIGHT + "Thanks for playing!")
                time.sleep(1.5)
                new_line()
                time.sleep(1.5)
                clear()
                title()
                time.sleep(1.5)
                print(Txt.MAIN + Txt.BRIGHT + "Come back again soon!")
                new_line()
                time.sleep(1.5)
                quit()
        while True:
            move(COMPUTER_GUESS_BOARD)
            break
        clear()
        mid_game_title()
        new_line()
        print(Txt.MAIN + "Computer's guessing board:\n")
        display_board(COMPUTER_GUESS_BOARD)
        new_line()
        if ships_hit(COMPUTER_GUESS_BOARD) == 15:
            new_line()
            time.sleep(1.5)
            new_line()
            time.sleep(1.5)
            print(Txt.ERROR + "Sorry, you have lost to the machine!")
            time.sleep(1)
            new_line()
            new_line()
            time.sleep(1.5)
            clear()
            title()
            new_line()
            game_options = Txt.MAIN + "1) Return to game menu\n2) Quit\n\n"
            user_option = input(game_options)
            while user_option not in ("1", "2"):
                print(Txt.MAIN + "Please choose an option")
                user_option = input(game_options)
            if user_option == "1":
                reset_boards()
                clear()
                title()
                time.sleep(1.5)
                game_menu()
            elif user_option == "2":
                new_line()
                print(Txt.MAIN + Txt.BRIGHT + "Thanks for playing!")
                time.sleep(1.5)
                new_line()
                time.sleep(1.5)
                clear()
                title()
                time.sleep(1.5)
                print(Txt.MAIN + Txt.BRIGHT + "Better luck next time!")
                new_line()
                time.sleep(1.5)
                quit()


# Main Game Functions


def display_board(board):
    """
    Creates and displays a visual board for the user
    to see as they progress throughout the game
    Passing: board so that the correct board can be
    displayed.
    """
    if board == USER_PLACE_BOARD or board == USER_GUESS_BOARD:
        print(Txt.USER + "  A B C D E F G H")
        print(Txt.USER + "  _ _ _ _ _ _ _ _")
        row_num = 1
        for row in board:
            print(Txt.USER + "%d|%s" % (row_num, f"{Txt.USER}|".join(row)))
            row_num += 1
    else:
        print(Txt.COMP + "  A B C D E F G H")
        print(Txt.COMP + "  _ _ _ _ _ _ _ _")
        row_num = 1
        for row in board:
            print(Txt.COMP + "%d|%s" % (row_num, f"{Txt.COMP}|".join(row)))
            row_num += 1


def place_ships(board):
    """
    When called this function will place the ships
    in either the computers boards or the will prompt
    the user for input to place onto their boards
    Passing: board so that the correct board can be
    altered depending on the stage of the game and if
    it's the computers turn or the users.
    """
    for ship in SHIPS:
        while True:
            if board == COMPUTER_PLACE_BOARD:
                orient = random.choice(["H", "V"])
                row, col = random.randint(0, 7), random.randint(0, 7)
                if ship_on_board_check(board, ship, orient, row, col):
                    if not ship_over_ship_check(board, ship, orient, row, col):
                        if orient == "H":
                            for i in range(col, col + ship):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = "X"
                        break
            else:
                place_ship = True
                print(Txt.MAIN + "Place the ship, it's size is" +
                      f" {Txt.MAIN + Txt.BRIGHT + str(ship)} spaces wide:")
                orient, row, col = user_input(place_ship)
                if ship_on_board_check(board, ship, orient, row, col):
                    if not ship_over_ship_check(board, ship, orient, row, col):
                        if orient == "H":
                            for i in range(col, col + ship):
                                board[row][i] = "X"
                        else:
                            for i in range(row, row + ship):
                                board[i][col] = "X"
                        clear()
                        mid_game_title()
                        new_line()
                        print(Txt.USER + "Your board:")
                        display_board(USER_PLACE_BOARD)
                        break


def ship_on_board_check(board, ship, orient, row, col):
    """
    Checks that the current ship being placed is on the
    board and doesn't 'fall off'. Meaning issues would
    arise with scores.
    Passing:
    - board: to check who's board is in use, display errors
    - ship: so that the ships size can be measured.
    - orient: to check the orientation for both types of r/c.
    - row/col: to check the position against the ship size.
    """
    if board == COMPUTER_PLACE_BOARD:
        if orient == "H":
            if col + ship > 8:
                return False
            else:
                return True
        else:
            if row + ship > 8:
                return False
            else:
                return True
    else:
        if orient == "H":
            if col + ship > 8:
                clear()
                mid_game_title()
                new_line()
                display_board(USER_PLACE_BOARD)
                print(Txt.ERROR + "Oops! The ship cannot go off the board!\n" +
                      "Please try again!")
                return False
            else:
                return True
        else:
            if row + ship > 8:
                clear()
                mid_game_title()
                new_line()
                display_board(USER_PLACE_BOARD)
                print(Txt.ERROR + "Oops! The ship cannot go off the board!\n" +
                      "Please try again!")
                return False
            else:
                return True


def ship_over_ship_check(board, ship, orient, row, col):
    """
    Checks that the current ship being placed is not being
    placed over another ship. Preventing issues with scores.
    Passing:
    - board: to check who's board is in use, display errors
    - ship: to allow us to measure the size of the ship
    against the row/column.
    - orient: to check the orientation for both types of r/c.
    - row/col: to determine if we're checking a row or column.
    """
    if board == COMPUTER_PLACE_BOARD:
        if orient == "H":
            for i in range(col, col + ship):
                if board[row][i] == "X":
                    return True
        else:
            for i in range(row, row + ship):
                if board[i][col] == "X":
                    return True
        return False
    else:
        if orient == "H":
            for i in range(col, col + ship):
                if board[row][i] == "X":
                    clear()
                    mid_game_title()
                    new_line()
                    display_board(USER_PLACE_BOARD)
                    print(Txt.ERROR + "Try again! The ship cannot go over" +
                          " another ship!")
                    return True
        else:
            for i in range(row, row + ship):
                if board[i][col] == "X":
                    clear()
                    mid_game_title()
                    new_line()
                    display_board(USER_PLACE_BOARD)
                    print(Txt.ERROR + "Try again! The ship cannot go over" +
                          " another ship!")
                    return True
        return False


def user_input(place_ship):
    """
    When called prompts the user for input
    and cycles through so that errors can be avoided.
    Passing: place_ships in order to determine
    if the user is placing ships
    or if they're guessing.
    """
    if place_ship is True:
        while True:
            try:
                orient = input(Txt.MAIN + "Would you like your ship to be" +
                               " Vertical(V) or Horizontal(H)?\n").upper()
                while orient not in ("H", "V"):
                    clear()
                    mid_game_title()
                    new_line()
                    display_board(USER_PLACE_BOARD)
                    print(Txt.ERROR + "Incorrect input, please choose either" +
                          " 'V'(Vertical) or 'H'(Horizontal)\n")
                    break
                if orient == "H" or orient == "V":
                    break
            except ValueError:
                clear()
                mid_game_title()
                new_line()
                display_board(USER_PLACE_BOARD)
                print(Txt.ERROR + "Incorrect input, please choose either" +
                      " 'V'(Vertical) or 'H'(Horizontal)\n")
        while True:
            try:
                row = input(Txt.MAIN + "Please enter the row you'd like to" +
                            " place the ship (1-8):\n")
                while row not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                    clear()
                    mid_game_title()
                    new_line()
                    display_board(USER_PLACE_BOARD)
                    print(Txt.ERROR + "Incorrect input, please enter a" +
                          " number between 1 & 8:\n")
                    break
                if row in ("1", "2", "3", "4", "5", "6", "7", "8"):
                    row = int(row) - 1
                    break
            except ValueError:
                clear()
                mid_game_title()
                new_line()
                display_board(USER_PLACE_BOARD)
                print(Txt.ERROR + "Incorrect input, please enter a" +
                      " number between 1 & 8:\n")
        while True:
            try:
                col = input(Txt.MAIN + "Please enter the column you'd" +
                            " like to place the ship (A-H):\n").upper()
                while col not in ("A", "B", "C", "D", "E", "F", "G", "H"):
                    clear()
                    mid_game_title()
                    new_line()
                    display_board(USER_PLACE_BOARD)
                    print(Txt.ERROR + "Incorrect input, please enter a " +
                          "letter between A & H:\n")
                    break
                if col in ("A", "B", "C", "D", "E", "F", "G", "H"):
                    col = LETTER_NUMBER[col]
                    break
            except ValueError:
                clear()
                mid_game_title()
                new_line()
                display_board(USER_PLACE_BOARD)
                print(Txt.ERROR + "Incorrect input, please enter a " +
                      "letter between A & H:\n")
        return orient, row, col
    else:
        while True:
            try:
                row = input(Txt.MAIN + "Please enter the row you'd like to" +
                            " guess the computer's ship (1-8):\n")
                while row not in ("1", "2", "3", "4", "5", "6", "7", "8"):
                    clear()
                    mid_game_title()
                    new_line()
                    print(Txt.MAIN + "Computer's guessing board:\n")
                    display_board(COMPUTER_GUESS_BOARD)
                    new_line()
                    print(Txt.MAIN + "Your guessing board:\n")
                    display_board(USER_GUESS_BOARD)
                    print(Txt.ERROR + "Incorrect input, please enter a" +
                          " number between 1 & 8:\n")
                    break
                if row in ("1", "2", "3", "4", "5", "6", "7", "8"):
                    row = int(row) - 1
                    break
            except ValueError:
                clear()
                mid_game_title()
                new_line()
                print(Txt.MAIN + "Computer's guessing board:\n")
                display_board(COMPUTER_GUESS_BOARD)
                new_line()
                print(Txt.MAIN + "Your guessing board:\n")
                display_board(USER_GUESS_BOARD)
                print(Txt.ERROR + "Incorrect input, please enter a" +
                      " number between 1 & 8:\n")
        while True:
            try:
                col = input(Txt.MAIN + "Please enter the column you'd" +
                            " like to guess the computer's ship (A-H)" +
                            ":\n").upper()
                while col not in ("A", "B", "C", "D", "E", "F", "G", "H"):
                    clear()
                    mid_game_title()
                    new_line()
                    print(Txt.MAIN + "Computer's guessing board:\n")
                    display_board(COMPUTER_GUESS_BOARD)
                    new_line()
                    print(Txt.MAIN + "Your guessing board:\n")
                    display_board(USER_GUESS_BOARD)
                    print(Txt.ERROR + "Incorrect input, please enter a " +
                          "letter between A & H:\n")
                    break
                if col in ("A", "B", "C", "D", "E", "F", "G", "H"):
                    col = LETTER_NUMBER[col]
                    break
            except ValueError:
                clear()
                mid_game_title()
                new_line()
                print(Txt.MAIN + "Computer's guessing board:\n")
                display_board(COMPUTER_GUESS_BOARD)
                new_line()
                print(Txt.MAIN + "Your guessing board:\n")
                display_board(USER_GUESS_BOARD)
                print(Txt.ERROR + "Incorrect input, please enter a " +
                      "letter between A & H:\n")
        return row, col


def ships_hit(board):
    """
    Will check the players and computers boards
    for the amount of "X"/"Hits" allowing us
    to determine a winner.
    Passing: board to check different boards
    """
    hit_user = 0
    hit_computer = 0
    if board == USER_GUESS_BOARD:
        for row in board:
            for col in row:
                if col == f"{Txt.COMP}X":
                    hit_user += 1
        return hit_user
    elif board == COMPUTER_GUESS_BOARD:
        for row in board:
            for col in row:
                if col == f"{Txt.USER}X":
                    hit_computer += 1
        return hit_computer


def move(board):
    """
    This function acts as the 'move'/'turn' for the game
    and will also place the 'bombs'/'misses' onto the board
    Passing: board to check which board we are using.
    """
    if board == USER_GUESS_BOARD:
        row, col = user_input(USER_GUESS_BOARD)
        if board[row][col] == f"{Txt.COMP}~":
            clear()
            mid_game_title()
            new_line()
            print(Txt.MAIN + "Computer's guessing board:\n")
            display_board(COMPUTER_GUESS_BOARD)
            new_line()
            print(Txt.MAIN + "Your guessing board:\n")
            display_board(USER_GUESS_BOARD)
            print(Txt.ERROR + "You've already guessed there, try again!\n")
            move(board)
        elif board[row][col] == f"{Txt.COMP}X":
            clear()
            mid_game_title()
            new_line()
            print(Txt.MAIN + "Computer's guessing board:\n")
            display_board(COMPUTER_GUESS_BOARD)
            new_line()
            print(Txt.MAIN + "Your guessing board:\n")
            display_board(USER_GUESS_BOARD)
            print(Txt.ERROR + "You've already guessed there, try again!\n")
            move(board)
        elif COMPUTER_PLACE_BOARD[row][col] == "X":
            board[row][col] = f"{Txt.COMP}X"
        else:
            board[row][col] = f"{Txt.COMP}~"
    else:
        row, col = random.randint(0, 7), random.randint(0, 7)
        if board[row][col] == f"{Txt.USER}~":
            move(board)
        elif board[row][col] == f"{Txt.USER}X":
            move(board)
        elif USER_PLACE_BOARD[row][col] == "X":
            board[row][col] = f"{Txt.USER}X"
        else:
            board[row][col] = f"{Txt.USER}~"


def reset_boards():
    """
    Reset the game boards if the user decides to play again.
    """
    global USER_GUESS_BOARD
    global USER_PLACE_BOARD
    global COMPUTER_GUESS_BOARD
    global COMPUTER_PLACE_BOARD
    USER_PLACE_BOARD = [[" "] * 8 for x in range(8)]
    USER_GUESS_BOARD = [[" "] * 8 for x in range(8)]
    COMPUTER_PLACE_BOARD = [[" "] * 8 for x in range(8)]
    COMPUTER_GUESS_BOARD = [[" "] * 8 for x in range(8)]


def increment_score():
    """
    Increments the users winning score on the Google Spreadsheet
    """
    login.PLAYER_SCORE += 1
    login.USERNAME_DATA.update_cell(login.USERNAME_ROW, 3, +
                                    int(login.PLAYER_SCORE))


def init_program():
    """
    Starts the python code.
    """
    login.welcome()


# Initiates the program upon loading - Also Script Guard
if __name__ == "__main__":
    init_program()
