

the_Board = {"7": " ", "8": " ", "9": " ",
             "4": " ", "5": " ", "6": " ",
             "1": " ", "2": " ", "3": " "}

board_keys = []

for key in the_Board:
    board_keys.append(key)

def printBoard(board):
    print(board['7'] + '|' + board['8'] + '|' + board['9'])
    print('-+-+-')
    print(board['4'] + '|' + board['5'] + '|' + board['6'])
    print('-+-+-')
    print(board['1'] + '|' + board['2'] + '|' + board['3'])

def game():
    turn = 'X'
    count = 0

    for i in range(10):
        printBoard(the_Board)
        print("Its your turn" + turn + ".Move to which place.")

        move = input()

        if the_Board[move] == ' ':
            the_Board[move] = turn
            count += 1
        else:
            print("That place is already taken. Pick another.")
            continue

        if count >= 5:
            if the_Board["7"] == the_Board["8"] == the_Board["9"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
            elif the_Board["4"] == the_Board["5"] == the_Board["6"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
            elif the_Board["1"] == the_Board["2"] == the_Board["3"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
            elif the_Board["1"] == the_Board["4"] == the_Board["7"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
            elif the_Board["2"] == the_Board["5"] == the_Board["8"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
            elif the_Board["3"] == the_Board["6"] == the_Board["9"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
            elif the_Board["7"] == the_Board["5"] == the_Board["3"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
            elif the_Board["1"] == the_Board["5"] == the_Board["9"] != " ":
                printBoard(the_Board)
                print("\nGame Over\n")
                print("The" + turn + "player wins!")
                break
        if count == 9:
            print("\n Game Over \n")
            print("It is a tie.")

        if turn == 'X':
            turn = "O"
        else:
            turn = "X"

    restart = input("Would you like to play again? If yes type 'y'! If no type 'n'!").upper()
    if restart == 'Y':
        for key in board_keys:
            the_Board[key] = " "
        game()


if __name__ == '__main__':
    game()


