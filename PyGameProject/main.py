import pygame

# initialize pygame
pygame.init()

# title & icon
pygame.display.set_caption("Cat Invaders")
icon = pygame.image.load('litter_icon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('shovel.png')
playerX = 370
playerY = 480
playerX_change = 0

enemyImg = pygame.image.load('catpoo.png')
enemyX = 370
enemyY = 50
enemyX_change = 0


def player(x, y):
    screen.blit(playerImg, (x, y))    # blit just means to draw


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


# render screen
screen = pygame.display.set_mode((800, 600))
# problem, screen renders but goes away almost instantly. fix:
running = True
while running:
    # screen RGB fill
    screen.fill((255, 253, 208))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False              # running is set to False if we detect pygame.QUIT after staying on True
        if event.type == pygame.KEYDOWN:   # KEYDOWN meanas key is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
        if event.type == pygame.KEYUP:   # KEYUP means the keystroke is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 736:
        playerX = 736
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    pygame.display.update()


