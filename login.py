"""
Login Authentiction for Battleships game -
Uses Google Sheets API.
"""
# Language and Script Imports
from google.oauth2 import service_account
import gspread
import time
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
