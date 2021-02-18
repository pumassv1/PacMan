from gameconstants import *



class GameManager:
    def __init__(self):
        self.board = [[None]*int(screen_width/box_size)]*int(screen_height/box_size)
        for y in range(len(self.board)): # making board frame
            if y == 0 or y == len(self.board) - 1:
                self.board[y] = ['X']*int(screen_width/box_size)
            for x in range(len(self.board)):
                if x == 0 or x == len(self.board)-1:
                    self.board[y][x] = 'X'

    def draw_board(self):
        blue_box = pygame.image.load('assets/box.png').convert_alpha()
        alpha_box = pygame.image.load('assets/alpha_box.png').convert_alpha()
        bg_surface = pygame.image.load('assets/background.png').convert_alpha()
        screen.blit(bg_surface, (0,0))
        for y in range(len(self.board)):
            for x in range(len(self.board)):
                if self.board[y][x] == 'X':
                    screen.blit(blue_box,blue_box.get_rect(topleft=(x*box_size,y*box_size)))
                else:
                    screen.blit(alpha_box,(y*box_size,x*box_size))

