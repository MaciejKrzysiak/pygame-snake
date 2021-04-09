from constants import (
    SCREEN_WIDTH,
    SCREEN_HEIGHT,
    GRID_SIZE,
    UP,
    DOWN,
    LEFT,
    RIGHT,
    WHITE,
    GREEN,
)
import random
import pygame
import sys


class Critter:
    def __init__(self, id):
        self.id = id
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])
        self.color = GREEN

    def get_head_position(self):
        return self.positions[0]

    def turn(self, point):
        if self.length > 1 and (point[0] * -1, point[1] * -1) == self.direction:
            return
        else:
            self.direction = point

    def draw(self, surface):
        for elem in self.positions:
            r = pygame.Rect((elem[0], elem[1]), (GRID_SIZE, GRID_SIZE))
            pygame.draw.rect(surface, self.color, r)
            pygame.draw.rect(surface, WHITE, r, 1)

    def reset(self):
        self.length = 1
        self.positions = [(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)]
        self.direction = random.choice([UP, DOWN, LEFT, RIGHT])

    def move(self):
        head = self.get_head_position()
        x, y = self.direction
        new_pos = (
            (head[0] + x * GRID_SIZE) % SCREEN_WIDTH,
            (head[1] + y * GRID_SIZE) % SCREEN_HEIGHT,
        )
        if (len(self.positions) > 2) and (new_pos in self.positions[2:]):
            self.reset()
            return -1
        else:
            self.positions.insert(0, new_pos)
            if len(self.positions) > self.length:
                self.positions.pop()
            return 0

    def user_input(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.turn(UP)
                if event.key == pygame.K_DOWN:
                    self.turn(DOWN)
                if event.key == pygame.K_LEFT:
                    self.turn(LEFT)
                if event.key == pygame.K_RIGHT:
                    self.turn(RIGHT)
