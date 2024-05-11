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

# Function to get available moves
def get_available_moves(board):
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == 0]

# Minimax function
def minimax(board, depth, maximizing_player):
    if check_winner(board, 2):
        return 1
    elif check_winner(board, 1):
        return -1
    elif is_board_full(board):
        return 0

    if maximizing_player:
        max_eval = float('-inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 2
            eval = minimax(board, depth + 1, False)
            board[move[0]][move[1]] = 0
            max_eval = max(max_eval, eval)
        return max_eval
    else:
        min_eval = float('inf')
        for move in get_available_moves(board):
            board[move[0]][move[1]] = 1
            eval = minimax(board, depth + 1, True)
            board[move[0]][move[1]] = 0
            min_eval = min(min_eval, eval)
        return min_eval

# Function to get the best move using minimax
def get_best_move(board):
    best_eval = float('-inf')
    best_move = None
    for move in get_available_moves(board):
        board[move[0]][move[1]] = 2
        eval = minimax(board, 0, False)
        board[move[0]][move[1]] = 0
        if eval > best_eval:
            best_eval = eval
            best_move = move
    return best_move

# Function to play the game against AI
def play_game_vs_ai():
    board = initialize_board()
    current_player = 1

    while True:
        print_board(board)
        if current_player == 1:
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
                    current_player = 2
            else:
                print("Invalid move. Try again.")
        else:
            print("AI is making a move...")
            row, col = get_best_move(board)
            make_move(board, row, col, current_player)
            if check_winner(board, current_player):
                print_board(board)
                print("AI wins!")
                break
            elif is_board_full(board):
                print_board(board)
                print("It's a tie!")
                break
            else:
                current_player = 1

if __name__ == "__main__":
    play_game_vs_ai()
