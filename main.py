
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



def main():
    # Initialize Pygame
    pygame.init()

    # Set up display
    screen_width = 600
    screen_height = 600
    screen = pygame.display.set_mode((screen_width, screen_height))

    # Set up caption
    pygame.display.set_caption("Minesweeper")


    # 
    screen.fill((colors["LIGHTGRAY"]))  # Light gray background




if __name__ == "__main__":
    main()