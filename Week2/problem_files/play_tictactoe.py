import pygame
import random
import json
import argparse


def draw_cross(x_pos, y_pos, s):
    global screen
    pygame.draw.line(s, P1_COLOR, (x_pos + 25, y_pos + 25), (x_pos + 75, y_pos + 75), 10)
    pygame.draw.line(s, P1_COLOR, (x_pos + 25, y_pos + 75), (x_pos + 75, y_pos + 25), 10)
    screen.blit(s, (0, 0))


def draw_circle(x_pos, y_pos, s):
    global screen
    pygame.draw.circle(s, P2_COLOR, (x_pos + 50, y_pos + 50), 25, 10)
    screen.blit(s, (0, 0))


def draw_shape(x_pos, y_pos, s, turn):
    global arguments
    if turn:
        if arguments.BotPlayer == 'x':
            draw_circle(x_pos, y_pos, s)
        else:
            draw_cross(x_pos, y_pos, s)
    else:
        if arguments.BotPlayer == 'x':
            draw_cross(x_pos, y_pos, s)
        else:
            draw_circle(x_pos, y_pos, s)


def draw_board(s):
    global moves, winning_line, turn, board, game_over, arial_font, winner, board_index_to_coordinates_map, blank_screen, arguments
    s.fill(BG_COLOR)

    if blank_screen:
        if game_over:
            blank_screen = False
        return

    pygame.draw.line(s, BOARD_COLOR, (100, 100), (100, 400), 5)
    pygame.draw.line(s, BOARD_COLOR, (200, 100), (200, 400), 5)
    pygame.draw.line(s, BOARD_COLOR, (300, 100), (300, 400), 5)
    pygame.draw.line(s, BOARD_COLOR, (400, 100), (400, 400), 5)

    pygame.draw.line(s, BOARD_COLOR, (100, 100), (400, 100), 5)
    pygame.draw.line(s, BOARD_COLOR, (100, 200), (400, 200), 5)
    pygame.draw.line(s, BOARD_COLOR, (100, 300), (400, 300), 5)
    pygame.draw.line(s, BOARD_COLOR, (100, 400), (400, 400), 5)

    if winning_line and game_over and winner is not None:
        for move in moves:
            draw_shape(move[0], move[1], s, move[2])

        if winning_line[2]:
            if arguments.BotPlayer == 'x':
                pygame.draw.line(s, P1_COLOR, winning_line[0], winning_line[1], 15)
            else:
                pygame.draw.line(s, P2_COLOR, winning_line[0], winning_line[1], 15)
        else:
            if arguments.BotPlayer == 'x':
                pygame.draw.line(s, P1_COLOR, winning_line[0], winning_line[1], 15)
            else:
                pygame.draw.line(s, P2_COLOR, winning_line[0], winning_line[1], 15)
        img = arial_font.render('Player ' + str(int(winner)) + ' Wins!', True, BOARD_COLOR)
        s.blit(img, (160, 20))
    elif game_over and winner is None:
        for move in moves:
            draw_shape(move[0], move[1], s, move[2])
        img = arial_font.render('Draw!', True, BOARD_COLOR)
        s.blit(img, (210, 20))
    elif winner is not None:
        for move in moves:
            draw_shape(move[0], move[1], s, move[2])
        img = arial_font.render('Player ' + str(int(winner)) + ' Wins!', True, BOARD_COLOR)
        s.blit(img, (135, 20))
    else:
        for move in moves:
            draw_shape(move[0], move[1], s, move[2])
        if turn:
            if arguments.BotPlayer == 'x':
                img = arial_font.render('Player 2 Move', True, P2_COLOR)
            else:
                img = arial_font.render('Player 1 Move', True, P1_COLOR)
        else:
            if arguments.BotPlayer == 'x':
                img = arial_font.render('Player 1 Move', True, P1_COLOR)
            else:
                img = arial_font.render('Player 2 Move', True, P2_COLOR)
        s.blit(img, (160, 20))


