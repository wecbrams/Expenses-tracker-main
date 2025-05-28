import random
from colorama import init, Fore, Style

init(autoreset=True)

# Display the game board with colors
def display_board(board):
    def colored(cell):
        if cell == 'X':
            return Fore.RED + cell + Style.RESET_ALL
        elif cell == 'O':
            return Fore.BLUE + cell + Style.RESET_ALL
        else:
            return Fore.YELLOW + cell + Style.RESET_ALL

    print()
    print(f"{colored(board[0])} | {colored(board[1])} | {colored(board[2])}")
    print("--+---+--")
    print(f"{colored(board[3])} | {colored(board[4])} | {colored(board[5])}")
    print("--+---+--")
    print(f"{colored(board[6])} | {colored(board[7])} | {colored(board[8])}")
    print()

# Let player choose X or O
def player_choice():
    while True:
        symbol = input(Fore.GREEN + "Do you want to be X or O? " + Style.RESET_ALL).upper()
        if symbol in ['X', 'O']:
            return (symbol, 'O' if symbol == 'X' else 'X')

# Player move input
def player_move(board, symbol):
    while True:
        try:
            move = int(input("Enter your move (1-9): "))
            if move in range(1, 10) and board[move - 1].isdigit():
                board[move - 1] = symbol
                break
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Please enter a number between 1 and 9.")

# Simple AI move logic
def ai_move(board, ai_symbol, player_symbol):
    # Try to win
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = ai_symbol
            if check_win(board_copy, ai_symbol):
                board[i] = ai_symbol
                return
    # Try to block
    for i in range(9):
        if board[i].isdigit():
            board_copy = board.copy()
            board_copy[i] = player_symbol
            if check_win(board_copy, player_symbol):
                board[i] = ai_symbol
                return
    # Random move
    possible_moves = [i for i in range(9) if board[i].isdigit()]
    move = random.choice(possible_moves)
    board[move] = ai_symbol

# Check win condition
def check_win(board, symbol):
    win_conditions = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),  # Horizontal
        (0, 3, 6), (1, 4, 7), (2, 5, 8),  # Vertical
        (0, 4, 8), (2, 4, 6)              # Diagonal
    ]
    for cond in win_conditions:
        if board[cond[0]] == board[cond[1]] == board[cond[2]] == symbol:
            return True
    return False

# Check if board is full
def check_full(board):
    return all(not spot.isdigit() for spot in board)

# Main game loop
def tic_tac_toe():
    print(Fore.CYAN + "Welcome to Tic-Tac-Toe!")
    player_name = input(Fore.GREEN + "Enter your name: " + Style.RESET_ALL)
    
    while True:
        board = [str(i+1) for i in range(9)]
        player_symbol, ai_symbol = player_choice()
        turn = "Player"
        game_on = True

        while game_on:
            display_board(board)
            if turn == "Player":
                player_move(board, player_symbol)
                if check_win(board, player_symbol):
                    display_board(board)
                    print(Fore.GREEN + f"Congratulations {player_name}, you won!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!")
                    break
                else:
                    turn = "AI"
            else:
                ai_move(board, ai_symbol, player_symbol)
                if check_win(board, ai_symbol):
                    display_board(board)
                    print(Fore.RED + "AI has won the game!")
                    game_on = False
                elif check_full(board):
                    display_board(board)
                    print(Fore.YELLOW + "It's a tie!")
                    break
                else:
                    turn = "Player"

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            print("Thank you for playing!")
            break

# Run the game
if __name__ == "__main__":
    tic_tac_toe()
