import pygame
from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_SIZE,
    FRAME_RATE,
    GRID_WIDTH,
    GRID_HEIGHT,
    WHITE,
)
from critter import Critter
from food import Food


def draw_grid(surface):
    for y in range(0, int(GRID_HEIGHT)):
        for x in range(0, int(GRID_WIDTH)):
            r = pygame.Rect(x * GRID_SIZE, y * GRID_SIZE, GRID_SIZE, GRID_SIZE)
            pygame.draw.rect(surface, WHITE, r)


def main():
    pygame.init()
    clock = pygame.time.Clock()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), 0, 32)

    surface = pygame.Surface(screen.get_size())
    surface = surface.convert()

    snake = Critter(0)
    food = Food(0)
    draw_grid(surface)

    myfont = pygame.font.SysFont("monospace", 16)
    score = 0

    while True:
        clock.tick(FRAME_RATE)
        snake.user_input()
        draw_grid(surface)
        result = snake.move()
        if result == -1:
            score = 0
        if snake.get_head_position() == food.position:
            snake.length += 1
            score += 1
            food.randomize_position()
            food.randomize_color()
        snake.draw(surface)
        food.draw(surface)
        screen.blit(surface, (0, 0))
        text = myfont.render(f"Score: {score}", 1, (0, 0, 0))
        screen.blit(text, (5, 10))
        pygame.display.update()


main()
