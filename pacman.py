from gamemanager import GameManager
from gameconstants import *
import sys


class PacMan:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.live = 3
        self.sprite = pygame.image.load('assets/pacman.png').convert_alpha()
        self.speed = 1

    def move_up(self):
        if self.y <= 31 and self.y > 0:
            self.y -= self.speed

    def move_down(self):
        if self.y < 31 and self.y >= 0:
            self.y += self.speed

    def move_right(self):
        if self.x < 31 and self.x >= 0:
            self.x += self.speed

    def move_left(self):
        if self.x <= 31 and self.x > 0:
            self.x -= self.speed

    def draw_sprite(self):
        screen.blit(self.sprite, self.sprite.get_rect(topleft=(self.x*box_size, self.y*box_size)))



gamemanager = GameManager()
pacman = PacMan()


while True:
    gamemanager.draw_board()
    pressed_keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    if pressed_keys[pygame.K_w] and pressed_keys[pygame.K_d] != True:
        pacman.move_up()
    if pressed_keys[pygame.K_s] and pressed_keys[pygame.K_d] != True:
        pacman.move_down()
    if pressed_keys[pygame.K_a] and pressed_keys[pygame.K_s] != True and pressed_keys[pygame.K_w] != True:
        pacman.move_left()
    if pressed_keys[pygame.K_d]:
        pacman.move_right()

    clock.tick(15)

    pacman.draw_sprite()
    pygame.display.update()

