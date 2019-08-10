"""The rendering engine represents on screen the evolution of the physics system.

Todo:

"""
import sys
import pygame
pygame.init()

size = width, height = 320, 240
speed = [2, 2]
black = 0, 0, 0
white = 255, 255, 255

screen = pygame.display.set_mode(size)
rect = pygame.draw.rect(screen, white, [0, 0, 100, 100], 50)


while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    screen.fill(black)
    screen.blit(rect, (0, 0))


class Rendering():
    pass