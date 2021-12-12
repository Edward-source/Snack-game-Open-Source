from snack import *
from food import *
from premiumfood import *
from GameInit import *

def GameMain():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface=surface.convert()
    drawGrid(surface)

    snack = Snake()
    food = Food()
    bigFood = PremiumFood()

    myfrond = pygame.font.SysFont("monospace", 16)
    score = 0
    bigScore = 0

    running = True
    while running:
        clock.tick(10)
        snack.handle_keys()
        drawGrid(surface)
        # handle ebents
        snack.move()
        if snack.get_head_position() == food.position:
            snack.length +=1
            score +=1
            bigScore = bigScore+score
            food.randomize_position()

        if score %5 == 0:
            bigFood.draw(surface)
            if snack.get_head_position() == bigFood.position:
              snack.length-=3
              score+=29
              bigFood.randomize_position()
        if bigScore > 40:
            print(" Game killer !!!......")
                   
         
        snack.draw(surface)
        food.draw(surface)
       
        screen.blit(surface, (0,0))
        text = myfrond.render(f"Score {score}", 1, (0,0,0))
        screen.blit(text, (5,10))
        pygame.display.update()

GameMain()