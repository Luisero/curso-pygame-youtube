import pygame
import sys 


pygame.init()

SCREEN_HEIGHT = 400
SCREEN_WIDTH = 700
screen = pygame.display.set_mode((SCREEN_WIDTH,SCREEN_HEIGHT))

screen_color = (20,140,252)
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.fill(screen_color)

    pygame.display.update()
