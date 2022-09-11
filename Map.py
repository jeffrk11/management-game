import pygame

map_size = 15; # W x H
tiles = []
GREEN = (50,255,50)

def set_tiles():
    for t in range(map_size*map_size):
        tiles.append(pygame.Rect((0,0), (20, 20)))

def draw(pygame,screen):
    # draw map
    for i in range(map_size):
        for j in range(map_size):
            pygame.draw.rect(screen, GREEN, pygame.Rect((i*20, j*20), (20, 20)),1)

def tile_hover():
    pygame.get