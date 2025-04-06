from .constants import SQUARE_SIZE, CROWN
import pygame


class Piece:
    def __init__(self, row, col, color):
        self.row = row
        self.col = col
        self.color = color
        self.king = False
        self.x = 0
        self.y = 0
        self.calc_position()

    def draw_piece(self, win):
        radius = SQUARE_SIZE//2 - 15
        pygame.draw.circle(win, self.color, (self.x, self.y), radius)
        if self.king:
            win.blit(CROWN, (self.x - CROWN.get_width() //
                     2, self.y - CROWN.get_height()//2))

    def make_king(self):
        self.king = True

    def move_piece(self, row, col):
        self.row = row
        self.col = col
        self.calc_position()

    def calc_position(self):
        self.x = SQUARE_SIZE * self.col + SQUARE_SIZE // 2
        self.y = SQUARE_SIZE * self.row + SQUARE_SIZE // 2
