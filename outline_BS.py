from random import randint
import os

board = []

for x in range(6):
    board.append(["O"] * 6)


def print_board(board):
    for row in board:
        print((" ").join(row))


def random_row(board):
    return randint(0, len(board) - 1)


def random_col(board):
    return randint(0, len(board[0]) - 1)


def get_username():
    username_file = "username.txt"
    if not os.path.isfile(username_file):
        fo = open(username_file, "a")
        fo.close()

    if os.stat(username_file).st_size == 0:
        fo = open(username_file, "a+")
        print("No saved username.")
        username = input("Enter username:")
        choice = input("Enter 1 to save username or enter any key to continue")
        if choice == "1":
            fo.write(username + "\n")
        fo.close()

    else:
        fo = open(username_file, "r")
        lines = fo.readlines()
        num = 1
        for line in lines:
            print(num, line.strip())
            num += 1
        username_num = int(input("Enter the number of your username or enter 0 to add new username:"))
        if username_num == 0:
            username = input("Enter username:")
            choice = input("Enter 1 to save username or enter any key to continue")
            if choice == "1":
                fo = open(username_file, "a+")
                fo.write(username + "\n")
            fo.close()
        else:
            while username_num > num:
                print("Invalid input!")
                username_num = int(input("Enter the number of your username:"))
            fo = open(username_file, "r")
            username = ""
            for count in range(username_num):
                username = fo.readline()
            fo.close()
            username = username.strip()
    print("Welcome " + username + "!")
    print("Let's play Battleship!")


def ask_guess():
    guess_num = int(input("Enter the number of turns you need (from 1-20): "))
    while guess_num < 1 or guess_num > 20:
        print("Invalid input!")
        guess_num = int(input("Enter the number of turns you need (from 1-20): "))
    return guess_num


get_username()
guess_num = ask_guess()
print_board(board)
ship_row = random_row(board)
ship_col = random_col(board)

turn_left = guess_num - 1;
for turn in range(guess_num):
    print("Turn ", turn + 1)
    print("Turn left: ", turn_left)
    guess_row = int(input("Guess Row:"))
    guess_col = int(input("Guess Col:"))

    if guess_row == ship_row and guess_col == ship_col:
        print("Congratulations! You sunk my battleship!")
        board[guess_row][guess_col] = "-"
        print_board(board)
        print("You won!")
        break
    else:
        if (guess_row < 0 or guess_row > 5) or (guess_col < 0 or guess_col > 5):
            print("Oops, that's not even in the ocean.")
        elif (board[guess_row][guess_col] == "X"):
            print("You guessed that one already.")
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"
    print_board(board)
    if (turn + 1) == guess_num:
        print("Game Over")
    else:
        turn_left -= 1
