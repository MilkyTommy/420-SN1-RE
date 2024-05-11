import numpy as np

# Function to initialize the board
def initialize_board():
    return np.zeros((3, 3), dtype=int)

# Function to print the board
def print_board(board):
    symbols = {0: ' ', 1: 'X', 2: 'O'}
    for row in board:
        print(" | ".join(symbols[val] for val in row))
        print("-" * 5)

# Function to check if the board is full
def is_board_full(board):
    return not np.any(board == 0)

# Function to check if there is a winner
def check_winner(board, player):
    # Check rows and columns
    if np.any(np.all(board == player, axis=0)) or np.any(np.all(board == player, axis=1)):
        return True
    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Function to check if the move is valid
def is_valid_move(board, row, col):
    return board[row][col] == 0

# Function to make a move
def make_move(board, row, col, player):
    if is_valid_move(board, row, col):
        board[row][col] = player
        return True
    return False

# Function to play the game
def play_game():
    board = initialize_board()
    current_player = 1

    while True:
        print_board(board)
        row = int(input(f"Player {current_player}, enter row (0-2): "))
        col = int(input(f"Player {current_player}, enter column (0-2): "))

        if make_move(board, row, col, current_player):
            if check_winner(board, current_player):
                print_board(board)
                print(f"Player {current_player} wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = 2 if current_player == 1 else 1
        else:
            print("Invalid move. Try again.")

if __name__ == "__main__":
    play_game()
