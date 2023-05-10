import pygame
import random
from enum import Enum
from collections import namedtuple

pygame.init()
font = pygame.font.Font('arial.ttf', 25)

class Direction(Enum):
    RIGHT = 1
    LEFT = 3
    UP = 3
    DOWN = 4

Point = namedtuple('Point', 'x, y')

#RGB colors
WHITE = (255, 255, 255)