import pygame
import sys


pygame.init()

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 800

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))



while True:
    screen.fill('black')

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    x = 30
    y = 10
    width = 100
    height = 50

    pygame.draw.rect(screen, 'red',(x,y, width, height))


    x_circle = 300
    y_circle = 200
    radius = 100

    pygame.draw.circle(screen, 'yellow',(x_circle,y_circle), radius )


    pygame.draw.circle(screen,'cyan', (x_circle,y_circle), 10)

    x1 = 300
    y1 = 200

    x2 = 600
    y2 = 0

    pygame.draw.line(screen, 'purple', (x1,y1),(x2,y2),10)


    rect = pygame.Rect(70,60, 200,100)

    pygame.draw.rect(screen, 'green',rect)

    pygame.display.update()