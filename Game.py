import pygame

pygame.init()
# Set the width and height of the output window, in pixels
WIDTH = 300
HEIGHT = 300
RED = (255, 0, 0)
GREEN = (50,255,50)
# Set up the drawing window
screen = pygame.display.set_mode([WIDTH, HEIGHT])
tile = pygame.Rect((0,0), (20, 20))

map_size = 20; # W x H

running = True
while running:
    # events
    for event in pygame.event.get():
        print(event)
        if event.type == pygame.QUIT:
            running = False
    #draw map
    for i in range(map_size):
        for j in range(map_size):
            pygame.draw.rect(screen, GREEN, pygame.Rect((i*20, j*20), (20, 20)),1)
    
    pygame.display.flip()


pygame.quit()