import pygame

# Initialize Pygame
pygame.init()

# Set the width and height of the screen (width, height).
screen = pygame.display.set_mode((400, 300))

pygame.display.set_caption("Tic Tac Toe")

# Loop until the user clicks the close button.
done = False

# Used to manage how fast the screen updates
clock = pygame.time.Clock()

# Define some colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Create a 3x3 grid
grid = [[0 for x in range(3)] for y in range(3)]

# Define the player's turn
player = 1

# Function to draw the grid
def draw_grid():
    for row in range(3):
        for column in range(3):
            pygame.draw.rect(screen, WHITE, [100 * column, 100 * row, 100, 100], 2)

# Function to place an X or O in the grid
def place_marker(row, column):
    global player
    if player == 1:
        pygame.draw.line(screen, BLACK, [100 * column + 25, 100 * row + 25], [100 * column + 75, 100 * row + 75], 2)
        pygame.draw.line(screen, BLACK, [100 * column + 75, 100 * row + 25], [100 * column + 25, 100 * row + 75], 2)
        grid[row][column] = 1
        player = 2
    elif player == 2:
        pygame.draw.circle(screen, BLACK, [100 * column + 50, 100 * row + 50], 25, 2)
        grid[row][column] = 2
        player = 1

# Function to check for a win
def check_win():
    for row in range(3):
        if grid[row][0] == grid[row][1] == grid[row][2] and grid[row][0] != 0:
            return True
    for column in range(3):
        if grid[0][column] == grid[1][column] == grid[2][column] and grid[0][column] != 0:
            return True
    if grid[0][0] == grid[1][1] == grid[2][2] and grid[0][0] != 0:
        return True
    if grid[0][2] == grid[1][1] == grid[2][0] and grid[0][2] != 0:
        return True
    return False

# Main game loop
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.MOUSEBUTTONUP:
            pos = pygame.mouse.get_pos()
            row = pos[1] // 100
            column = pos[0] // 100
            place_marker(row, column)
            if check_win():
                print("Player " + str(player) + " wins!")
