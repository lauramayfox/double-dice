import random
import time
import os

# pypi.org colorama article on adding color to the terminal
import colorama
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive",
]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("double_dice")

SCORE_SHEET = SHEET.worksheet("score")

colorama.init(autoreset=True)

# ● ┌ ─ ┐ │ └ ┘ Dice pieces for welcome message


def welcome_msg():
    """
    A welcome message to greet the player and explain the rules.
    """
    print("\033[31m" + "┌ ─  - ┐  ┌ ─  - ┐")
    print("\033[31m" + "| ●    |  | ●    |")
    print("\033[31m" + "|    ● |  |    ● |")
    print("\033[31m" + "└ - -  ┘  └ - -  ┘\n")
    print("*** Welcome To ***")
    print(" ___           _    _       ___  _")
    print("|   \ ___ _  _| |__| |___  |   \(_)__ ___")
    print("| |) / _ | || | '_ | / -_) | |) | / _/ -_)")
    print("|___/\___/\_,_|_.__|_\___| |___/|_\__\___|")
    print("")
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
        1 point per double..
        Try to beat your highest score!
        """
    )
    return player


def get_player_name():
    """
    A function to get the player's name and
    ensure only letters used.
    """

    while True:
        name = input("What is your name?:\n")
        if name.isalpha():
            return name
        else:
            print("Not a valid input, please try again")


def view_scoreboard(player):
    """
    A function to view previous high scores
    """
    while True:
        view_scoreboard = input(
            "Would you like to view previous highest score? y or n:\n"
        )

        if view_scoreboard == "y":
            print("The highest score of all time is:", load_high_score())
            time.sleep(1)
            break
        elif view_scoreboard == "n":
            break
            main()
        else:
            print("\nNot a valid input. Please select y or n \n")


def start_game(player):
    """
    A function to check if user is ready to start the game
    """
    while True:
        start_answer = input("Start new game select y or n:\n")

        if start_answer == "y":
            print("\033[31m" + "\n Let's Roll...")
            time.sleep(1)
            break
        elif start_answer == "n":
            print("\033[31m" + "See you on the next roll!")
            quit()
        else:
            print("\nPlease answer y or n \n")


def play_game(player):
    """
    A function for the main game component
    """
    roll_again = "y"
    score = 0
    while roll_again == "y":
        print("Rolling the dice...")
        time.sleep(1)

        dice1 = random.randint(1, 6)
        dice2 = random.randint(1, 6)
        print("The values are: ")
        print("Dice 1 = ", dice1)
        print("Dice 2 = ", dice2)

        if dice1 == dice2:
            print("\033[32m" + "You rolled a double! You win!")
            score += 1
        else:
            print("\033[31m" + "Keep trying")

        roll_again = input("Roll the dice again? y or n: \n")
        while roll_again.lower() not in ("y", "n"):
            print("\nNot a valid input. Please select y or n\n")
            roll_again = input("Roll the dice again? y or n: \n")

    if roll_again == "n":
        print("\033[31m" + "See you on the next roll!")
        print(f"Your total score this game: {score}")
        save_high_score(score)
        quit()


def load_high_score():
    """
    Gives an option to view previous high scores when game starts
    """
    try:
        return int(SCORE_SHEET.acell("A1").value)
    except ValueError:
        print("Warning: Unable to convert high score to an integer.")
        return 0


def save_high_score(new_score):
    """
    Saves the highest scores to an external google spreadsheet file
    if it is greater than the high score in the document
    """
    current_high_score = load_high_score()

    if new_score > current_high_score:
        SCORE_SHEET.update(range_name="A1", values=[[new_score]])
        print("Congratulations! New high score saved.")


def main():
    """
    Sequence of events for the game play
    """
    player = welcome_msg()
    view_scoreboard(player)
    start_game(player)
    load_high_score()
    play_game(player)
    save_high_score(new_score)


main()
