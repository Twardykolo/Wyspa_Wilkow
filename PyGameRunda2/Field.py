import random
import pygame
from Animals import Tile


class GrassField(Tile):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image = pygame.image.load("Textures/grass.png").convert_alpha()


class SandField(Tile):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image = pygame.image.load("Textures/sand.png").convert_alpha()
        self.timer = random.randint(4, 10)

    def update(self):
        if self.timer:
            self.timer = self.timer - 1