def check_win():
    global winning_line, board
    if board[0] == board[1] == board[2] and board[0] != '0':
        if board[0] == 'x':
            winning_line = [(125, 150), (375, 150), False]
        else:
            winning_line = [(125, 150), (375, 150), True]
        return board[0]
    elif board[3] == board[4] == board[5] and board[3] != '0':
        if board[3] == 'x':
            winning_line = [(125, 250), (375, 250), False]
        else:
            winning_line = [(125, 250), (375, 250), True]
        return board[3]
    elif board[6] == board[7] == board[8] and board[6] != '0':
        if board[6] == 'x':
            winning_line = [(125, 350), (375, 350), False]
        else:
            winning_line = [(125, 350), (375, 350), True]
        return board[6]
    elif board[0] == board[3] == board[6] and board[0] != '0':
        if board[0] == 'x':
            winning_line = [(150, 125), (150, 375), False]
        else:
            winning_line = [(150, 125), (150, 375), True]
        return board[0]
    elif board[1] == board[4] == board[7] and board[1] != '0':
        if board[1] == 'x':
            winning_line = [(250, 125), (250, 375), False]
        else:
            winning_line = [(250, 125), (250, 375), True]
        return board[1]
    elif board[2] == board[5] == board[8] and board[2] != '0':
        if board[2] == 'x':
            winning_line = [(350, 125), (350, 375), False]
        else:
            winning_line = [(350, 125), (350, 375), True]
        return board[2]
    elif board[0] == board[4] == board[8] and board[0] != '0':
        if board[0] == 'x':
            winning_line = [(125, 125), (375, 375), False]
        else:
            winning_line = [(125, 125), (375, 375), True]
        return board[0]
    elif board[2] == board[4] == board[6] and board[2] != '0':
        if board[2] == 'x':
            winning_line = [(375, 125), (125, 375), False]
        else:
            winning_line = [(375, 125), (125, 375), True]
        return board[2]
    else:
        return False


def check_draw():
    global board
    for i in range(9):
        if board[i] == '0':
            return False
    return True


def make_move(move):
    global moves, board, turn, game_over, winner, blank_screen, game_history, arguments
    moves.add(move)

    ind = move[0] // 100 + 3 * (move[1] // 100 - 1) - 1
    if move[2]:
        if arguments.BotPlayer == 'x':
            board[ind] = 'o'
        else:
            board[ind] = 'x'
        game_history.append(ind)
    else:
        if arguments.BotPlayer == 'x':
            board[ind] = 'x'
        else:
            board[ind] = 'o'
        game_history.append(str(ind))

    win = check_win()
    draw = check_draw()
    if win == 'x':
        winner = 1
        blank_screen = False
        return 'x'
    elif win == 'o':
        winner = 2
        blank_screen = False
        return 'o'
    elif draw:
        blank_screen = False
        return 'draw'
    return False


def in_square(x, y, square):
    top_left_corner = board_index_to_coordinates_map[square]
    if x > top_left_corner[0] and x < top_left_corner[0] + 100 and y > top_left_corner[1] and y < top_left_corner[
        1] + 100:
        return True
    else:
        return False


def return_square(x, y):
    if in_square(x, y, 0):
        return 0
    elif in_square(x, y, 1):
        return 1
    elif in_square(x, y, 2):
        return 2
    elif in_square(x, y, 3):
        return 3
    elif in_square(x, y, 4):
        return 4
    elif in_square(x, y, 5):
        return 5
    elif in_square(x, y, 6):
        return 6
    elif in_square(x, y, 7):
        return 7
    elif in_square(x, y, 8):
        return 8
    else:
        return None


def move_action(event, last_click_time, square, surface):
    global click_delay, moves, turn, screen, winner, game_over, blank_screen
    move_coordinates = board_index_to_coordinates_map[square]

    if (move_coordinates[0], move_coordinates[1], turn) and (
            move_coordinates[0], move_coordinates[1], not turn) not in moves:
        if event.type == pygame.MOUSEBUTTONDOWN:
            current_time = pygame.time.get_ticks()
            if current_time - last_click_time > click_delay:
                game_over = make_move((move_coordinates[0], move_coordinates[1], turn))
                turn = not turn
                blank_screen = True
                draw_board(screen)

            # Update last click time
            last_click_time = current_time
        else:
            draw_board(screen)
            draw_shape(move_coordinates[0], move_coordinates[1], surface, turn)

    return last_click_time


