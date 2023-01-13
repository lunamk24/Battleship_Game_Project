from random import randint
import os

board = []
player = "Choice"
play = "y"

while play == "y":

    #player = input("Do you want to play Single Mode or Dual Mode (S/D): ")

    i = 2;
    while (i < 3 or i > 9) :
        i = int(input("Choose your board size: "))
        if i < 3:
            print("Choose a size larger than 2")
        elif i > 9:
            print("Choose a size smaller than 10")

    for x in range(i):
        board.append(["O"] * i)


    def print_board(board):
        for row in board:
            print((" ").join(row))


    def random_row(board):
        return randint(0, len(board) - 1)


    def random_col(board):
        return randint(0, len(board[0]) - 1)

    #if(player is "S"):
    #Aurielle & Luna's Code
    def get_username():
        username_file = "username.txt"
        if not os.path.isfile(username_file):
            fo = open(username_file, "a")
            fo.close()

        if os.stat(username_file).st_size == 0:
            fo = open(username_file, "a+")
            print("No saved username.")
            username = input("Enter username:")
            choice = input("Enter 1 to save username or enter any key to continue : ")
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
    #File handling ---- done

    def ask_guess():
        guess_num = int(input("Enter the number of turns you need (from 1-20): "))
        while guess_num < 1 or guess_num > 20:
            print("Invalid input!")
            guess_num = int(input("Enter the number of turns you need (from 1-20): "))
        return guess_num

    #if(player is "S"):
    get_username()

    guess_num = ask_guess()
    print_board(board)
    ship_row = random_row(board)
    ship_col = random_col(board)

    turn_left = guess_num - 1;

    #Random position
    def random_pos(board):
        return randint(0, len(board) - 1)

    ship_row = []
    ship_col = []

    # number of ships = row size - 1
    for ships in range(i - 2):
        ship_row.append(random_pos(board))
        ship_col.append(random_pos(board))
        print("There is a ship at row", ship_row[ships] + 1, "column", ship_col[ships] + 1)

    ships = i - 2

    #Playing the Game
    for turn in range(guess_num):
        print(guess_num - turn, "turns left")
        guess_row = (int(input("Guess Row: ")) - 1)
        guess_col = (int(input("Guess Col: ")) - 1)

        if guess_row in ship_row and guess_col in ship_col:
            board[guess_row][guess_col] = "@"
            ships -= 1
            if ships == 0:
                print("Congratulations! You sunk all my battleship!")
                break
            else:
                print("You sunk my battleship!", ships, "more remaining")
        elif (guess_row < 0 or guess_row > i - 1) or (guess_col < 0 or guess_col > i - 1):
            print("Oops, that's not even in the ocean.")
            turn -= 1
        elif board[guess_row][guess_col] == "X":
            print("You guessed that one already.")
            turn -= 1
        else:
            print("You missed my battleship!")
            board[guess_row][guess_col] = "X"

        if turn + 1 == guess_num:
            print("Game Over")
            for x in range(i - 2):
                board[int(ship_row[x])][int(ship_col[x])] = "@"
        print_board(board)

    play = input("Try again?(y/n) : ")
    print(" ")
