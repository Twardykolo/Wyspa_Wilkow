import random
from Settings import tile_size, screen_size
import pygame
import numpy as np

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.rect = self.image.get_rect(topleft=pos)


class Animal(Tile):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.fat = 20
        self.lastPosition = None

    def update(self, availablePositions=[]):
        if len(availablePositions) == 0:
            availablePositions = self.randomStep()
        availablePositions = list(dict.fromkeys(availablePositions))
        step = None
        while step == self.lastPosition or step is None:
            step = random.choice(availablePositions)
            if (len(availablePositions) == 1):
                break
        self.move(step)
        self.lastPosition = step
        self.fat -= 1
        if self.fat <= 0:
            self.kill()

    def randomStep(self):
        availablePositions = []
        for posX in [tile_size, 0, -tile_size]:
            for posY in [tile_size, 0, -tile_size]:
                if self.checkMove(posX, posY):
                    availablePositions.append((posX, posY))
        return availablePositions

    def move(self, step):
        self.rect.topleft += pygame.math.Vector2(step[0], step[1])

    def checkMove(self, x, y):
        x += self.rect.x
        y += self.rect.y
        if x < screen_size[0] and x > 0 and y < screen_size[1] and y > 0:
            return True
        else:
            return False


class WolfFemale(Animal):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image = pygame.image.load("Textures/wolfF.png").convert_alpha()
        self.fat = 50

    def update(self, rabbitMaleSprites, rabbitFemaleSprites, wolfSprites, availablePositions=[]):
        if len(availablePositions) == 0:
            availablePositions = self.rabbitStep(rabbitMaleSprites.sprites() + rabbitFemaleSprites.sprites())
        safePositions = self.wolfRunAway(wolfSprites, availablePositions)
        availablePositions = safePositions.copy()
        super().update(availablePositions)

    def rabbitStep(self, rabbitSprites):
        xr = self.rect.x
        yr = self.rect.y

        availablePositions = []
        for rabbit in rabbitSprites:
            xg = rabbit.rect.x
            yg = rabbit.rect.y
            absx = xg - xr
            absy = yg - yr

            if (abs(absx) <= tile_size * 2 and abs(absy) <= tile_size * 2):
                absx = absx / 2 if abs(absx) > tile_size else absx
                absy = absy / 2 if abs(absy) > tile_size else absy
                availablePositions.append((absx, absy))
        return availablePositions

    def wolfRunAway(self, wolfSprites, availablePositions):
        xr = self.rect.x
        yr = self.rect.y
        kaczka = availablePositions.copy()
        for wolf in wolfSprites:
            xw = wolf.rect.x
            yw = wolf.rect.y
            absx = xw - xr
            absy = yw - yr
            if (abs(absx) <= tile_size and abs(absy) <= tile_size):
                if (absx, absy) in kaczka:
                    kaczka.remove((absx, absy))
        return kaczka


class WolfMale(WolfFemale):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image = pygame.image.load("Textures/wolf.png").convert_alpha()

    def update(self, rabbitMaleSprites, rabbitFemaleSprites, femaleWolfSprites, wolfSprites):
        availablePositions = []
        if self.fat > 7:
            availablePositions = self.wolfStep(femaleWolfSprites)
        super().update(rabbitMaleSprites, rabbitFemaleSprites, wolfSprites, availablePositions)

    def wolfStep(self, wolfFemaleSprites):
        xr = self.rect.x
        yr = self.rect.y

        availablePositions = []
        for wolfesse in wolfFemaleSprites.sprites():
            xg = wolfesse.rect.x
            yg = wolfesse.rect.y
            absx = xg - xr
            absy = yg - yr

            if (abs(absx) <= tile_size * 2 and abs(absy) <= tile_size * 2):
                absx = absx / 2 if abs(absx) > tile_size else absx
                absy = absy / 2 if abs(absy) > tile_size else absy
                availablePositions.append((absx, absy))
        return availablePositions


class RabbitFemale(Animal):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.inDanger = False
        self.fat = 10
        self.image = pygame.image.load("Textures/bunnyF.png").convert_alpha()

    def update(self, grassSprites, wolfSprites, availablePositions=[]):
        if len(availablePositions) == 0:
            availablePositions = self.grassStep(grassSprites)
        safePositions = self.wolfRunAway(wolfSprites, availablePositions)
        if len(safePositions) == len(availablePositions):
            self.inDanger = False
        availablePositions = safePositions.copy()
        if self.fat <= 3 and self.inDanger:
            availablePositions = []
            self.inDanger = False
        if len(availablePositions) != 0:
            super().update(availablePositions)
        else:
            self.fat -= 1

    def wolfRunAway(self, wolfSprites, availablePositions):
        xr = self.rect.x
        yr = self.rect.y
        kaczka = availablePositions.copy()
        for wolf in wolfSprites:
            xw = wolf.rect.x
            yw = wolf.rect.y
            absx = xw - xr
            absy = yw - yr
            if (abs(absx) <= tile_size and abs(absy) <= tile_size):
                self.inDanger = True
                if (absx, absy) in kaczka:
                    kaczka.remove((absx, absy))
        return kaczka

    def grassStep(self, grassSprites):
        xr = self.rect.x
        yr = self.rect.y

        availablePositions = []
        for grass in grassSprites.sprites():
            xg = grass.rect.x
            yg = grass.rect.y
            absx = xg - xr
            absy = yg - yr

            if (abs(absx) <= tile_size and abs(absy) <= tile_size):
                availablePositions.append((absx, absy))
        return availablePositions


class RabbitMale(RabbitFemale):
    def __init__(self, pos, size):
        super().__init__(pos, size)
        self.image = pygame.image.load("Textures/bunny.png").convert_alpha()

    def update(self, grassSprites, femaleRabbitSprites, wolfSprites):
        availablePositions = []
        if self.fat > 7:
            availablePositions = self.rabbitStep(femaleRabbitSprites)
        super().update(grassSprites, wolfSprites, availablePositions)

    def rabbitStep(self, femaleRabbitSprites):
        xr = self.rect.x
        yr = self.rect.y

        availablePositions = []
        for rabbit in femaleRabbitSprites.sprites():
            xg = rabbit.rect.x
            yg = rabbit.rect.y
            absx = xg - xr
            absy = yg - yr

            if (abs(absx) <= tile_size * 2 and abs(absy) <= tile_size * 2):
                absx = absx / 2 if abs(absx) > tile_size else absx
                absy = absy / 2 if abs(absy) > tile_size else absy
                availablePositions.append((absx, absy))
        return availablePositions
