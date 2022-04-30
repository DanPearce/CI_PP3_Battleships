"""
Login Authentiction for Battleships game -
Uses Google Sheets API.
"""
# Language and Script Imports
import time
import gspread
import maskpass
from google.oauth2 import service_account
from run import clear, new_line, game_menu, title
from colours import Colours as Txt

# Global Variables
SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
CREDS = service_account.Credentials.from_service_account_file('creds.json',
                                                              scopes=SCOPE)
CLIENT = gspread.authorize(CREDS)
USERNAME_DATA = CLIENT.open('battleships_usernames').sheet1
USERNAME = None
USERNAME_ROW = None
PLAYER_USERNAME = None
PLAYER_PASSWORD = None
PLAYER_SCORE = None

# Login Functions


def welcome():
    """
    Welcomes the user to the game.
    Prompts user to log into their account.
    """
    title()
    print(Txt.MAIN + "Welcome to Batttleships!\n")
    new_line()
    time.sleep(1)
    print(Txt.MAIN + "Please choose and option:")
    game_options = Txt.MAIN + "1) Login\n 2) Create a new user\n\n"
    user_option = input(game_options)
    while user_option not in ("1", "2"):
        print(Txt.ERROR + "Please choose a correct option, either '1' or '2'")
        user_option = input(game_options)
    if user_option == "1":
        clear()
        title()
        check_user()
    elif user_option == "2":
        clear()
        title()
        create_user()


def check_user():
    """
    Checks the user's input agaisnt the data stored in the
    Google Sheet
    """
    check_username = input(Txt.MAIN + "Please enter your username:\n")
    if check_username in USERNAME_DATA.col_values(1):
        global USERNAME
        USERNAME = check_username
        existing_user()
        return USERNAME
    elif check_username not in USERNAME_DATA.col_values(1):
        print(Txt.ERROR + "Incorrect username!")
        time.sleep(1)
        print(Txt.MAIN + "Please choose an option:")
        game_options = Txt.MAIN + "1) Try again\n2) Create a new user\n\n"
        user_option = input(game_options)
        while user_option not in ("1", "2"):
            print(Txt.ERROR + "Please choose a correct option, either '1' or" +
                  " '2'")
            user_option = input(game_options)
        if user_option == "1":
            clear()
            title()
            check_user()
        elif user_option == "2":
            clear()
            title()
            create_user()


def existing_user():
    """
    Existing user is prompted to enter their password which is checked
    agaisnt the Google Sheet.
    """
    global USERNAME_ROW
    global PLAYER_USERNAME
    global PLAYER_PASSWORD
    global PLAYER_SCORE
    clear()
    title()
    print(f"{Txt.USER}Welcome back, {USERNAME}!")
    time.sleep(1.5)
    USERNAME_ROW = USERNAME_DATA.find(USERNAME).row
    PLAYER_USERNAME = USERNAME_DATA.row_values(USERNAME_ROW)[0]
    PLAYER_PASSWORD = USERNAME_DATA.row_values(USERNAME_ROW)[1]
    PLAYER_SCORE = USERNAME_DATA.row_values(USERNAME_ROW)[2]
    username_pass = maskpass.askpass(prompt="Password:", mask="*")

    if username_pass == PLAYER_PASSWORD:
        new_line()
        print(f"{Txt.USER}Thanks for logging in, {PLAYER_USERNAME}!")
        new_line()
        time.sleep(1)
        print(f"{Txt.MAIN}You have won {PLAYER_SCORE} time(s) against the" +
              " computer!")
        game_menu()
    else:
        print(Txt.ERROR + "Incorrect password!")
        print(Txt.ERROR + "Please try again!")
        time.sleep(1.5)
        existing_user()


def create_user():
    """
    Creates a new user to be added to the Google Sheet
    """


def add_new_user(name, password, score):
    """
    Add's the data from create_user to the Google Sheet
    passing:
    - name the user's desired username
    - password the user's desired password
    - score setting the new user's score to zero
    """
