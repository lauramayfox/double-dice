import random
import time
import os

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
    time.sleep(1)
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


def start_game(player):
    """
    A function to check if user is ready to start the game
    """
    while True:
        start_answer = input("Start new game select y or n: ")

        if start_answer == "y":
            print("\033[31m" + "\n Let's Roll...")
            time.sleep(1)     
            break
        elif start_answer == "n":
            print("\033[31m" + "See you on the next roll!") 
        else:
            print("\nPlease answer y or n: \n")
        
def play_game(player):
    roll_again = "y"
    score = 0
    while roll_again == "y":
        print("Rolling the dice...")
        time.sleep(1)

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("The values are: ")
        print("Dice 1: ", dice1)
        print("Dice 2: ", dice2)

    if dice1 == dice2:
        print("\033[32m" + "You rolled a double! YOU WIN!")     
        score += 1
    else:
        print("\033[31m" + "Keep trying")

        roll_again = input("Roll the dice again? y or n: \n")
        if roll_again == "n":
            print("\033[31m" + "See you on the next roll!")
            print(f"Your total score this game: {score}")
            save_high_score(score)


# Adaption from Quora q&a on scoreboard trackers

def save_high_score(score):
    """
    Saves the highest scores to an external google spreadsheet file
    """
    with open(SHEET.worksheet('score'), "w") as file:
        file.write(str(score))


def load_high_score():
    """ 
    Gives an option to view previous high scores when game starts
    """
    if os.path.exists(SHEET.worksheet('score')):
        with open("SHEET.worksheet('score')", "r") as file:
            return int(file.read())
    else:
        return 0

def main():
    """
    Sequence of events for the game play
    """
    player = welcome_msg()
    start_game(player)
    play_game(player)
    load_high_score()

main()