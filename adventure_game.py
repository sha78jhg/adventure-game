# This is a simple adventure game created in Python
# Player explores different locations and makes choices
import time

print("Welcome to the game!")
time.sleep(2)  # Wait for 2 seconds
print("You find yourself in a dark room with no windows. You're not sure how you got here, but you know you need to find a way out.")
time.sleep(3)  # Wait for 3 seconds
print("Your goal is to explore the room, look for clues, and solve puzzles that will help you escape.")

import time
import random


def print_pause(message, delay=2):
    print(message)
    time.sleep(delay)


MAX_TURNS = 3  # Maximum number of turns allowed
WIN_SCORE = 5  # Score required to win the game


def door_left():
    global score  # Use the global keyword to modify the score variable
    print_pause("You chose the door on the left.")
    score += 1  # Increase the score by 1
    print_pause(f"Your score is now {score}.")
    # add more code here for what happens when the player chooses this option


def door_right():
    global score  # Use the global keyword to modify the score variable
    print_pause("You chose the door on the right.")
    score += 2  # Increase the score by 2
    print_pause(f"Your score is now {score}.")
    # add more code here for what happens when the player chooses this option


def choose_door():
    global turns
    valid_input = False
    while not valid_input:
        print_pause("You see two doors in front of you. Which one do you choose?")
        door = input("Enter 1 to choose the door on the left, or 2 to choose the door on the right: ")
        if door == "1":
            door_left()
            valid_input = True
        elif door == "2":
            door_right()
            valid_input = True
        else:
            print_pause("Sorry, I didn't understand that. Please enter 1 or 2.")

    turns += 1  # Increase the number of turns by 1


def play_game():
    global score, turns
    score = 0  # Initialize the score to zero
    turns = 0  # Initialize the number of turns to zero
    print_pause("Welcome to the game!")
    print_pause(
        "You find yourself in a dark room with no windows. You're not sure how you got here, but you know you need to find a way out.")
    print_pause("Your goal is to explore the room, look for clues, and solve puzzles that will help you escape.",
                delay=3)

    enemy = random.choice(["pirate", "troll", "dragon", "giant", "zombie"])  # Choose a random enemy creature
    print_pause(f"You encounter a {enemy}! Defeat it to earn points and move closer to the exit.")

    while turns < MAX_TURNS:
        choose_door()
        if score >= WIN_SCORE:
            print_pause("Congratulations! You have escaped the room and won the game!")
            return True
        print_pause(f"You have {MAX_TURNS - turns} turn(s) left.")

    print_pause(f"Sorry, you didn't escape the room in time. Your final score is {score}.")
    return False
import random

# Define game state variables
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
player_turn = "X"
game_over = False
score = {"X": 0, "O": 0}

# Define function to print the game board
def print_board():
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[0], board[1], board[2]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[3], board[4], board[5]))
    print("___|___|___")
    print("   |   |   ")
    print(" {} | {} | {} ".format(board[6], board[7], board[8]))
    print("   |   |   ")

# Define function to check if the game is over
def check_game_over():
    global game_over
    # Check for a win
    if (board[0] == board[1] == board[2] != " ") or \
       (board[3] == board[4] == board[5] != " ") or \
       (board[6] == board[7] == board[8] != " ") or \
       (board[0] == board[3] == board[6] != " ") or \
       (board[1] == board[4] == board[7] != " ") or \
       (board[2] == board[5] == board[8] != " ") or \
       (board[0] == board[4] == board[8] != " ") or \
       (board[2] == board[4] == board[6] != " "):
        print("{} wins!".format(player_turn))
        score[player_turn] += 1
        game_over = True
    # Check for a tie
    elif " " not in board:
        print("It's a tie!")
        game_over = True

# Main game loop
while not game_over:
    # Print the current game state
    print("Score: X={}, O={}".format(score["X"], score["O"]))
    print_board()
    print("It's {}'s turn.".format(player_turn))
    # Get the player's move
    valid_move = False
    while not valid_move:
        move = input("Enter a number from 1-9 to place your mark: ")
        if move.isdigit() and int(move) in range(1, 10) and board[int(move)-1] == " ":
            board[int(move)-1] = player_turn
            valid_move = True
        else:
            print("Invalid move. Please try again.")
    # Check if the game is over
    check_game_over()
    # Switch to the other player's turn
    if player_turn == "X":
        player_turn = "O"
    else:
        player_turn = "X"


def play_again():
    while True:
        answer = input("Would you like to play again? (y/n): ")
        if answer == "y":
            return True
        elif answer == "n":
            return False
        else:
            print_pause("Sorry, I didn't understand that. Please enter 'y' or 'n'.")


def main():
    while True:
        if play_game():
            if play_again():
                continue
            else:
                break
        else:
            if play_again():
                continue
            else:
                break

    print_pause("Thanks for playing! Goodbye.")


main()
