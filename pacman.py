import pygame
from gamemanager import GameManager
from gameconstants import *


class PacMan:
    def __init__(self):
        self.x = 31
        self.y = 15
        self.live = 3
        self.sprite = pygame.image.load('assets/pacman.png').convert_alpha()

    def move_up(self):
        if self.y < 31 and self.y > 0:
            self.y -= 1

    def move_down(self):
        if self.y < 31 and self.y > 0:
            self.y += 1

    def move_right(self):
        if self.x < 31 and self.x > 0:
            self.x += 1

    def move_left(self):
        if self.x < 31 and self.x > 0:
            self.x -= 1

    def draw_sprite(self):
        screen.blit(self.sprite, self.sprite.get_rect(topleft=(self.x*box_size, self.y*box_size)))



gamemanager = GameManager()
pacman = PacMan()


gamemanager.draw_board()

pacman.draw_sprite()

pygame.display.update()
input()
