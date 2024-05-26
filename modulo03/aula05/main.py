import pygame
import sys
from random import randint

pygame.init()

SCREEN_WIDTH = 700
SCREEN_HEIGHT = 400

screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

rect_color = (255,255,0)

x,y= 30,40

while True:
    screen.fill((2,102,135))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        ''' if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                print('Apertou space')

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_SPACE:
                print('Soltou space')
        '''

        keys = pygame.key.get_pressed()

        if keys[pygame.K_SPACE]:
            r = randint(0,255)
            g = randint(0,255)
            b = randint(0,255)
            rect_color = (r,g,b)

        if keys[pygame.K_a]:
            x = x -10
        if keys[pygame.K_d]:
            x = x +10

        if keys[pygame.K_w]:
            y = y -10
        
        if keys[pygame.K_s]:
            y = y +10   

    rect = pygame.Rect(x,y, 100,50)
    pygame.draw.rect(screen, rect_color, rect)
    
    pygame.display.update()