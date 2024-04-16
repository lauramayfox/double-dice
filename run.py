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
    print("\033[31m" + "┌ ─  - ┐  ┌ ─  - ┐")
    print("\033[31m" + "| ●    |  | ●    |")
    print("\033[31m" + "|    ● |  |    ● |")
    print("\033[31m" + "└ - -  ┘  └ - -  ┘")
    print("*** Welcome To ***")
    print("Double Dice")
    print("\033[31m" + "┌ ─  - ┐  ┌ ─  - ┐")
    print("\033[31m" + "| ●    |  | ●    |")
    print("\033[31m" + "|    ● |  |    ● |")
    print("\033[31m" + "└ - -  ┘  └ - -  ┘\n")

    player = get_player_name()

    print(f"\nAlright, {player}, the rules of the game are:")
    print(
        """
        The aim is to roll 2 of the same numbers...
        Double or nothing...
        Try to beat your highest score!
        """)
    return player

def get_player_name():
    """
    A function to get the player's name and
    ensure only letters used.
    """

    while True:
        name = input("What is your name?: ")
        if name.isalpha():
            return name
        else:
            print("Not a valid input, please try again")

            
def main():
    player = welcome_msg()

main()