
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
        if not grid[x][y].hasMine:
            grid[x][y].hasMine = True
            placedMines += 1
    
    for col in grid:
        for cell in col:
            cell.countAdjacent(grid)

    return grid

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