
import pygame
import random

pygame.init()
pygame.font.init()
screenSizeX = 1000 # screen width
screenSizeY = 700 # screen height
win = pygame.display.set_mode((screenSizeX, screenSizeY)) # Display
background = pygame.image.load('background.png')
background2 = pygame.image.load('Google.png')
myfont = pygame.font.SysFont('Comic Sans MS', 30) # Font style and size
myfont2 = pygame.font.SysFont('Comic Sans MS', 20) # Same
characterR = pygame.image.load('Space-ManR.png') # character looking right
characterL = pygame.image.load('Space-ManL.png') # character looking left
drawCharacter = pygame.image.load('Space-ManR.png') # default character looking
enemy1 = pygame.image.load('enemy.png') # enemy image
width = 50 # char width
height = 50 # char height
x = 50 # char x
y = screenSizeY - height # char y
Xvel = 10 # char x vel
Yvel = 0 # char y vel
direction = 1 # char dir
gravity = 0 # char gravity
run = True # main loop on/off
health = 3 # char health
bulletsOn = 0 # bullets onscreen
bulletX = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # bullet x pos
bulletY = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # bullet y pos
bulletDirs = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0] # bullet dirs
startTime = 0 # start bullet timer?
shoot = 1 # allowing to fire?
time = 0 # time between fire

while True:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    win.fill((0, 0, 0))

    textsurface = myfont.render('Press S to Start', False, (50, 255, 255))
    text2 = myfont.render('Welcome to Cyber Space', False, (50, 255, 255))
    text3 = myfont2.render('Created by Luke and Alan Gonsalves', False, (50, 255, 255))
    win.blit(background, (0, 0))
    win.blit(textsurface, (30,30))
    win.blit(text2, (300, 300))
    win.blit(text3, (310, 400))
    keys = pygame.key.get_pressed()
    if keys[pygame.K_s]:
        break
    
    pygame.display.update()
while run:
    pygame.time.delay(50)
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if startTime == 1:
        time += 1
        shoot = 0
        if time == 5:
            shoot = 1
            startTime = 0

    keys = pygame.key.get_pressed()

    if y < screenSizeY - (height + 3):
        if Yvel < 7:
            Yvel += .35
        else:
            Yvel = 7
        if gravity < 7:
            gravity += .35
        else:
            gravity = 7
    else:
        Yvel = 0
        gravity = 0

    if keys[pygame.K_UP]:
        if Yvel > -4:
            Yvel -= 2
        else:
            Yvel = -4

        if gravity < 3:
            gravity += 1.5
        else:
            gravity = 3

    if keys[pygame.K_RIGHT]:
        if x < screenSizeX - width:
            x += Xvel
        drawCharacter = characterR
        direction = 1

    if keys[pygame.K_LEFT]:
        if x > 0:
            x -= Xvel
        drawCharacter = characterL
        direction = 3

    if keys[pygame.K_z]:
        if shoot == 1:
            if bulletsOn != 12:
                startTime = 1
                bulletY[bulletsOn] = (y + (height / 2 + 10))
                if direction == 1:
                    bulletX[bulletsOn] = x + width
                else:
                    bulletX[bulletsOn] = x - 10
                bulletDirs[bulletsOn] = direction
                bulletsOn += 1
                time = 0

    b = 0
    while b < gravity:
        y += (Yvel)
        b += 1
        if y > screenSizeY - (height + 5):
            break
    win.fill((0, 0, 0))
    win.blit(background2, (0, 0))
    win.blit(drawCharacter, (x, y))

    if bulletsOn > 0:
        c = 0
        while c < bulletsOn:
            pygame.draw.rect(win, (random.randint(50, 200), random.randint(50, 200), random.randint(50, 200) ), (bulletX[c], bulletY[c], 50, 3))
            if bulletDirs[c] == 1:
                bulletX[c] += 60
                if  bulletX[c] > screenSizeX:
                    del bulletX[c]
                    del bulletY[c]
                    del bulletDirs[c]
                    bulletX.append(0)
                    bulletY.append(0)
                    bulletDirs.append(0)
                    bulletsOn -= 1
            elif bulletDirs[c] == 3:
                bulletX[c] -= 60
                if  bulletX[c] < 0:
                    del bulletX[c]
                    del bulletY[c]
                    del bulletDirs[c]
                    bulletX.append(0)
                    bulletY.append(0)
                    bulletDirs.append(0)
                    bulletsOn -= 1
            c += 1
   
    pygame.display.update()








pygame.quit()                      

