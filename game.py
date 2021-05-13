import pygame

from board import Board


class Game(object):
    """
    Łączy wszystkie elementy gry w całość.
    """

    def text_objects(text, font):
        textSurface = font.render(text, True, black)
        return textSurface, textSurface.get_rect()

    def __init__(self, width, ai_turn=False):
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
           # if self.ai_turn:
                #self.ai.make_turn()
                #self.ai_turn = False
            self.fps_clock.tick(15)

    def handle_events(self):
        """
        Obsługa zdarzeń systemowych, tutaj zinterpretujemy np. ruchy myszką

        :return True jeżeli pygame przekazał zdarzenie wyjścia z gry
        """
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return True

            if event.type == pygame.MOUSEBUTTONDOWN:
                #if self.ai_turn:
                    # jeśli jeszcze trwa ruch komputera to ignorujemy zdarzenia
                    #continue
                # pobierz aktualną pozycję kursora na planszy mierzoną w pikselach
                x, y = pygame.mouse.get_pos()
                self.board.player_move(x, y)
                self.ai_turn = True