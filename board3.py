import queue
import threading

import pygame
import math
from state import GameState
from nodes import MonteCarloTreeSearchNode
from search import MonteCarloTreeSearch

pygame.init()

# Screen
WIDTH = 600
ROWS = 10
win = pygame.display.set_mode((WIDTH, WIDTH))
pygame.display.set_caption("Freedom")

# Colors
ORANGE = (252, 195, 134)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Images
white_IMAGE = pygame.transform.scale(pygame.image.load("images/pionek_bialyy.jpg"), (55, 55))
black_IMAGE = pygame.transform.scale(pygame.image.load("images/pionek_czarnyy.jpg"), (55, 55))

# Fonts
END_FONT = pygame.font.SysFont('arial', 40)

images = []
draw = False

run = True

next_move = []

white_turn = True
black_turn = False


class board(object):
    white_pawns = 50
    black_pawns = 50
    next_move = []
    next_moveb = []

    def draw_grid(self):
        gap = WIDTH // ROWS

        # Starting points
        x = 0
        y = 0

        for i in range(ROWS):
            x = i * gap

            pygame.draw.line(win, BLACK, (x, 0), (x, WIDTH), 1)
            pygame.draw.line(win, BLACK, (0, x), (WIDTH, x), 1)
        pygame.draw.line(win, BLACK, (10 * gap, 0), (10 * gap, WIDTH), 1)

    def initialize_grid(self):
        dis_to_cen = WIDTH // ROWS // 2

        # Initializing the array
        game_array = []
        for i in range(10):
            game_array.append([None, None, None, None, None, None, None, None, None, None])

        for i in range(len(game_array)):
            for j in range(len(game_array[i])):
                x = dis_to_cen * (2 * j + 1)
                y = dis_to_cen * (2 * i + 1)

                # Adding centre coordinates
                game_array[i][j] = (x, y, "", True)

        return game_array

    def render(self):
        win.fill(ORANGE)
        self.draw_grid()

        # Drawing figures
        for image in images:
            x, y, IMAGE = image
            win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

        pygame.display.update()

    def finish(self):
        if (self.white_pawns == 0 and self.black_pawns == 0):
            return True

    def Freedom(self, table, xc, yc):
        # return true if freedom
        self.table = table
        self.xc = xc
        self.yc = yc
        print(self.table[3])
        if (xc >= 1 and xc < 9 and yc >= 1 and yc < 9):
            if (self.table[xc - 1][yc][3] == False and self.table[xc - 1][yc - 1][3] == False and self.table[xc][
                yc - 1][3] == False and self.table[xc + 1][yc][3] == False and self.table[xc][yc + 1][3] == False and
                    self.table[xc + 1][yc + 1][3] == False and self.table[xc + 1][yc - 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy
        # sprawdzenie freedom prawy dolny
        if (xc == 9 and yc == 9):
            if (self.table[xc - 1][yc][3] == False and self.table[xc - 1][yc - 1][3] == False and self.table[xc][
                yc - 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy

        # sprawdzenie freedom prawy górny
        if (xc == 9 and yc == 0):
            if (self.table[xc - 1][yc][3] == False and self.table[xc - 1][yc + 1][3] == False and self.table[xc][
                yc + 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy

        # sprawdzenie freedom lewy górny
        if (xc == 0 and yc == 0):
            if (self.table[xc + 1][yc][3] == False and self.table[xc + 1][yc + 1][3] == False and self.table[xc][
                yc + 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy

        # sprawdzenie freedom lewy dolny
        if (xc == 0 and yc == 9):
            if (self.table[xc + 1][yc][3] == False and self.table[xc + 1][yc - 1][3] == False and self.table[xc][
                yc - 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy

        # sprawdzenie freedom dolna krawedz
        if (xc > 0 and xc < 9 and yc == 9):
            if (self.table[xc + 1][yc][3] == False and self.table[xc + 1][yc - 1][3] == False and self.table[xc][
                yc - 1][3] == False and self.table[xc - 1][yc][3] == False and self.table[xc - 1][yc - 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy

        # sprawdzenie freedom gorna krawedz
        if (xc > 0 and xc < 9 and yc == 0):
            if (self.table[xc + 1][yc][3] == False and self.table[xc + 1][yc + 1][3] == False and self.table[xc][
                yc + 1][3] == False and self.table[xc - 1][yc][3] == False and self.table[xc - 1][yc + 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy

        # sprawdzenie freedom prawa krawedz
        if (xc == 9 and yc > 0 and yc < 9):
            if (self.table[xc][yc + 1][3] == False and self.table[xc][yc - 1][3] == False and self.table[xc - 1][
                yc - 1][3] == False and self.table[xc - 1][yc][3] == False and self.table[xc - 1][yc + 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy

        # sprawdzenie freedom lewa krawedz
        if (xc == 0 and yc > 0 and yc < 9):
            if (self.table[xc][yc + 1][3] == False and self.table[xc][yc - 1][3] == False and self.table[xc + 1][
                yc - 1][3] == False and self.table[xc + 1][yc][3] == False and self.table[xc + 1][yc + 1][3] == False):
                return True  # zajete wszystkie miejsca obok, dowolny ruch na planszy
        else:
            return False

    def get_Possieble_Move(self, move):
        moves_list = []
        for j in range(10):
            for i in range(10):
                for move in self.gen_legal_moves(j, i):
                    moves_list.append({move: {(i, j)}})
        return moves_list

    def gen_legal_moves(self, table, x, y):
        move_set = set()
        offsets = [[x - 1, y - 1], [x, y - 1], [x + 1, y], [x, y + 1], [x + 1, y + 1], [x - 1, y], [x - 1, y + 1],
                   [x + 1, y - 1]]
        for offset in offsets:
            newX = x + offset[0]
            newY = y + offset[1]

            if self.move_check(table, newX, newY):
                move_set.add((newX, newY))
        return move_set

    def move_check(self, table, i, j):
        if self.Freedom(table, i, j) == True:
            if table[i][j][3] == True:
                return True
            else:
                return False

    def check_score(self, table):
        self.table = table
        score = [0, 0]
        temp = 0
        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if (self.table[i][j][2]) == 'w':
                    print(self.table[i][j])
                    temp = 1
                    # sprawdzanie w liniach
                    if j - 1 in range(len(self.table[i])) and (self.table[i][j - 1][2]) == 'w':
                        print(self.table[i][j])
                        temp = temp + 1
                        if j + 1 in range(len(self.table[i])) and (self.table[i][j + 1][2]) == 'w':
                            print(self.table[i][j])
                            temp = temp + 1
                            if j + 2 in range(len(self.table[i])) and (self.table[i][j + 2][2]) == 'w':
                                print(self.table[i][j])
                                temp = temp + 1
                                if j + 3 in range(len(self.table[i])) and (self.table[i][j + 3][2]) == 'w':
                                    print(self.table[i][j])
                                    temp = temp + 1
                                    if j + 4 in range(len(self.table[i])) and (self.table[i][j + 4][2]) == 'w':
                                        print(self.table[i][j])
                                        temp = temp + 1
                                        if temp == 4:
                                            temp = 0
                                            score[0] = score[0] + 1
                                        else:
                                            temp = 0
                    # sprawdzanie w kolumnach
                    if i - 1 in range(len(self.table)) and (self.table[i - 1][j][2]) == 'w':
                        print(self.table[i][j])
                        temp = temp + 1
                        if i + 1 in range(len(self.table)) and (self.table[i + 1][j][2]) == 'w':
                            print(self.table[i][j])
                            temp = temp + 1
                            if i + 2 in range(len(self.table)) and (self.table[i + 2][j][2]) == 'w':
                                print(self.table[i][j])
                                temp = temp + 1
                                if i + 3 in range(len(self.table)) and (self.table[i + 3][j][2]) == 'w':
                                    print(self.table[i][j])
                                    temp = temp + 1
                                    if i + 4 in range(len(self.table)) and (self.table[i + 4][j][2]) == 'w':
                                        print(self.table[i][j])
                                        temp = temp + 1
                                        if temp == 4:
                                            temp = 0
                                            score[0] = score[0] + 1
                                        else:
                                            temp = 0

                    if i - 1 in range(len(self.table)) and j - 1 in range(len(self.table[i - 1])) and (
                    self.table[i - 1][j - 1][2]) == 'w':
                        temp = temp + 1
                        if i + 1 in range(len(self.table)) and j + 1 in range(len(self.table[i + 1])) and (
                        self.table[i + 1][j + 1][2]) == 'w':
                            temp = temp + 1
                            if i + 2 in range(len(self.table)) and j + 2 in range(len(self.table[i + 2])) and (
                                    self.table[i + 2][j + 2][2]) == 'w':
                                temp = temp + 1
                                if i + 3 in range(len(self.table)) and j + 3 in range(len(self.table[i + 3])) and (
                                        self.table[i + 3][j + 3][2]) == 'w':
                                    temp = temp + 1
                                    if i + 4 in range(len(self.table)) and j + 4 in range(len(self.table[i + 4])) and (
                                            self.table[i + 4][j + 4][2]) == 'w':
                                        temp = temp + 1
                                        if temp == 4:
                                            temp = 0
                                            score[0] = score[0] + 1
                                        else:
                                            temp = 0

        for i in range(len(self.table)):
            for j in range(len(self.table[i])):
                if (self.table[i][j][2]) == 'b':
                    temp = 1
                    # sprawdzanie w liniach
                    if j - 1 in range(len(self.table[i])) and (self.table[i][j - 1][2]) == 'b':
                        temp = temp + 1
                        if j + 1 in range(len(self.table[i])) and (self.table[i][j + 1][2]) == 'b':
                            temp = temp + 1
                            if j + 2 in range(len(self.table[i])) and (self.table[i][j + 2][2]) == 'b':
                                temp = temp + 1
                                if j + 3 in range(len(self.table[i])) and (self.table[i][j + 3][2]) == 'b':
                                    temp = temp + 1
                                    if j + 4 in range(len(self.table[i])) and (self.table[i][j + 4][2]) == 'b':
                                        temp = temp + 1
                                        if temp == 4:
                                            temp = 0
                                            score[1] = score[1] + 1
                                        else:
                                            temp = 0

                    # sprawdzanie w kolumnach
                    if i - 1 in range(len(self.table)) and (self.table[i - 1][j][2]) == 'b':
                        temp = temp + 1
                        if i + 1 in range(len(self.table)) and (self.table[i + 1][j][2]) == 'b':
                            temp = temp + 1
                            if i + 2 in range(len(self.table)) and (self.table[i + 2][j][2]) == 'b':
                                temp = temp + 1
                                if i + 3 in range(len(self.table)) and (self.table[i + 3][j][2]) == 'b':
                                    temp = temp + 1
                                    if i + 4 in range(len(self.table)) and (self.table[i + 4][j][2]) == 'b':
                                        temp = temp + 1
                                        if temp == 4:
                                            temp = 0
                                            score[1] = score[1] + 1
                                        else:
                                            temp = 0

                    if i - 1 in range(len(self.table)) and j - 1 in range(len(self.table[i - 1])) and (
                    self.table[i - 1][j - 1][2]) == 'b':
                        temp = temp + 1
                        if i + 1 in range(len(self.table)) and j + 1 in range(len(self.table[i + 1])) and (
                        self.table[i + 1][j + 1][2]) == 'b':
                            temp = temp + 1
                            if i + 2 in range(len(self.table)) and j + 2 in range(len(self.table[i + 2])) and (
                                    self.table[i + 2][j + 2][2]) == 'b':
                                temp = temp + 1
                                if i + 3 in range(len(self.table)) and j + 3 in range(len(self.table[i + 3])) and (
                                        self.table[i + 3][j + 3][2]) == 'b':
                                    temp = temp + 1
                                    if i + 4 in range(len(self.table)) and j + 4 in range(len(self.table[i + 4])) and (
                                            self.table[i + 4][j + 4][2]) == 'b':
                                        temp = temp + 1
                                        if temp == 4:
                                            temp = 0
                                            score[1] = score[1] + 1
                                        else:
                                            temp = 0
        print(score)

    # def player_move(self, game_array):
    #     global white_turn, black_turn, images, freedom
    #     freedom = False
    #
    #     # Mouse position
    #     m_x, m_y = pygame.mouse.get_pos()
    #
    #     for i in range(len(game_array)):
    #         for j in range(len(game_array[i])):
    #             x, y, char, can_play = game_array[i][j]
    #
    #
    #             # Distance between mouse and the centre of the square
    #             dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)
    #
    #
    #             # If it's inside the square
    #             if dis < WIDTH // ROWS // 2 and can_play:
    #                 if white_turn:  # white turn
    #
    #
    #                     if freedom == False and [x,y] in self.next_move:
    #                         images.append((x, y, white_IMAGE))
    #                         white_turn = False
    #                         black_turn = True
    #                         game_array[i][j] = (x, y, 'w', False)
    #                         self.white_pawns = self.white_pawns - 1
    #                     elif freedom == True or self.white_pawns==50:
    #                             images.append((x, y, white_IMAGE))
    #                             white_turn = False
    #                             black_turn = True
    #                             game_array[i][j] = (x, y, 'w', False)
    #                             self.white_pawns = self.white_pawns - 1
    #                     if(self.Freedom(table=game_array,xc= i,yc= j)==True):
    #                             print("freedom black")
    #                             freedom = True
    #                     else:
    #                         self.next_moveb = [[x - 60, y - 60], [x, y - 60], [x + 60, y], [x, y + 60],
    #                                                [x + 60, y + 60], [x - 60, y], [x - 60, y + 60], [x + 60, y - 60]]
    #                         print("false black")
    #                         freedom = False
    #
    #                 elif black_turn:
    #                     if freedom == False and [x,y] in self.next_moveb:  # black turn
    #                         images.append((x, y, black_IMAGE))
    #                         white_turn = True
    #                         black_turn = False
    #                         game_array[i][j] = (x, y, 'b', False)
    #                         self.black_pawns = self.black_pawns - 1
    #                         self.a = x + 60
    #                         self.b = y + 60
    #                     elif freedom == True:
    #                         images.append((x, y, black_IMAGE))
    #                         white_turn = True
    #                         black_turn = False
    #                         game_array[i][j] = (x, y, 'b', False)
    #                         self.black_pawns = self.black_pawns - 1
    #                 if (self.Freedom(table=game_array, xc=i, yc=j)==True):
    #                         print("freedom white")
    #                         freedom = True
    #                 else:
    #                     self.next_move = [[x - 60, y - 60], [x, y - 60], [x + 60, y], [x, y + 60], [x + 60, y + 60],
    #                                           [x - 60, y], [x - 60, y + 60], [x + 60, y - 60]]
    #                     print("false white")
    #                     freedom = False
    #                 if(self.black_pawns == 0):
    #                     self.check_score(game_array)

    def finish(self):
        if (self.white_pawns == 0 and self.black_pawns == 0):
            return True

    def player_move(self, game_array):
        is_simulation_running = False
        t1, t2 = None, None
        q1, q2 = queue.Queue(), queue.Queue()
        global white_turn, black_turn, images

        # Mouse position
        m_x, m_y = pygame.mouse.get_pos()

        for i in range(len(game_array)):
            for j in range(len(game_array[i])):
                x, y, char, can_play = game_array[i][j]

                # Distance between mouse and the centre of the square
                dis = math.sqrt((x - m_x) ** 2 + (y - m_y) ** 2)

                # If it's inside the square
                if dis < WIDTH // ROWS // 2 and can_play:
                    if white_turn:  # white turn
                        if self.white_pawns == 50:
                            images.append([x, y, white_IMAGE])
                            white_turn = False
                            black_turn = True
                            game_array[i][j] = (x, y, 'w', False)
                            self.white_pawns = self.white_pawns - 1
                            if (y == 570):
                                if (x == 30):
                                    self.next_moveb = [[x, y - 60], [x + 60, y], [x + 60, y - 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y - 60], [x - 60, y], [x - 60, y - 60]]
                                else:
                                    self.next_moveb = [[x - 60, y], [x + 60, y], [x - 60, y - 60], [x + 60, y - 60],
                                                       [x, y - 60]]
                            elif (y == 30):
                                if (x == 30):
                                    self.next_moveb = [[x, y + 60], [x + 60, y], [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y + 60], [x - 60, y], [x - 60, y + 60]]
                                else:
                                    self.next_moveb = [[x - 60, y], [x + 60, y], [x - 60, y + 60], [x + 60, y + 60],
                                                       [x, y + 60]]
                            else:
                                if (x == 30):
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x + 60, y], [x + 60, y - 60],
                                                       [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                       [x - 60, y + 60]]
                                else:
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                       [x - 60, y + 60], [x + 60, y], [x + 60, y - 60],
                                                       [x + 60, y + 60]]

                        elif [x, y] in self.next_move:
                            images.append((x, y, white_IMAGE))
                            white_turn = False
                            black_turn = True
                            game_array[i][j] = (x, y, 'w', False)
                            self.white_pawns = self.white_pawns - 1
                            if (y == 570):
                                if (x == 30):
                                    self.next_moveb = [[x, y - 60], [x + 60, y], [x + 60, y - 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y - 60], [x - 60, y], [x - 60, y - 60]]
                                else:
                                    self.next_moveb = [[x - 60, y], [x + 60, y], [x - 60, y - 60], [x + 60, y - 60],
                                                       [x, y - 60]]
                            elif (y == 30):
                                if (x == 30):
                                    self.next_moveb = [[x, y + 60], [x + 60, y], [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y + 60], [x - 60, y], [x - 60, y + 60]]
                                else:
                                    self.next_moveb = [[x - 60, y], [x + 60, y], [x - 60, y + 60], [x + 60, y + 60],
                                                       [x, y + 60]]
                            else:
                                if (x == 30):
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x + 60, y], [x + 60, y - 60],
                                                       [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                       [x - 60, y + 60]]
                                else:
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                       [x - 60, y + 60], [x + 60, y], [x + 60, y - 60],
                                                       [x + 60, y + 60]]
                        elif (self.next_move == []):
                            images.append((x, y, white_IMAGE))
                            white_turn = False
                            black_turn = True
                            game_array[i][j] = (x, y, 'w', False)
                            self.white_pawns = self.white_pawns - 1
                            if (y == 570):
                                if (x == 30):
                                    self.next_moveb = [[x, y + 60], [x + 60, y], [x + 60, y - 60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y - 60], [x - 60, y], [x - 60, y - 60]]
                                else:
                                    self.next_moveb = [[x - 60, y], [x + 60, y], [x - 60, y - 60], [x + 60, y - 60],
                                                       [x, y - 60]]
                            elif (y == 30):
                                if (x == 30):
                                    self.next_moveb = [[x, y + 60], [x + 60, y], [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y + 60], [x - 60, y], [x - 60, y + 60]]
                                else:
                                    self.next_moveb = [[x - 60, y], [x + 60, y], [x - 60, y + 60], [x + 60, y + 60],
                                                       [x, y + 60]]
                            else:
                                if (x == 30):
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x + 60, y], [x + 60, y - 60],
                                                       [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                       [x - 60, y + 60]]
                                else:
                                    self.next_moveb = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                       [x - 60, y + 60], [x + 60, y], [x + 60, y - 60],
                                                       [x + 60, y + 60]]

                        a = [[item[0], item[1]] for item in images]
                        temp = [element for element in self.next_moveb if element in a]

                        for i in range(len(temp)):
                            self.next_moveb.remove(temp[i])

                        board_state = GameState(state = game_array,next_to_move = 1)
                        root = MonteCarloTreeSearchNode(state=board_state, parent= None)
                        mcts = MonteCarloTreeSearch(root)
                        if not is_simulation_running:
                            t1 = threading.Thread(target=mcts.best_action, args=(100, q1))
                            t1.daemon = True
                            t1.start()
                            is_simulation_running = True
                        else:
                            if not q1.empty():
                                best_node = q1.get()
                                q1.queue.clear()
                                is_simulation_running = False
                                c_state = best_node.state
                                c_board = c_state.board

                                i_point = c_state.current_move.i()
                                j_point = c_state.current_move.j()
                                if i_point == 0:
                                    x = 30
                                elif i_point ==1:
                                    x= 90
                                elif i_point == 2:
                                    x= 150
                                elif i_point == 3:
                                    x=210
                                elif i_point == 4:
                                    x=270
                                elif i_point ==5:
                                    x=330
                                elif i_point ==6:
                                    x=390
                                elif i_point==7:
                                    x=450
                                elif i_point==8:
                                    x=510
                                elif i_point==9:
                                    x=570
                                if j_point == 0:
                                    y = 30
                                elif j_point == 1:
                                    y = 90
                                elif j_point == 2:
                                    y = 150
                                elif j_point == 3:
                                    y = 210
                                elif j_point == 4:
                                    y = 270
                                elif j_point == 5:
                                    y = 330
                                elif j_point == 6:
                                    y = 390
                                elif j_point == 7:
                                    y = 450
                                elif j_point == 8:
                                    y = 510
                                elif j_point == 9:
                                    y = 570

                                images.append((x, y, white_IMAGE))
                                white_turn = True
                                black_turn = False
                                game_array[i_point][j_point] = (x, y, 'w', False)


                        a = [[item[0], item[1]] for item in images]

                        temp = [element for element in self.next_move if element in a]

                        for i in range(len(temp)):
                            self.next_move.remove(temp[i])

        if not (self.finish()):
            # self.check_score(game_array)
            # sprawdzanie wierszy
            for row in range(len(game_array)):
                q = game_array[row]
                if (q[0][2] == q[1][2] == q[2][2] == q[3][2]) and q[0][2] == "b":
                    self.points_black += 1

                elif (q[0][2] == q[1][2] == q[2][2] == q[3][2]) and q[0][2] == "w":
                    self.points_white += 1

            # sprawdzanie kolumn
            for col in range(len(game_array)):
                if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2] == game_array[3][col][
                    2]) and game_array[0][col][2] == "b":
                    self.points_black += 1
                elif (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2] == game_array[3][col][
                    2]) and game_array[0][col][2] == "w":
                    self.points_white += 1

            # print(self.points_black, self.points_black)
            for index, elem in enumerate(game_array):
                print("PREV: ", game_array[index][index - 1])
                print("EL: ", elem[index])
                if (index + 1 < len(game_array) and index + 2 < len(game_array) and index - 1 >= 0):
                    prev_el = game_array[index][index - 1][2]
                    curr_el = elem[index]
                    next_el = game_array[index][index + 1][2]
                    next2_el = game_array[index][index + 2][2]
                    if (prev_el == curr_el == next_el == next2_el):
                        print("1")
