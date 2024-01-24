import pygame
import random

# initialize pygame
pygame.init()

# title & icon
pygame.display.set_caption("Cat Invaders")
icon = pygame.image.load('litter_icon.png')
pygame.display.set_icon(icon)

# player
playerImg = pygame.image.load('shovel.png')
playerX = 350
playerY = 680
playerX_change = 0


# enemy
enemyImg = pygame.image.load('catpoo.png')
enemyX = random.randint(0, 800)
enemyY = random.randint(50, 150)
enemyX_change = 0
enemyY_change = 20


# rocks
rocksImg = pygame.image.load('litterrocks.png')
rocksX = 0
rocksY = 480
rocksX_change = 0
rocksY_change = 10
rock_state = "ready"


# background
background = pygame.image.load('living_room.jpg')


def player(x, y):
    screen.blit(playerImg, (x, y))    # blit just means to draw


def enemy(x, y):
    screen.blit(enemyImg, (x, y))


def shoot_rock(x, y):
    global rock_state
    rock_state = "shoot"
    screen.blit(rocksImg, (x+16, y+10))


# render screen
screen = pygame.display.set_mode((800, 800))
# problem, screen renders but goes away almost instantly. fix:
running = True
while running:
    # screen RGB fill
    screen.fill((255, 253, 208))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False              # running is set to False if we detect pygame.QUIT after staying on True
        if event.type == pygame.KEYDOWN:   # KEYDOWN meanas key is pressed
            if event.key == pygame.K_LEFT:
                playerX_change = -4
            if event.key == pygame.K_RIGHT:
                playerX_change = 4
            if event.key == pygame.K_SPACE:
                shoot_rock(playerX, rocksY)

        if event.type == pygame.KEYUP:   # KEYUP means the keystroke is released
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                playerX_change = 0
    # player movement
    playerX += playerX_change
    if playerX <= 0:
        playerX = 0
    elif playerX >= 800:
        playerX = 800
    # enemy movement
    enemyX += enemyX_change
    enemyY += 0.5
    player(playerX, playerY)
    enemy(enemyX, enemyY)
    # rock movement
    if rock_state is "shoot":
        shoot_rock(playerX, rocksY)
        rocksY -= rocksY_change
    pygame.display.update()



