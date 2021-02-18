import pygame

### GAME CONSTANTS ###

screen_width = 1024
screen_height = 1024
box_size = 32

pygame.init()

screen = pygame.display.set_mode((screen_width,screen_height)) # 200x200 blocks where each block is 4x4

clock = pygame.time.Clock()