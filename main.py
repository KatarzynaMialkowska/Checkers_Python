import pygame
import sys
from checkers.constants import TYPE, WOOD, BACKGRAUND, SCREEN_WIDTH, SCREEN_HEIGHT, SQUARE_SIZE, FPS, GAME_ICON, PIECES_G2
from checkers.game import Game
from minimax.algorithm import minimax
from pygame import mixer

# initialize the pygame
pygame.init()

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Checkers')
pygame.display.set_icon(GAME_ICON)
FONT_TITLE = pygame.font.Font(TYPE, 128)
FONT = pygame.font.Font(TYPE, 32)
mixer.set_num_channels(2) 
sound = mixer.Sound('assets/Adventure.mp3')
mixer.Channel(0).play(sound, loops = -1)
mixer.Channel(0).set_volume(0.05)

def position_from_mouse(pos):
    x, y = pos
    print(pos)
    row = y // SQUARE_SIZE
    col = x // SQUARE_SIZE
    print(f"{row}, {col}")
    return row, col


def draw_text(text, font, color, surface, x, y):
    text_obj = font.render(text, 1, color)
    text_rect = text_obj.get_rect()
    text_rect.topleft = (x, y)
    surface.blit(text_obj, text_rect)


def main_menu():
    click = False
    clock = pygame.time.Clock()
    color_g1 = (216, 183, 186)
    color_g2 = (216, 183, 186)
    while True:

        SCREEN.fill((0, 0, 0))
        SCREEN.blit(BACKGRAUND, (0, 0))
        draw_text('MENU', FONT_TITLE, (0, 0, 0), SCREEN, 240, 100)
        mx, my = pygame.mouse.get_pos()
        button_first = pygame.Rect(200, 320, 470, 140)
        button_second = pygame.Rect(200, 480, 470, 140)
        SCREEN.blit(WOOD, (200, 300))
        SCREEN.blit(WOOD, (200, 450))

        draw_text('PLAYER VS PLAYER', FONT, color_g1, SCREEN, 284.5, 370)
        draw_text('PLAYER VS COMPUTER', FONT, color_g2, SCREEN, 258.5, 520)

        if button_first.collidepoint((mx, my)):
            color_g1 = (255, 255, 255)
            if click:
                game_vs_player()
        else:
            color_g1 = (216, 183, 186)

        if button_second.collidepoint((mx, my)):
            color_g2 = (255, 255, 255)
            if click:
                game_vs_computer()
        else:
            color_g2 = (216, 183, 186)

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        pygame.display.update()
        clock.tick(FPS)


def game_vs_player():
    run = True
    clock = pygame.time.Clock()
    game = Game(SCREEN)

    while run:
        clock.tick(FPS)

        if game.winner():
            print(game.winner())

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = position_from_mouse(pos)
                game.select(row, col)
                

        game.update()
    
    
def game_vs_computer():
    run = True
    clock = pygame.time.Clock()
    game = Game(SCREEN)
    while run:
        clock.tick(FPS)

        if game.winner() != None:
            print(game.winner())

        if game.turn == PIECES_G2:
            score, new_board = minimax(game.get_board(), 4, PIECES_G2, game)
            game.ai_move(new_board)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos()
                row, col = position_from_mouse(pos)
                game.select(row, col)

        game.update()


main_menu()
