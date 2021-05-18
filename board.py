import pygame


class Board(object):

    player = "white"

    # konstruktor planszy gry
    def __init__(self, width):
        self.surface = pygame.display.set_mode((width, width), 0, 32)
        pygame.display.set_caption('Freedom Game')

        pygame.font.init()
        font_path = pygame.font.match_font('arial')
        self.font = pygame.font.Font(font_path, 48)

        # tablica znaczników 10x10 w formie listy
        self.markers = [None] * 100

    def draw(self, *args):
        """
        Rysuje okno gry

        :param args: lista obiektów do narysowania
        """
        background = (210, 180, 140)
        self.surface.fill(background)
        self.draw_net()
        self.draw_markers()
        self.draw_score()
        for drawable in args:
            drawable.draw_on(self.surface)

        # dopiero w tym miejscu następuje fatyczne rysowanie
        # w oknie gry, wcześniej tylko ustalaliśmy co i jak ma zostać narysowane
        pygame.display.update()

    def draw_net(self):
        """
        Rysuje siatkę linii na planszy
        """
        color = (0, 0, 0)
        width = self.surface.get_width()
        for i in range(1, 10):
            pos = width / 10 * i
            # linia pozioma
            pygame.draw.line(self.surface, color, (0, pos), (width, pos), 1)
            # linia pionowa
            pygame.draw.line(self.surface, color, (pos, 0), (pos, width), 1)

    def player_move(self, x, y):
        """
        Ustawia na planszy znacznik gracza X na podstawie współrzędnych w pikselach
        """
        cell_size = self.surface.get_width() / 10
        x /= cell_size
        y /= cell_size
        if self.player == "white":
            self.markers[int(x) + int(y) * 10] = player_marker(True)
        else:
            self.markers[int(x) + int(y) * 10] = player_marker(False)
        if self.player == "white":
            self.player = "black"
        else:
            self.player = "white"

    def draw_markers(self):
        """
        Rysuje znaczniki graczy
        """
        box_side = self.surface.get_width() / 10
        for x in range(10):
            for y in range(10):
                marker = self.markers[x + y * 10]
                if not marker:
                    continue
                # zmieniamy współrzędne znacznika
                # na współrzędne w pikselach dla centrum pola
                center_x = x * box_side + box_side / 2
                center_y = y * box_side + box_side / 2

                self.draw_text(self.surface, marker, (center_x, center_y))

    def draw_text(self, surface,  text, center, color=(100, 180, 180)):
        """
        Rysuje wskazany tekst we wskazanym miejscu
        """
        text = self.font.render(text, True, color)
        rect = text.get_rect()
        rect.center = center
        surface.blit(text, rect)

    def draw_score(self):
        """
        Sprawdza czy gra została skończona i rysuje właściwy komunikat
        """
        if check_win(self.markers, True):
            score = u"Wygrałeś(aś)"
        elif check_win(self.markers, True):
            score = u"Przegrałeś(aś)"
        elif None not in self.markers:
            score = u"Remis!"
        else:
            return

        i = self.surface.get_width() / 2
        self.draw_text(self.surface, score, center=(i, i), color=(255, 26, 26))

    def game_intro(self):
        width = self.surface.get_width()
        intro = True
        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
            self.surface.fill((255, 255, 255))
            i = self.surface.get_width() / 2
            self.draw_text(self.surface, u"Wygrałeś(aś)", center=(i, i), color=(0, 0, 0))

def player_marker(x_player):
    """
    Funkcja pomocnicza zwracająca znaczniki graczy
    :param x_player: True dla gracza X False dla gracza O
    :return: odpowiedni znak gracza
    """
    return "X" if x_player else "O"


def check_win(markers, x_player):
    """
    Sprawdza czy przekazany zestaw znaczników gry oznacza zwycięstwo wskazanego gracza

    :param markers: jednowymiarowa sekwencja znaczników w
    :param x_player: True dla gracza X False dla gracza O
    """
    win = [player_marker(x_player)] * 4
    seq = range(4)

    # definiujemy funkcję pomocniczą pobierającą znacznik
    # na podstawie współrzędnych x i y
    def marker(xx, yy):
        return markers[xx + yy * 3]

    # sprawdzamy każdy rząd
    for x in seq:
        row = [marker(x, y) for y in seq]
        if row == win:
            return True

    # sprawdzamy każdą kolumnę
    for y in seq:
        col = [marker(x, y) for x in seq]
        if col == win:
            return True

    # sprawdzamy przekątne
    diagonal1 = [marker(i, i) for i in seq]
    diagonal2 = [marker(i, abs(i-2)) for i in seq]
    if diagonal1 == win or diagonal2 == win:
        return True
