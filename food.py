from constants import GRID_SIZE, GRID_WIDTH, GRID_HEIGHT, WHITE
import random
import pygame


class Food:
    def __init__(self, id):
        self.id = id
        self.position = (0, 0)
        self.color = WHITE
        self.randomize_position()
        self.randomize_color()

    def draw(self, surface):
        r = pygame.Rect((self.position[0], self.position[1]), (GRID_SIZE, GRID_SIZE))
        pygame.draw.rect(surface, self.color, r)
        pygame.draw.rect(surface, WHITE, r, 1)

    def reset(self):
        pass

    def randomize_position(self):
        self.position = (
            random.randint(0, GRID_WIDTH - 1) * GRID_SIZE,
            random.randint(0, GRID_HEIGHT - 1) * GRID_SIZE,
        )

    def randomize_color(self):
        self.color = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255),
        )
