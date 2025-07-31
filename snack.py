from game import *

class Snake:
    def __init__(self)->None:
        self.length =1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP,DOWN, LEFT, RIGHT])
        self.color =(17,24,47)

    def getHeadPosition(self):
        return self.positions[0]

    def turn(self, point):
        if self.length >1 and (point[0]*-1, point[1]*-1) == self.direction:
            return
        else: self.direction = point

    def move(self):
        cur = self.getHeadPosition()
        x,y = self.direction
        new = (((cur[0]+(x*GRIDSIZE))%SCREEN_WIDTH), (cur[1]+(y*GRIDSIZE))%SCREEN_HEIGHT)
        if len(self.positions) > 2 and new in self.positions[2:]:
            self.reset()
        else:
            self.positions.insert(0, new)
            if len(self.positions)> self.length:
                self.positions.pop()

    def reset(self):
        self.length =1
        self.positions = [((SCREEN_WIDTH/2), (SCREEN_HEIGHT/2))]
        self.direction = random.choice([UP,DOWN, LEFT, RIGHT])
       
    def draw(self, surface):
        for p in self.positions:
            r = pygame.Rect((p[0],p[1]), (GRIDSIZE, GRIDSIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, (93,216, 228), r, 1)

    def handleKeys(self)->None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key==pygame.K_UP:
                    self.turn(UP)
                if event.key==pygame.K_DOWN:
                    self.turn(DOWN)
                if event.key==pygame.K_LEFT:
                    self.turn(LEFT)
                if event.key==pygame.K_RIGHT:
                    self.turn(RIGHT)

