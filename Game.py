import pygame
import Map

pygame.init()
# Set the width and height of the output window, in pixels
WIDTH = 400
HEIGHT = 400
RED = (255, 0, 0)

# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
tile = pygame.Rect((0,0), (20, 20))

pygame.draw.rect(screen, GREEN, tile,1)

running = True
while running:
    # events
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False

    Map.draw(pygame,screen)
    
    pygame.display.flip()


pygame.quit()