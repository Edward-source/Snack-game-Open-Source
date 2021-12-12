
from snack import *
from food import *
from premiumfood import *
from game import *
from pygame import *


def drawGrid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            if (x+y) % 2==0:
                r=pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                pygame.draw.rect(surface, (93,216,228), r)
            else:
                 rr=pygame.Rect((x*GRIDSIZE, y*GRIDSIZE), (GRIDSIZE, GRIDSIZE))
                 pygame.draw.rect(surface, (93,216,205), rr)



