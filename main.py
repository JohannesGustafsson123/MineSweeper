
import pygame
import sys
import random
import time

from settings import *
from cell import Cell

# Create the grid
def createGrid(cols, rows):
    grid = [[Cell(x, y) for y in range(rows)] for x in range(cols)]
    # Place all mines
    placedMines = 0
    while placedMines < mineCount:
        x = random.randint(0, cols - 1)
        y = random.randint(0, rows - 1)
        # Check if grid already has a mine.
        if not grid[x][y].hasMine:
            grid[x][y].hasMine = True
            placedMines += 1
    # Count adjacent mines.
    for col in grid:
        for cell in col:
            cell.countAdjacent(grid)

    return grid

def revealEmpty(cell, grid):
    # Check if cell has already been revealed or flagged.
    if cell.revealed or cell.flagged:
        return
    
    cell.revealed = True
    # Check if cell has no mines next to it and it's not a mine.
    if cell.adjacentMines == 0 and not cell.hasMine:
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = cell.xCell + dx, cell.yCell + dy
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    revealEmpty(grid[nx][ny], grid)

def checkWin(grid):
    # Loop through all cells, check if all non-mine cells have been revealed.
    for col in grid:
        for cell in col:
            if not cell.revealed and not cell.hasMine:
                return False
    return True

def main():
    pygame.init()
    font = pygame.font.SysFont(None, 32)

    screen_width = 600
    screen_height = 650
    screen = pygame.display.set_mode((screen_width, screen_height))
    pygame.display.set_caption("Minesweeper")

    cols = screen_width // cellSize
    rows = (screen_height - 50) // cellSize

    grid = createGrid(cols, rows)

    flagCount = 0
    gameOver = False
    won = False

    # Restart button.
    restartButton = pygame.Rect(250, 10, 100, 30)

    # Timer setup
    startTicks = pygame.time.get_ticks()
    totalTime = startTime

    clock = pygame.time.Clock()

    running = True
    while running:
        dt = clock.tick(fps) / 1000  # x seconds since last frame

        screen.fill(colors["LIGHTGRAY"])

        # Calculate remaining time
        if not gameOver:
            secondsPassed = (pygame.time.get_ticks() - startTicks) / 1000
            elapsedTime = max(0, totalTime - int(secondsPassed))
        else:
            elapsedTime = max(0, elapsedTime)  # freeze timer if you loose (shitcan)

        # Check if time is up
        if elapsedTime <= 0 and not gameOver:
            gameOver = True
            won = False

        # Time, flag count.
        timeText = font.render(f"Time: {elapsedTime}s", True, colors["BLACK"])
        flagText = font.render(f"Flags: {flagCount}/{mineCount}", True, colors["BLACK"])
        screen.blit(timeText, (10, 10))
        screen.blit(flagText, (400, 10))

        # Draw restart button.
        pygame.draw.rect(screen, colors["GREEN"], restartButton)
        restartLabel = font.render("Restart", True, colors["BLACK"])
        screen.blit(restartLabel, restartLabel.get_rect(center=restartButton.center))

        # Draw cells.
        for col in grid:
            for cell in col:
                cell.draw(screen)
        # Check if game is over.
        if gameOver:
            endText = "You Win :D" if won else "Game Over, bloody noob"
            label = font.render(endText, True, colors["RED"])
            screen.blit(label, label.get_rect(center=(screen_width // 2, screen_height - 20)))

        # Mouse events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()

                # Check if restart button clicked
                if restartButton.collidepoint(mx, my):
                    grid = createGrid(cols, rows)
                    flagCount = 0
                    gameOver = False
                    won = False
                    startTicks = pygame.time.get_ticks()  # reset timer
                    continue
                
                if my >= 50 and not gameOver:
                    gridX = mx // cellSize
                    gridY = (my - 50) // cellSize
                    cell = grid[gridX][gridY]

                    if event.button == 1 and not cell.flagged:  # Left click
                        # Check if cell has mine
                        if cell.hasMine:
                            cell.revealed = True
                            gameOver = True
                            won = False
                        else:
                            revealEmpty(cell, grid)
                            if checkWin(grid):
                                gameOver = True
                                won = True

                    elif event.button == 3 and not cell.revealed:  # Right click
                        cell.flagged = not cell.flagged
                        flagCount += 1 if cell.flagged else -1

        pygame.display.flip()

    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
