import pygame
from settings import *

class Cell:
    def __init__(self, xCell, yCell):
        # Cell x, y position
        self.xCell = xCell
        self.yCell = yCell

        # Does the cell have a mine
        self.hasMine = False
        # Has the cell been revealed by the player
        self.revealed = False
        # Has the cell been flagged by the player
        self.flagged = False
        # Number of adjacnet cells that have mines
        self.adjacentMines = 0

        # Draw the cell
        self.rect = pygame.Rect(xCell * cellSize, yCell * cellSize, cellSize, cellSize)