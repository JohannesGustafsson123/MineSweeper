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

    # Draw the cell 
    def draw(self, surface):
        if self.revealed:
            # If the cell is revealed, fill it with gray color
            pygame.draw.rect(surface, colors["GRAY"], self.rect)
            if self.hasMine:
                # If the cell has a mine, fill it with a red circle
                pygame.draw.circle(surface, colors["RED"], self.rect.center, cellSize // 4)
            elif self.adjacentMines > 0:
                # If there are other mines next to it, display the number in black text on the cell.
                font = pygame.font.SysFont(None, 24)
                text = font.render(str(self.adjacentMines), True, colors["BLACK"])
                surface.blit(text, text.get_rect(center=self.rect.center))
        else:
            # If the cell is not revealed, fill it with white color
            pygame.draw.rect(surface, colors["WHITE"], self.rect)
            # If the cell is flagged, draw a blue circle
            if self.flagged:
                pygame.draw.circle(surface, colors["BLUE"], self.rect.center, cellSize // 4)