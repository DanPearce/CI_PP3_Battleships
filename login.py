"""
Login Authentiction for Battleships game -
Uses Google Sheets API.
"""
# Language and Script Imports
import time
import gspread
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

# Login Functions


def welcome():
    """
    Welcomes the user to the game.
    Prompts user to log into their account.
    """
    title()
    print(Txt.MAIN + "Welcome to Batttleships!\n")
    time.sleep(1)
    new_line()
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


def existing_user():
    """
    Existing user is prompted to enter their password which is checked
    agaisnt the Google Sheet.
    """


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
