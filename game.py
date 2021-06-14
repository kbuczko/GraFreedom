import math
from math import fabs

import pygame

import board
from board import Board


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

    table = [[0 for i in range(10)] for j in range(10)]
    table2 = [[0 for i in range(10)] for j in range(10)]
    def text_objects(text, font):
        textSurface = font.render(text, True)
        return textSurface, textSurface.get_rect()

    def __init__(self, width):
        """
        Przygotowanie ustawień gry
        :param width: szerokość planszy mierzona w pikselach
        """
        pygame.init()
        # zegar którego użyjemy do kontrolowania szybkości rysowania
        # kolejnych klatek gry
        self.fps_clock = pygame.time.Clock()

        self.board = Board(width)

    def run(self):
        """
        Główna pętla gry
        """
        while not self.handle_events():
            # działaj w pętli do momentu otrzymania sygnału do wyjścia
            self.board.draw()

            self.fps_clock.tick(15)

    def handle_events(self):
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

            if pygame.mouse.get_pressed()[0]:
                if (self.nrofmove >= 100):
                    print("endgame")
                    '''
                    #wyniki
                    #licznie przy lewej krawedzi
                    for i in range(0):
                        for j in range(10):
                            if self.table2[i][j]==self.table2[i+1][j] and self.table2[i+1][j]==self.table2[i+2][j] and self.table2[i+2][j]==self.table2[i+3][j] and self.table2[i][j] ==1 and self.table2[i+4][j] ==2:
                                self.count1 = self.count1+1
                            if self.table2[i][j] == self.table2[i + 1][j] and self.table2[i + 1][j] == \
                                    self.table2[i + 2][j] and self.table2[i + 2][j] == self.table2[i + 3][j] and \
                                    self.table2[i][j] == 2 and self.table2[i + 4][j] == 1:
                                self.count1 = self.count2 + 1
                    i=1
                    #liczenie w srodku
                    for i in range(6):
                        for j in range(10):
                            if self.table2[i][j]==2 and self.table2[i][j]==self.table2[i+1][j] and self.table2[i+1][j]==self.table2[i+2][j] and self.table2[i+2][j]==self.table2[i+3][j] and self.table2[i][j] ==1 and self.table2[i+4][j] ==2:
                                self.count1 = self.count1+1
                            if self.table2[i][j]==1 and self.table2[i][j] == self.table2[i + 1][j] and self.table2[i + 1][j] == \
                                    self.table2[i + 2][j] and self.table2[i + 2][j] == self.table2[i + 3][j] and \
                                    self.table2[i][j] == 2 and self.table2[i + 4][j] == 1:
                                self.count1 = self.count2 + 1
                    #liczenie na koncu
                    for i in range(0):
                        for j in range(10):
                            if self.table2[5][j]==2 and self.table2[6][j]==self.table2[6+1][j] and self.table2[6+1][j]==self.table2[6+2][j] and self.table2[6+2][j]==self.table2[6+3][j] and self.table2[6][j] ==1:
                                self.count1 = self.count1+1
                            if self.table2[5][j]==1 and self.table2[6][j] == self.table2[6 + 1][j] and self.table2[6 + 1][j] == \
                                    self.table2[6 + 2][j] and self.table2[6 + 2][j] == self.table2[6 + 3][j] and \
                                    self.table2[6][j] == 2:
                                self.count1 = self.count2 + 1

                    print(self.count1, self.count2)
                    if(self.count1>self.count2):
                        print("wygral gracz nr 1")
                    if (self.count1 < self.count2):
                        print("wygral gracz nr 2")
                    else:
                        print("remis")
                    print(self.table2)
                    '''

                if (self.nrofmove == 99):
                    self.nrofmove = 100
                    print("ruch 99")
                    # dorobic przedostatni ruch

                    # dorobic ruch

            if pygame.mouse.get_pressed()[2]:
                # pobierz aktualną pozycję kursora na planszy mierzoną w pikselach
                self.move = self.move + 1
                self.x, self.y = pygame.mouse.get_pos()



                if (self.nrofmove == 10):
                    #sprawdzenie wynikow
                    print("ruch nr 100")
                    #return True

                if self.move <=1 : #ruch nr 1 w grze albo freedom
                    #wyznaczamy srodek kafelka na ktorym stawiamy pionek
                    xc = math.ceil(self.x/70) - 1
                    yc = math.ceil(self.y/70) - 1
                    self.x = xc*70+35
                    self.y = yc*70+35
                    #przesuwamy x na poprzednie miejsca, nowy x to przyszly stary x
                    self.first_x = self.x
                    self.first_y = self.y
                    #ustawiamy pionek na planszy
                    if self.table[xc][yc] != 'x':
                        self.board.player_move(self.x, self.y)
                        self.table[xc][yc] = 'x'
                        self.table2[xc][yc] = self.nrofmove % 2 + 1
                        self.nrofmove = self.nrofmove + 1
                        print(self.nrofmove)
                    else:
                        print("niedozwolony ruch")
                        self.move = self.move -1
                    #tabela kontrolna, zaznaczamy zajete pozycje



                    #print(self.table2)
                    #print(self.table)
                    # sprawdzenie freedom w srodku planszy
                    if (xc >= 1 and xc < 9 and yc >= 1 and yc < 9):
                        if (self.table[xc - 1][yc] =='x' and self.table[xc - 1][yc - 1] =='x' and self.table[xc][
                            yc - 1] =='x' and self.table[xc + 1][yc] =='x' and self.table[xc][yc + 1] =='x' and
                                self.table[xc + 1][yc + 1] =='x' and self.table[xc + 1][yc - 1] =='x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")
                    # sprawdzenie freedom prawy dolny
                    if (xc == 9 and yc == 9):
                        if (self.table[xc - 1][yc] =='x' and self.table[xc - 1][yc - 1] =='x' and self.table[xc][
                            yc - 1] =='x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")
                    # sprawdzenie freedom prawy górny
                    if (xc == 9 and yc == 0):
                        if (self.table[xc - 1][yc]  =='x' and self.table[xc - 1][yc + 1] =='x' and self.table[xc][
                            yc + 1] =='x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")

                    # sprawdzenie freedom lewy górny
                    if (xc == 0 and yc == 0):
                        if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc + 1] == 'x' and self.table[xc][
                            yc + 1] == 'x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")
                    # sprawdzenie freedom lewy dolny
                    if (xc == 0 and yc == 9):
                        if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc - 1] == 'x' and self.table[xc][
                            yc - 1] == 'x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")
                    # sprawdzenie freedom dolna krawedz
                    if (xc > 0 and xc < 9 and yc == 9):
                        if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc - 1] == 'x' and self.table[xc][
                            yc - 1] == 'x' and self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc - 1] == 'x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")
                    # sprawdzenie freedom gorna krawedz
                    if (xc > 0 and xc < 9 and yc == 0):
                        if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc + 1] == 'x' and self.table[xc][
                            yc + 1] == 'x' and self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc + 1] == 'x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")
                    # sprawdzenie freedom prawa krawedz
                    if (xc == 9 and yc > 0 and yc < 9):
                        if (self.table[xc][yc + 1] == 'x' and self.table[xc][yc - 1] == 'x' and self.table[xc - 1][
                            yc - 1] == 'x' and self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc + 1] == 'x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")

                    # sprawdzenie freedom lewa krawedz
                    if (xc == 0 and yc > 0 and yc < 9):
                        if (self.table[xc][yc + 1] == 'x' and self.table[xc][yc - 1] == 'x' and self.table[xc + 1][
                            yc - 1] == 'x' and self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc + 1] == 'x'):
                            self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                            print("freedom")



                else:
                    #jezeli chcemy postawic odpowiednio blisko nowy pionek, to wtedy przechodzi ifa nizej

                    if fabs(self.first_x-self.x)<70 and fabs(self.first_y-self.y)<70:
                        xc = math.ceil(self.x / 70) - 1
                        yc = math.ceil(self.y / 70) - 1
                        self.x = xc * 70 + 35
                        self.y = yc * 70 + 35
                        self.first_x = self.x
                        self.first_y = self.y
                        #print (xc,yc)
                        #sprawdzenie freedom w srodku planszy
                        if(xc>=1 and xc<9 and yc>=1 and yc<9):
                            if(self.table[xc-1][yc]=='x' and self.table[xc-1][yc-1]=='x'and self.table[xc][yc-1]=='x'and self.table[xc+1][yc]=='x'and self.table[xc][yc+1]=='x'and self.table[xc+1][yc+1]=='x' and self.table[xc + 1][yc - 1] =='x'):
                                self.move = 0 #zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")
                        #sprawdzenie freedom prawy dolny
                        if(xc==9 and yc==9):
                            if (self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc - 1] == 'x' and self.table[xc][yc - 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")
                        # sprawdzenie freedom prawy górny
                        if (xc == 9 and yc == 0):
                            if (self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc + 1] == 'x' and self.table[xc][
                                yc + 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")

                        # sprawdzenie freedom lewy górny
                        if (xc == 0 and yc == 0):
                            if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc + 1] == 'x' and self.table[xc][
                                yc + 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")
                        # sprawdzenie freedom lewy dolny
                        if (xc == 0 and yc == 9):
                            if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc - 1] == 'x' and self.table[xc][
                                yc - 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")
                        #sprawdzenie freedom dolna krawedz
                        if (xc > 0 and xc < 9 and yc == 9):
                            if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc - 1] == 'x' and self.table[xc][
                                yc - 1] == 'x' and self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc - 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")
                        # sprawdzenie freedom gorna krawedz
                        if (xc > 0 and xc < 9 and yc == 0):
                            if (self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc + 1] == 'x' and self.table[xc][
                                yc + 1] == 'x' and self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc + 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")
                        # sprawdzenie freedom prawa krawedz
                        if (xc == 9 and yc > 0 and yc < 9):
                            if (self.table[xc][yc+1] == 'x' and self.table[xc][yc - 1] == 'x' and self.table[xc-1][
                                yc - 1] == 'x' and self.table[xc - 1][yc] == 'x' and self.table[xc - 1][yc + 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")

                        # sprawdzenie freedom lewa krawedz
                        if (xc == 0 and yc > 0 and yc < 9):
                            if (self.table[xc][yc+1] == 'x' and self.table[xc][yc - 1] == 'x' and self.table[xc+1][
                                yc - 1] == 'x' and self.table[xc + 1][yc] == 'x' and self.table[xc + 1][yc + 1] == 'x'):
                                self.move = 0  # zajete wszystkie miejsca obok, dowolny ruch na planszy
                                print("freedom")






                        #jezeli na wybranym polu nie ma pionka, to stawia go na planszy i w tabeli kontrolnej
                        if self.table[xc][yc] != 'x':
                            self.board.player_move(self.x, self.y)
                            self.table[xc][yc] = 'x'
                            self.table2[xc][yc] = self.nrofmove % 2 +1
                            self.nrofmove = self.nrofmove + 1
                            print(self.nrofmove)
                        else:
                            print("niedozwolony ruch")
                    #print(self.table2)

                print(self.table2)
