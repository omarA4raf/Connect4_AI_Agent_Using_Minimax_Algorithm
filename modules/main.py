import pygame
import sys
import math
from game_board import create_board, drop_piece, is_valid_location, get_next_open_row, print_board, \
    number_of_connected_fours, check_winner, is_full_board, draw_board

COLUMN_COUNT = 7
ROW_COUNT = 6
BLUE = (0, 76, 153)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
Black = (0, 0, 0)

def main():
    board = create_board()
    print_board(board)
    full_board = is_full_board(board)
    turn = 0

    pygame.init()

    SQUARESIZE = 100

    width = COLUMN_COUNT * SQUARESIZE
    height = (ROW_COUNT+1) * SQUARESIZE

    size = (width, height)

    RADIUS = int(SQUARESIZE/2 - 5)

    screen = pygame.display.set_mode(size)
    draw_board(board)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    while not full_board:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, WHITE, (0, 0, width, SQUARESIZE))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, RED, (posx, int(SQUARESIZE / 2)), RADIUS)
                else:
                    pygame.draw.circle(screen, Black, (posx, int(SQUARESIZE / 2)), RADIUS)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, WHITE, (0, 0, width, SQUARESIZE))
                # print(event.pos)
                # Ask for Player 1 Input
                if turn == 0:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 1)
                        full_board = is_full_board(board)

                # # Ask for Player 2 Input
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx / SQUARESIZE))

                    if is_valid_location(board, col):
                        row = get_next_open_row(board, col)
                        drop_piece(board, row, col, 2)
                        full_board = is_full_board(board)

                print_board(board)
                draw_board(board)

                turn += 1
                turn = turn % 2

                if full_board:
                    numbers_of_connected_fours_player1 = number_of_connected_fours(board, 1)
                    numbers_of_connected_fours_player2 = number_of_connected_fours(board, 2)
                    check_winner(numbers_of_connected_fours_player1, numbers_of_connected_fours_player2)
                    if numbers_of_connected_fours_player1 > numbers_of_connected_fours_player2:
                        label = myfont.render("Player 1 wins!!", 1, RED)
                        screen.blit(label, (40, 10))
                    elif numbers_of_connected_fours_player2 > numbers_of_connected_fours_player1:
                        label = myfont.render("Player 2 wins!!", 1, Black)
                        screen.blit(label, (40, 10))
                    else:
                        label = myfont.render("No winner!!", 1, RED)
                        screen.blit(label, (40, 10))
                    pygame.display.update()
                    pygame.time.wait(5000)

if __name__ == "__main__":
    main()
