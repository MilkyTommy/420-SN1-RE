import pygame
import numpy as np

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (in pixels)
WIDTH, HEIGHT = 600, 400

# Set the number of cells in each direction
CELL_SIZE = 10
NUM_ROWS = HEIGHT // CELL_SIZE
NUM_COLS = WIDTH // CELL_SIZE

# Set the colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Create the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Conway's Game of Life")

# Initialize the grid
grid = np.zeros((NUM_ROWS, NUM_COLS))

# Function to initialize the grid with random values
def initialize_grid():
    return np.random.choice([0, 1], size=(NUM_ROWS, NUM_COLS))

# Function to draw the grid
def draw_grid():
    screen.fill(WHITE)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            if grid[row][col] == 1:
                pygame.draw.rect(screen, BLACK, (col * CELL_SIZE, row * CELL_SIZE, CELL_SIZE, CELL_SIZE))

# Function to update the grid based on the rules of Conway's Game of Life
def update_grid():
    new_grid = np.copy(grid)
    for row in range(NUM_ROWS):
        for col in range(NUM_COLS):
            num_neighbors = np.sum(grid[max(0, row - 1):min(NUM_ROWS, row + 2), max(0, col - 1):min(NUM_COLS, col + 2)]) - grid[row][col]
            if grid[row][col] == 1:
                if num_neighbors < 2 or num_neighbors > 3:
                    new_grid[row][col] = 0
            else:
                if num_neighbors == 3:
                    new_grid[row][col] = 1
    return new_grid

# Main function
def main():
    grid[:] = initialize_grid()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        draw_grid()
        grid[:] = update_grid()

        pygame.display.flip()
        pygame.time.delay(100)

    pygame.quit()

if __name__ == "__main__":
    main()
