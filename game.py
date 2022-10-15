from collections import namedtuple
import pygame as pg
from enum import Enum

pg.init()

# setting the font_face and size
font = pg.font.SysFont("cambria", 25)

# setting the values for each of the direction using Enum
class Direction(Enum):
    RIGHT = 1
    LEFT = 2
    UP = 3
    DOWN = 4

# colors defined
neon = (204, 255, 102)
dark_green = (0, 51, 0)
black = (0, 0, 0)
red = (255, 0, 0)

# snake and its speed is set
snake_block = 10
speed = 15

Point = namedtuple('Point', 'x, y')


 