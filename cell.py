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
        offsetRect = self.rect.move(0, 50)
        if self.revealed:
            # If the cell is revealed, fill it with gray color
            pygame.draw.rect(surface, colors["GRAY"], offsetRect)
            if self.hasMine:
                # If the cell has a mine, fill it with a red circle
                pygame.draw.circle(surface, colors["RED"], offsetRect.center, cellSize // 4)
            elif self.adjacentMines > 0:
                # If there are other mines next to it, display the number in black text on the cell.
                font = pygame.font.SysFont(None, 24)
                text = font.render(str(self.adjacentMines), True, colors["BLACK"])
                surface.blit(text, text.get_rect(center=offsetRect.center))
        else:
            # If the cell is not revealed, fill it with white color
            pygame.draw.rect(surface, colors["WHITE"], offsetRect)
            # If the cell is flagged, draw a blue circle
            if self.flagged:
                pygame.draw.circle(surface, colors["BLUE"], offsetRect.center, cellSize // 4)
        
    def countAdjacent(self, grid):
        # If the cell has a mine return
        if self.hasMine:
            return

        count = 0
        # Loop through all cells that are within 1 tile.
        for dx in [-1, 0, 1]:
            for dy in [-1, 0, 1]:
                nx, ny = self.xCell + dx, self.yCell + dy
                # Make sure the cell is inside the grid
                if 0 <= nx < len(grid) and 0 <= ny < len(grid[0]):
                    # If the cell has a mine, increase the count.
                    if grid[nx][ny].hasMine:
                        count += 1
        self.adjacentMines = count