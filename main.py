from snack import Snake
from food import Food
from premiumfood import PremiumFood
from GameInit import SCREEN_SIZE, drawGrid
import pygame


class Game:
    def __init__(self):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)
        self.surface = pygame.Surface(self.screen.get_size()).convert()
        drawGrid(self.surface)

        self.snake = Snake()
        self.food = Food()
        self.big_food = PremiumFood()

        self.font = pygame.font.SysFont("monospace", 16)
        self.score = 0
        self.big_score = 0
        self.running = True

    def handle_food_collision(self):
        if self.snake.getHeadPosition() == self.food.position:
            self.snake.length += 1
            self.score += 1
            self.big_score += self.score
            self.food.randomize_position()

    def handle_premium_food(self):
        if self.score % 5 == 0:
            self.big_food.draw(self.surface)
            if self.snake.getHeadPosition() == self.big_food.position:
                self.snake.length = max(1, self.snake.length - 3)
                self.score += 5
                self.big_food.randomize_position()

    def draw_ui(self):
        drawGrid(self.surface)
        self.snake.draw(self.surface)
        self.food.draw(self.surface)
        self.screen.blit(self.surface, (0, 0))

        score_text = self.font.render(f"Score {self.score}", True, (0, 0, 0))
        self.screen.blit(score_text, (5, 10))
        pygame.display.update()

    def run(self):
        while self.running:
            self.clock.tick(10)
            self.snake.handleKeys()
            self.snake.move()

            self.handle_food_collision()
            self.handle_premium_food()

            if self.big_score > 10:
               import sys
               exit()

            self.draw_ui()


if __name__ == "__main__":
    game = Game()
    game.run()
