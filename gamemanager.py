import pygame

pygame.init()

### GAME CONSTANTS ###

screen_width = 1024
screen_height = 1024
box_size = 32

######################

screen = pygame.display.set_mode((screen_width,screen_height)) # 200x200 blocks where each block is 4x4

class GameManager:
    def __init__(self):
        self.board = [[None]*int(screen_width/box_size)]*int(screen_height/box_size)
        print(self.board)
        for y in range(len(self.board)): # making board frame
            if y == 0 or y == len(self.board) - 1:
                self.board[y] = ['X']*int(screen_width/box_size)
            for x in range(len(self.board)):
                if x == 0 or x == len(self.board)-1:
                    self.board[y][x] = 'X'

        print(self.board)

    def draw_board(self):
        blue_box = pygame.image.load('assets/box.png').convert()
        alpha_box = pygame.image.load('assets/alpha_box.png').convert_alpha()
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                if self.board[y][x] == 'X':
                    screen.blit(blue_box,blue_box.get_rect(topleft=(x*box_size,y*box_size)))
                else:
                    screen.blit(alpha_box,(y*box_size,x*box_size))



x = GameManager()
x.draw_board()
pygame.display.update()
input()
