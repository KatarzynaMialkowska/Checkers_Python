import pygame
from .constants import PIECES_G1, PIECES_G2, ALLOWED_MOVES, SQUARE_SIZE
from checkers.board import Board
from .constants import WOOD_HOR, WOOD_WER, CORNER, TYPE, SCREEN_HEIGHT, SCREEN_WIDTH

class Game:
    def __init__(self, screen):
        self.selected = None
        self.board = Board()
        self.valid_moves = {}
        self.turn = PIECES_G1
        self.screen = screen

    def update(self):
        self.board.draw_board(self.screen)
        self.draw_valid_moves(self.valid_moves)
        pygame.display.update()
        
    def select(self, row, col):
        if self.selected:
            result = self.move(row, col)
            if not result:
                self.selected = None
                self.select(row, col)

        piece = self.board.get_square(row, col)
        if piece != 0 and piece.color == self.turn:
            self.selected = piece
            self.valid_moves = self.board.get_valid_moves(piece)
            return True

        return False

    def move(self, row, col):
        piece = self.board.get_square(row, col)
        if self.selected and piece == 0 and (row, col) in self.valid_moves:
            self.board.move(self.selected, row, col)
            skipped = self.valid_moves[(row, col)]
            if skipped:
                self.board.remove_skipped_piece(skipped)
            self.change_turn() 
            self.board.sound_effect()
        else:
            return False
       
        return True

    def draw_valid_moves(self, moves):
        for move in moves:
            row, col = move
            pygame.draw.circle(self.screen, ALLOWED_MOVES, (col * SQUARE_SIZE +
                               SQUARE_SIZE//2, row * SQUARE_SIZE + SQUARE_SIZE//2), 15)

    def change_turn(self):
        self.valid_moves = {}
       
        if self.turn == PIECES_G1:
            self.turn = PIECES_G2
        else:
            self.turn = PIECES_G1
            
    def get_board(self):
        return self.board

    def ai_move(self, board):
        self.board = board
        self.change_turn()
        self.board.sound_effect()
        
    def winner(self):
        return self.board.is_winner()