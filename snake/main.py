import pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 500))
clock = pygame.time.Clock()
background = pygame.image.load('grass.png')
background = pygame.transform.scale(background, (1280, 720))
running = True

while running:
    screen.fill((255, 253, 208))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    pygame.display.update()
