
import pygame

from settings import *
from cell import Cell

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