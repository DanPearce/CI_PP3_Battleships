"""
Login Authentiction for Battleships game -
Uses Google Sheets API.
"""
# Language and Script Imports
from google.oauth2 import service_account
import gspread

# Global Variables
SCOPE = ['https://www.googleapis.com/auth/spreadsheets',
         'https://www.googleapis.com/auth/drive.file',
         'https://www.googleapis.com/auth/drive']
CREDS = service_account.Credentials.from_service_account_file('creds.json',
                                                              scopes=SCOPE)
CLIENT = gspread.authorize(CREDS)
USERNAME_DATA = CLIENT.open('battleships_usernames').sheet1

# Login Functions
