# Two Player Tic-Tac-Toe Game in Python

# Create the board
theBoard = {
    '7': ' ', '8': ' ', '9': ' ',
    '4': ' ', '5': ' ', '6': ' ',
    '1': ' ', '2': ' ', '3': ' '
}
# Function to print the board
def printBoard(board):
    print()
    print(board['7'] + ' | ' + board['8'] + ' | ' + board['9'])   
    print('--+---+--')
    print(board['4'] + ' | ' + board['5'] + ' | ' + board['6'])
    print('--+---+--')
    print(board['1'] + ' | ' + board['2'] + ' | ' + board['3'])
    print()

# Function to check winner
def checkWin(board, turn):
    win_patterns = [
        ['7','8','9'], ['4','5','6'], ['1','2','3'],  # rows
        ['7','4','1'], ['8','5','2'], ['9','6','3'],  # columns
        ['7','5','3'], ['1','5','9']                  # diagonals
    ]

    for pattern in win_patterns:
        if board[pattern[0]] == board[pattern[1]] == board[pattern[2]] == turn:
            return True

    return False

# Main game function
def game():

    turn = 'X'
    count = 0

    while True:
        printBoard(theBoard)
        move = input(f"Player {turn}, choose position (1-9): ")

        # Check for invalid position
        if move not in theBoard:
            print("Invalid position! Choose a number from 1-9.")
            continue
        # Check if space is free
        if theBoard[move] != ' ':
            print("That position is already taken!")
            continue
        # Place move
        theBoard[move] = turn
        count += 1
        # Check for win
        if count >= 5:
            if checkWin(theBoard, turn):
                printBoard(theBoard)
                print("🎉 Game Over!")
                print(f"Player {turn} wins!")
                break

        # Check for tie
        if count == 9:
            printBoard(theBoard)
            print("🤝 Game Over!")
            print("It's a Tie!")
            break

        # Switch player
        turn = 'O' if turn == 'X' else 'X'

    # Ask to restart
    restart = input("Play again? (y/n): ")

    if restart.lower() == 'y':
        for key in theBoard:
            theBoard[key] = ' '
        game()
    else:
        print("Thanks for playing!")

# Run the game
if __name__ == "__main__":
    game()