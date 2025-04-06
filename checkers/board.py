import pygame
from .constants import FIELD_DARK, ROWS, PIECES_G1, SQUARE_SIZE, COLS, PIECES_G2, FIELD_BRIGHT
from .piece import Piece
from .constants import WOOD_HOR, WOOD_WER, CORNER, TYPE, SCREEN_HEIGHT, SCREEN_WIDTH
from pygame import mixer

class Board:
    def __init__(self):
        self.board = []
        self.G2_pieces_count = self.G1_pieces_count = 12
        self.G2_kings_count = self.G1_kings_count = 0
        self.init_board()

    def init_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                if col % 2 == ((row + 1) % 2):
                    if row < 3:
                        self.board[row].append(Piece(row, col, PIECES_G2))
                    elif row > 4:
                        self.board[row].append(Piece(row, col, PIECES_G1))
                    else:
                        self.board[row].append(0)
                else:
                    self.board[row].append(0)

    def draw_board(self, screen):
        FONT = pygame.font.Font(TYPE, 32)
        screen.fill(FIELD_DARK)
        screen.blit(WOOD_HOR, (800, 0))
        screen.blit(WOOD_WER, (0, 800))
        screen.blit(CORNER, (800, 800))
        
        
        for col in range(COLS):
            num = FONT.render(str(col+1), True, (255,255,255))
            screen.blit(num, (SCREEN_WIDTH-(SQUARE_SIZE/2)-8, SQUARE_SIZE * col + (SQUARE_SIZE/2 - 16)))

        for col in range(COLS):
            s = chr((65+col))
            num = FONT.render(s, True, (255,255,255))
            screen.blit(num, (SQUARE_SIZE * col + (SQUARE_SIZE/2 - 16), SCREEN_HEIGHT-(SQUARE_SIZE/2)-8))
        
        for row in range(ROWS):
            for col in range(row % 2, COLS, 2):
                pygame.draw.rect(screen, FIELD_BRIGHT, (row*SQUARE_SIZE,
                                 col * SQUARE_SIZE, SQUARE_SIZE, SQUARE_SIZE))
        for row in range(ROWS):
            for col in range(COLS):
                piece = self.board[row][col]
                if piece != 0:
                    piece.draw_piece(screen)
                    
        if self.is_winner():
            win = FONT.render("WINNER IS: " + self.is_winner(), True, (0,255,0))
            screen.blit(win, (100,100))
                        
    def score(self):
        return self.G1_pieces_count - self.G2_pieces_count + (self.G1_kings_count * 2- self.G2_kings_count * 2)

    def get_all_pieces(self, color):
        pieces = []
        for row in self.board:
            for piece in row:
                if piece != 0 and piece.color == color:
                    pieces.append(piece)
        return pieces

    def sound_effect(self):
        sound = mixer.Sound('assets/sound_move.mp3')
        mixer.Channel(1).play(sound)
        mixer.Channel(1).set_volume(0.05)

    def move(self, piece, row, col):
        temp = self.board[piece.row][piece.col]
        self.board[piece.row][piece.col] = self.board[row][col]
        self.board[row][col] = temp

        piece.move_piece(row, col)

        if row == ROWS - 1 or row == 0:
            piece.make_king()
            if piece.color == PIECES_G2:
                self.G1_kings_count += 1
            else:
                self.G2_kings_count += 1


    def get_square(self, row, col):
        return self.board[row][col]

    def remove_skipped_piece(self, pieces):
        for piece in pieces:
            self.board[piece.row][piece.col] = 0
            if piece != 0:
                if piece.color != PIECES_G1:
                    self.G1_pieces_count -= 1
                else:
                    self.G2_pieces_count -= 1

    def is_winner(self):
        if self.G2_pieces_count <= 0:
            return "PIECES_G2"
        elif self.G1_pieces_count <= 0:
            return "PIECES_G1"

        return None

    def get_valid_moves(self, piece):
        moves = {}
        left = piece.col - 1
        right = piece.col + 1
        row = piece.row

        if piece.color == PIECES_G1 or piece.king:
            moves.update(self.diagonal_traverse_left(
                row - 1, max(row-3, -1), -1, piece.color, left))
            moves.update(self.diagonal_traverse_right(
                row - 1, max(row-3, -1), -1, piece.color, right))
        if piece.color == PIECES_G2 or piece.king:
            moves.update(self.diagonal_traverse_left(
                row + 1, min(row+3, ROWS), 1, piece.color, left))
            moves.update(self.diagonal_traverse_right(
                row + 1, min(row+3, ROWS), 1, piece.color, right))

        return moves

    def diagonal_traverse_left(self, start, stop, step, color, left, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if left < 0:
                break

            current = self.board[r][left]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, left)] = last + skipped
                else:
                    moves[(r, left)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.diagonal_traverse_left(
                        r+step, row, step, color, left-1, skipped=last))
                    moves.update(self.diagonal_traverse_right(
                        r+step, row, step, color, left+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            left -= 1

        return moves

    def diagonal_traverse_right(self, start, stop, step, color, right, skipped=[]):
        moves = {}
        last = []
        for r in range(start, stop, step):
            if right >= COLS:
                break

            current = self.board[r][right]
            if current == 0:
                if skipped and not last:
                    break
                elif skipped:
                    moves[(r, right)] = last + skipped
                else:
                    moves[(r, right)] = last

                if last:
                    if step == -1:
                        row = max(r-3, 0)
                    else:
                        row = min(r+3, ROWS)
                    moves.update(self.diagonal_traverse_left(
                        r+step, row, step, color, right-1, skipped=last))
                    moves.update(self.diagonal_traverse_right(
                        r+step, row, step, color, right+1, skipped=last))
                break
            elif current.color == color:
                break
            else:
                last = [current]

            right += 1

        return moves
