import random

# pypi.org colorama article on adding color to the terminal
import colorama
colorama.init(autoreset = True)

# Love Sandwiches walk-through on APIs
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('double_dice')

score = SHEET.worksheet('score')

data = score.get_all_values()


def welcome_msg():
    """
    A welcome message to greet the player and explain the rules.
    """
    print("")
    print("")
    print("")
    print("")
    print("*** Welcome To ***")
    print(" ___           _    _       ___  _       ")
    print("|   \ ___ _  _| |__| |___  |   \(_)__ ___ ")
    print("| |) / _ | || | '_ | / -_) | |) | / _/ -_)")
    print("|___/\___/\_,_|_.__|_\___| |___/|_\__\___|")