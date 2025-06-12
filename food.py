from game import *
import random

class Food:
    def __init__(self):
        self.position = (0, 0)
        self.color = (223, 163, 49)
        self.randomize_position()

    def randomize_position(self):
      self.position = (
        int(random.randint(0, GRID_WIDTH - 1) * GRIDSIZE),
        int(random.randint(0, GRID_HEIGHT - 1) * GRIDSIZE)
        )

    def draw(self, surface):
        r = pygame.Rect(self.position, (GRIDSIZE, GRIDSIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, (93, 216, 228), r, 1)
