import pygame
import sys
from Level import Level
from Settings import screen_size, tile_size

pygame.init()
window = pygame.display.set_mode(screen_size)
pygame.display.set_caption("Wyspa wilków")
clock = pygame.time.Clock()

level = Level(window, 7, 7, 15, 15)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill('grey')

    level.run()

    pygame.display.update()
    clock.tick(60)
