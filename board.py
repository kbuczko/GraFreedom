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
        """
        
        background = (210, 180, 140)
        self.surface.fill(background)
        self.draw_net()
        self.draw_markers()
        self.draw_score()
        if(self.player == "white"):
            self.draw_text(self.surface, "Tura gracza: " + self.player, (self.surface.get_width()/2, self.surface.get_width()-50))
        else:
            self.draw_text(self.surface, "Tura gracza: " + self.player, (self.surface.get_width()/2, self.surface.get_width()-50), (0,0,0))
        for drawable in args:
            drawable.draw_on(self.surface)

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
        #pygame.draw.line(self.surface, color, (600, 0), (600, width), 1)
        #pygame.draw.line(self.surface, color, (0, 600), (width, 600), 1)

    def player_move(self, x, y):
        """
        Ustawia na planszy znacznik gracza X na podstawie współrzędnych w pikselach
        """
        cell_size = self.surface.get_width() / 10
        x /= cell_size
        y /= cell_size

        if self.player == "white":
            self.markers[int(x) + int(y) * 10] = player_marker(True)
            largeText = pygame.font.SysFont('Helvetica', 50)
            self.player = "black"
        else:
            self.markers[int(x) + int(y) * 10] = player_marker(False)
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
               
               

    def draw_text(self, surface,  text, center, color=(255,255,255)):
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
        if check_score(self.markers, True):
            i = self.surface.get_width() / 2
            self.draw_text(self.surface, "a", center=(i, i), color=(255, 26, 26))
        elif check_score(self.markers, False):
            i = self.surface.get_width() / 2
            self.draw_text(self.surface, "b", center=(i, i), color=(255, 26, 26))
        else:
            return

        
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
           

def check_score(markers, x_player):
    point = [player_marker(x_player)] * 4
    seq = range(4)


    def marker(xx, yy):
        return markers[xx + yy * 4]

    for x in seq:
        row = [marker(x, y) for y in seq]
        if row == point:
            return True

    for y in seq:
        col = [marker(x, y) for x in seq]
        if col == point:
            return True

    diagonal1 = [marker(i, i) for i in seq]
    diagonal2 = [marker(i, abs(i-2)) for i in seq]
    if diagonal1 == point or diagonal2 == point:
        return True


def player_marker(x_player):
    """
    Funkcja pomocnicza zwracająca znaczniki graczy
    :param x_player: True dla gracza X False dla gracza O
    :return: odpowiedni znak gracza
    """
    return "o" if x_player else "O"