parser = argparse.ArgumentParser()
parser.add_argument('--BotPlayer', type=str, required=True, help='x or o')
parser.add_argument('--BotStrategyFile', type=str, required=True, help='json file containing strategy')
arguments = parser.parse_args()

# pygame setup
pygame.init()
screen = pygame.display.set_mode((500, 500))

pygame.display.set_caption("Tic Tac Toe")

# global variables
clock = pygame.time.Clock()
click_delay = 500  # milliseconds
last_click_time = 0
dt = 0
running = True
if arguments.BotPlayer == 'x':
    turn = False
else:
    turn = True
game_over = False
winning_line = None
winner = None
blank_screen = False
strategy_file_name = arguments.BotStrategyFile
use_policy = True

# define the colors
BOARD_COLOR = "black"
P1_COLOR = "red"
P2_COLOR = "blue"
BG_COLOR = "white"
arial_font = pygame.font.SysFont('arialunicode', 36)

board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
game_history = []

moves = set()
coordinates_to_board_index_map = {(100, 100): 0, (200, 100): 1, (300, 100): 2,
                                  (100, 200): 3, (200, 200): 4, (300, 200): 5,
                                  (100, 300): 6, (200, 300): 7, (300, 300): 8}

board_index_to_coordinates_map = {0: (100, 100), 1: (200, 100), 2: (300, 100),
                                  3: (100, 200), 4: (200, 200), 5: (300, 200),
                                  6: (100, 300), 7: (200, 300), 8: (300, 300)}

policy = json.load(open(strategy_file_name, 'r'))

# game loop
while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # toggle blank_screen when enter pressed
                blank_screen = False
            elif event.key == pygame.K_y:
                # reset game when y pressed
                board = ['0', '0', '0', '0', '0', '0', '0', '0', '0']
                game_history = []
                moves = set()
                if arguments.BotPlayer == 'x':
                    turn = False
                else:
                    turn = True
                game_over = False
                winning_line = None
                winner = None
                blank_screen = False
            elif event.key == pygame.K_n:
                # quit game when n pressed
                running = False

    x = pygame.mouse.get_pos()[0]
    y = pygame.mouse.get_pos()[1]
    # create a surface to draw on of the same size as the screen
    surface = pygame.Surface((500, 500))
    surface.set_alpha(100)

    if blank_screen:
        draw_board(screen)
        for i in range(8):
            pygame.draw.arc(screen, BOARD_COLOR, (220, 220, 60, 60), 0.33 * i * 3.14, 0.33 * (i + 1) * 3.14, 8)
            pygame.display.flip()
            pygame.time.wait(10)
            pygame.draw.arc(screen, BG_COLOR, (220, 220, 60, 60), 0.33 * i * 3.14, 0.33 * (i + 1) * 3.14, 8)

        blank_screen = False

    elif not game_over:
        if use_policy and not turn:
            board_str = ''.join([str(act) for act in game_history])
            if board_str not in policy.keys():
                print('Error: You policy does not contain history', board_str)
                exit(1)
            available_plays = policy[board_str]
            random_number = random.uniform(0, 1)
            sum = 0
            chosen_play = -1
            for key, val in available_plays.items():
                sum += available_plays[key]
                if random_number <= sum:
                    chosen_play = key
                    break
            move_coordinates = board_index_to_coordinates_map[int(chosen_play)]

            if (move_coordinates[0], move_coordinates[1], turn) and (
                    move_coordinates[0], move_coordinates[1], not turn) not in moves:
                game_over = make_move((move_coordinates[0], move_coordinates[1], turn))
                turn = not turn
                blank_screen = True
                draw_board(screen)
            # else:
            #     raise Exception("TA error")

        else:
            square = return_square(x, y)
            if square is None:
                draw_board(screen)
            else:
                last_click_time = move_action(event, last_click_time, square, surface)
    else:
        draw_board(screen)
        # show message "Play again? y/n"
        img = arial_font.render('Play again? y/n', True, BOARD_COLOR)
        screen.blit(img, (160, 430))

    # flip() the display to put your work on screen
    pygame.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pygame.quit()
