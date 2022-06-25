import random
import pygame
from Settings import tile_size, horizontal_tiles, vertical_tiles
from Animals import WolfFemale, WolfMale, RabbitFemale, RabbitMale
from Field import GrassField, SandField


class Level:
    def __init__(self, surface, wolfMaleNumber, wolfFemalneNumber, rabbitMaleNumber, rabbitFemalneNumber):
        self.displaySurface = surface
        self.wolfMaleNum = wolfMaleNumber
        self.wolfFemaleNum = wolfFemalneNumber
        self.rabbitMaleNum = rabbitMaleNumber
        self.rabbitFemaleNum = rabbitFemalneNumber
        self.timer = 0

        self.wolfMaleSprites = self.createAnimals("wolfMale")
        self.wolfFemaleSprites = self.createAnimals("wolfFemale")
        self.rabbitMaleSprites = self.createAnimals("rabbitMale")
        self.rabbitFemaleSprites = self.createAnimals("rabbitFemale")

        self.grassFieldSprites = self.createFields()
        self.sandFieldSprites = pygame.sprite.Group()

    def drawGrid(self):
        for row in range(horizontal_tiles):
            for field in range(vertical_tiles):
                pygame.draw.rect(self.displaySurface, (174, 174, 173),
                                 pygame.Rect(tile_size * row, tile_size * field, tile_size, tile_size), 1)

    def createFields(self):
        sprites = pygame.sprite.Group()
        for x in range(horizontal_tiles):
            for y in range(vertical_tiles):
                field = GrassField((x * tile_size, y * tile_size), tile_size)
                sprites.add(field)
        return sprites

    def createAnimals(self, type):
        sprites = pygame.sprite.Group()

        if type == "wolfMale":
            i = self.wolfMaleNum
            animalsClass = WolfMale
        elif type == "wolfFemale":
            i = self.wolfFemaleNum
            animalsClass = WolfFemale
        elif type == "rabbitMale":
            i = self.rabbitMaleNum
            animalsClass = RabbitMale
        elif type == "rabbitFemale":
            i = self.rabbitFemaleNum
            animalsClass = RabbitFemale
        else:
            i = 0

        availablePositions = []

        for _ in range(i):
            for x in range(horizontal_tiles):
                for y in range(vertical_tiles):
                    availablePositions.append((x * tile_size, y * tile_size))
            chosenPosition = random.choice(availablePositions)
            availablePositions.remove(chosenPosition)
            sprites.add(animalsClass(chosenPosition, tile_size))
        return sprites

    def checkFields(self):
        for sand in self.sandFieldSprites.sprites():
            if sand.timer <= 0:
                position = sand.rect.topleft
                field = GrassField(position, tile_size)
                self.grassFieldSprites.add(field)
                sand.kill()

        for rabbit in self.rabbitMaleSprites.sprites() + self.rabbitFemaleSprites.sprites():
            if rabbit.inDanger == False:
                for grass in self.grassFieldSprites.sprites():
                    if rabbit.rect.colliderect(grass.rect):
                        position = grass.rect.topleft
                        field = SandField(position, tile_size)
                        self.sandFieldSprites.add(field)
                        grass.kill()
                        if rabbit.fat < 10:
                            rabbit.fat += 2
                        break

        for wolf in self.wolfFemaleSprites.sprites() + self.wolfMaleSprites.sprites():
            for rabbit in self.rabbitMaleSprites.sprites() + self.rabbitFemaleSprites.sprites():
                if wolf.rect.colliderect(rabbit.rect):
                    rabbit.kill()
                    if wolf.fat < 20:
                        wolf.fat += 5
                    break

    def hornyRabbit(self):
        for rabbitMale in self.rabbitMaleSprites.sprites():
            if rabbitMale.fat < 5:
                continue
            for rabbitFemale in self.rabbitFemaleSprites.sprites():
                if rabbitFemale.fat < 5:
                    continue
                if rabbitMale.rect.colliderect(rabbitFemale.rect):
                    positionF = rabbitFemale.rect.topleft
                    positionM = rabbitMale.rect.topleft
                    rabbitMale.fat -= 2
                    rabbitFemale.fat -= 2
                    newRabbit = RabbitMale(positionF, tile_size)
                    newRabbit.fat = 4
                    self.rabbitMaleSprites.add(newRabbit)
                    newRabbit2 = RabbitFemale(positionM, tile_size)
                    newRabbit2.fat = 4
                    self.rabbitFemaleSprites.add(newRabbit2)

                if (rabbitFemale.fat <= 0):
                    rabbitFemale.kill()
                if (rabbitMale.fat <= 0):
                    rabbitMale.kill()


    def hornyWolf(self):
        for wolfMale in self.wolfMaleSprites.sprites():
            for wolfFemale in self.wolfFemaleSprites.sprites():
                if wolfFemale.rect.colliderect(wolfMale.rect):
                    positionF = wolfFemale.rect.topleft
                    positionM = wolfMale.rect.topleft
                    wolfMale.fat -= 5
                    wolfFemale.fat -= 3
                    los = random.choice([True, False])
                    if los:
                        newWolf = WolfMale(positionF, tile_size)
                        newWolf.fat = 5
                        self.wolfMaleSprites.add(newWolf)
                    else:
                        newWolf = WolfFemale(positionM, tile_size)
                        newWolf.fat = 5
                        self.wolfFemaleSprites.add(newWolf)
                    if (wolfFemale.fat <= 0):
                        wolfFemale.kill()
                    if (wolfMale.fat <= 0):
                        wolfMale.kill()


    def run(self):
        if self.timer >= 120:
            self.checkFields()
            self.wolfMaleSprites.update(self.rabbitMaleSprites, self.rabbitFemaleSprites, self.wolfFemaleSprites,
                                        self.wolfFemaleSprites.sprites() + self.wolfMaleSprites.sprites())
            self.wolfFemaleSprites.update(self.rabbitMaleSprites, self.rabbitFemaleSprites,
                                          self.wolfFemaleSprites.sprites() + self.wolfMaleSprites.sprites())
            self.rabbitFemaleSprites.update(self.grassFieldSprites,
                                            self.wolfFemaleSprites.sprites() + self.wolfMaleSprites.sprites())
            self.rabbitMaleSprites.update(self.grassFieldSprites, self.rabbitFemaleSprites,
                                          self.wolfFemaleSprites.sprites() + self.wolfMaleSprites.sprites())
            self.sandFieldSprites.update()
            self.hornyRabbit()
            self.hornyWolf()

            self.timer = 0
        else:
            self.timer += 1

        self.grassFieldSprites.draw(self.displaySurface)
        self.sandFieldSprites.draw(self.displaySurface)

        self.rabbitMaleSprites.draw(self.displaySurface)
        self.rabbitFemaleSprites.draw(self.displaySurface)
        self.wolfMaleSprites.draw(self.displaySurface)
        self.wolfFemaleSprites.draw(self.displaySurface)

        self.drawGrid()












