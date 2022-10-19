import pygame
from settings import *
from sys import *


def main():
    screen = pygame.display.set_mode(SCREENSIZE)
    pygame.display.set_caption("Timer")
    clock = pygame.time.Clock()


if __name__ == '__main__':
    main()