from gamemanager import GameManager
from gameconstants import *
import sys


class PacMan:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.live = 3
        self.sprite = pygame.image.load('assets/pacman.png').convert_alpha()

    def move_up(self):
        if self.y <= 31 and self.y > 0:
            self.y -= 1

    def move_down(self):
        if self.y < 31 and self.y >= 0:
            self.y += 1

    def move_right(self):
        if self.x < 31 and self.x >= 0:
            self.x += 1

    def move_left(self):
        if self.x <= 31 and self.x > 0:
            self.x -= 1

    def draw_sprite(self):
        screen.blit(self.sprite, self.sprite.get_rect(topleft=(self.x*box_size, self.y*box_size)))



gamemanager = GameManager()
pacman = PacMan()


while True:
    gamemanager.draw_board()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                pacman.move_up()
            if event.key == pygame.K_s:
                pacman.move_down()
            if event.key == pygame.K_a:
                pacman.move_left()
            if event.key == pygame.K_d:
                pacman.move_right()


    pacman.draw_sprite()
    pygame.display.update()

