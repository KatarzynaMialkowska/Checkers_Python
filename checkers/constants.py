import pygame

FPS = 60

# BOARD
SCREEN_WIDTH, SCREEN_HEIGHT = 900, 900
WIDTH, HEIGHT = 800, 800
ROWS, COLS = 8, 8
SQUARE_SIZE = WIDTH//COLS

# COLORS
PIECES_G1 = (240, 238, 220)
PIECES_G2 = (0, 0, 0)
FIELD_BRIGHT = (205, 198, 151)
FIELD_DARK = (87, 67, 50)

ALLOWED_MOVES = (179, 179, 179)

CROWN = pygame.transform.scale(pygame.image.load('assets/crown.png'), (44, 25))

GAME_ICON = pygame.image.load('assets/checkers_32.png')

TYPE = 'assets/FFF_Tusj.ttf'

BACKGRAUND = pygame.image.load('assets/backgraund.png')

WOOD = pygame.image.load('assets/wood.png')

WOOD_HOR = pygame.image.load('assets/woodBGh.jpg')

WOOD_WER = pygame.image.load('assets/woodBGw.jpg')

CORNER = pygame.image.load('assets/corner.jpg')
