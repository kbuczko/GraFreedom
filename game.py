import math
from math import fabs

import pygame
import board

from board import Board
from board2 import board


global x_turn, o_turn, images, draw
draw = False
run = True
x_turn = True
o_turn = False


class Game(object):
    """
    Łączy wszystkie elementy gry w całość.
    """
    player = 'white'
    move = 0 #ruch nr 1 w grze albo freedom
    first_x = 0 #poprzedni ruch pozycja x
    first_y = 0 #poprzedni ruch pozycja y
    x = 0 #obecny ruch pozycja x
    y = 0 #obecny ruch pozycja y
    nrofmove = 0 #laczna liczba ruchow w grze (potrzebna przy ruchu nr 99 i 100)
    count1 = 0
    count2 = 0
    game_array =[]


    table = [[0 for i in range(10)] for j in range(10)]
    table2 = [[0 for i in range(10)] for j in range(10)]
    
    def display_message(content, self):
        pygame.time.delay(500)
        win.fill(WHITE)
        end_text = END_FONT.render(content, 1, BLACK)
        win.blit(end_text, ((WIDTH - end_text.get_width()) // 2, (WIDTH - end_text.get_height()) // 2))
        pygame.display.update()
        pygame.time.delay(3000)

    def __init__(self, width):
        """
        Przygotowanie ustawień gry
        :param width: szerokość planszy mierzona w pikselach
        """
        pygame.init()
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()

        #self.board = Board(width)
        self.board = board()

    def run(self):
        """
        Główna pętla gry
        """
        
        self.game_array = self.board.initialize_grid()
        
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.fps_clock.tick(15)

    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True
            if event.type == pygame.MOUSEBUTTONDOWN:
                self.board.player_move(self.game_array)
        self.board.render()
            
