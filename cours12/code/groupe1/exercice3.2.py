import pygame
import numpy as np
import sys

# Initialize Pygame
pygame.init()

# Set the dimensions of the window
WIDTH, HEIGHT = 300, 300
LINE_WIDTH = 10
BOARD_ROWS, BOARD_COLS = 3, 3
CELL_WIDTH = WIDTH // BOARD_COLS
CELL_HEIGHT = HEIGHT // BOARD_ROWS
FPS = 60

# Set colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Set up the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tic Tac Toe")

# Initialize the board
board = np.zeros((BOARD_ROWS, BOARD_COLS))

# Function to draw the board
def draw_board():
    screen.fill(WHITE)
    for row in range(1, BOARD_ROWS):
        pygame.draw.line(screen, BLACK, (0, row * CELL_HEIGHT), (WIDTH, row * CELL_HEIGHT), LINE_WIDTH)
    for col in range(1, BOARD_COLS):
        pygame.draw.line(screen, BLACK, (col * CELL_WIDTH, 0), (col * CELL_WIDTH, HEIGHT), LINE_WIDTH)

# Function to draw the symbols
def draw_symbols():
    for row in range(BOARD_ROWS):
        for col in range(BOARD_COLS):
            if board[row][col] == 1:
                pygame.draw.circle(screen, BLACK, (int(col * CELL_WIDTH + CELL_WIDTH / 2), int(row * CELL_HEIGHT + CELL_HEIGHT / 2)), min(CELL_WIDTH, CELL_HEIGHT) // 3, LINE_WIDTH)
            elif board[row][col] == 2:
                pygame.draw.line(screen, RED, (col * CELL_WIDTH + CELL_WIDTH // 4, row * CELL_HEIGHT + CELL_HEIGHT // 4), (col * CELL_WIDTH + 3 * CELL_WIDTH // 4, row * CELL_HEIGHT + 3 * CELL_HEIGHT // 4), LINE_WIDTH)
                pygame.draw.line(screen, RED, (col * CELL_WIDTH + CELL_WIDTH // 4, row * CELL_HEIGHT + 3 * CELL_HEIGHT // 4), (col * CELL_WIDTH + 3 * CELL_WIDTH // 4, row * CELL_HEIGHT + CELL_HEIGHT // 4), LINE_WIDTH)

# Function to check if the board is full
def is_board_full():
    return not np.any(board == 0)

# Function to check if there is a winner
def check_winner(player):
    # Check rows and columns
    if np.any(np.all(board == player, axis=0)) or np.any(np.all(board == player, axis=1)):
        return True
    # Check diagonals
    if np.all(np.diag(board) == player) or np.all(np.diag(np.fliplr(board)) == player):
        return True
    return False

# Function to get the cell clicked by the player
def get_clicked_cell(pos):
    row = pos[1] // CELL_HEIGHT
    col = pos[0] // CELL_WIDTH
    return row, col

# Main game loop
def main():
    global board

    turn = 1  # Player 1 starts

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.MOUSEBUTTONDOWN:
                if turn == 1:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_cell(pos)
                    if board[row][col] == 0:
                        board[row][col] = 1
                        if check_winner(1):
                            print("Player 1 wins!")
                            pygame.quit()
                            sys.exit()
                        elif is_board_full():
                            print("It's a tie!")
                            pygame.quit()
                            sys.exit()
                        turn = 2
                else:
                    pos = pygame.mouse.get_pos()
                    row, col = get_clicked_cell(pos)
                    if board[row][col] == 0:
                        board[row][col] = 2
                        if check_winner(2):
                            print("Player 2 wins!")
                            pygame.quit()
                            sys.exit()
                        elif is_board_full():
                            print("It's a tie!")
                            pygame.quit()
                            sys.exit()
                        turn = 1

        draw_board()
        draw_symbols()
        pygame.display.flip()
        pygame.time.Clock().tick(FPS)

if __name__ == "__main__":
    main()
