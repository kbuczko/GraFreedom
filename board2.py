import pygame
import math


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
RED= (255,0,0)

# Images
white_IMAGE = pygame.transform.scale(pygame.image.load("images/pionek_bialyy.jpg"), (55, 55))
black_IMAGE = pygame.transform.scale(pygame.image.load("images/pionek_czarnyy.jpg"), (55, 55))

# Fonts
END_FONT = pygame.font.SysFont('arial', 32)

images = []
draw = False

run = True

play = True

abc = 0
white_turn = True
black_turn = False


class board(object):
    white_pawns = 50
    black_pawns = 50
    next_move = []
    next_moveb = []
    points_white = 0
    points_black = 0

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
        self.display_message("Player's turn:", 610, 100, BLACK)

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

    def text_objects(self,text, font):
        textSurface = font.render(text, True, BLACK)
        return textSurface, textSurface.get_rect()

    def render(self):
        win.fill(ORANGE)
        self.draw_grid()

        if(self.black_pawns == 1 and self.white_pawns == 0):
            pygame.draw.rect(win,WHITE,[640,300,70,60])
            smallText = pygame.font.SysFont('Helvetica', 20)
            textSurf, textRect = self.text_objects("Play?", smallText)
            textRect.center = ( (640+(70/2)), (300+(60/2)) )
            win.blit(textSurf, textRect)
            click = pygame.mouse.get_pressed()
            '''
            if click[0] == 1:
                play = True
            else:
                play = False
            '''
        # Drawing figures
        for image in images:
            x, y, IMAGE = image
            win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

        if (white_turn):
            self.display_message("White", 660, 150, BLACK)
        else:
            self.display_message("Black", 660, 150, BLACK)
        pygame.display.update()


    def display_message(self,content,x,y,colour):
        end_text = END_FONT.render(content, 1, colour)
        win.blit(end_text, (x,y))
        pygame.display.update()
    

    def finish(self):
        if (self.white_pawns == 0 and self.black_pawns == 0):
            if(self.points_white == self.points_black):
                self.display_message("It's a draw!", 625, 250, RED)
            elif(self.points_white > self.points_black):
                self.display_message("Player white", 615, 250, RED)
                self.display_message("won", 665, 285, RED)
            else:
                self.display_message("Player black", 615, 250, RED)
                self.display_message("won", 665, 285, RED)
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


    def player_move(self, game_array):
        #self.points_white = 3
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
                       
                        elif (self.next_move ==[]):
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
                        #if(self.white_pawns ==40):
                            #self.check_score(game_array)
                            
                    elif black_turn and self.black_pawns > 1:  # black turn
                        if ([x, y] in self.next_moveb):

                            images.append([x, y, black_IMAGE])
                            white_turn = True
                            black_turn = False
                            game_array[i][j] = (x, y, 'b', False)
                            self.black_pawns = self.black_pawns - 1

                            if (y == 570):
                                if (x == 30):
                                    self.next_move = [[x, y - 60], [x + 60, y], [x + 60, y - 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y - 60], [x - 60, y], [x - 60, y - 60]]
                                else:
                                    self.next_move = [[x - 60, y], [x + 60, y], [x - 60, y - 60], [x + 60, y - 60],
                                                      [x, y - 60]]
                            elif (y == 30):
                                if (x == 30):
                                    self.next_move = [[x, y + 60], [x + 60, y], [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y + 60], [x - 60, y], [x - 60, y + 60]]
                                else:
                                    self.next_move = [[x - 60, y], [x + 60, y], [x - 60, y + 60], [x + 60, y + 60],
                                                      [x, y + 60]]
                            else:
                                if (x == 30):
                                    self.next_move = [[x, y + 60], [x, y - 60], [x + 60, y], [x + 60, y - 60],
                                                      [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                      [x - 60, y + 60]]
                                else:
                                    self.next_move = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                      [x - 60, y + 60], [x + 60, y], [x + 60, y - 60], [x + 60, y + 60]]
                        elif self.next_moveb == []:
                            images.append([x, y, black_IMAGE])
                            white_turn = True
                            black_turn = False
                            game_array[i][j] = (x, y, 'b', False)
                            self.black_pawns = self.black_pawns - 1

                            if (y == 570):
                                if (x == 30):
                                    self.next_move = [[x, y - 60], [x - 60, y], [x - 60, y + 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y - 60], [x - 60, y], [x - 60, y - 60]]
                                else:
                                    self.next_move = [[x - 60, y], [x + 60, y], [x - 60, y - 60], [x + 60, y - 60],
                                                      [x, y - 60]]
                            elif (y == 30):
                                if (x == 30):
                                    self.next_move = [[x, y + 60], [x + 60, y], [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y + 60], [x - 60, y], [x - 60, y + 60]]
                                else:
                                    self.next_move = [[x - 60, y], [x + 60, y], [x - 60, y + 60], [x + 60, y + 60],
                                                      [x, y + 60]]
                            else:
                                if (x == 30):
                                    self.next_move = [[x, y + 60], [x, y - 60], [x + 60, y], [x + 60, y - 60],
                                                      [x + 60, y + 60]]
                                elif (x == 570):
                                    self.next_move = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                      [x - 60, y + 60]]
                                else:

                                    self.next_move = [[x, y + 60], [x, y - 60], [x - 60, y], [x - 60, y - 60],
                                                      [x - 60, y + 60], [x + 60, y], [x + 60, y - 60], [x + 60, y + 60]]

                        a = [[item[0], item[1]] for item in images]

                        temp = [element for element in self.next_move if element in a]

                        for i in range(len(temp)):
                            self.next_move.remove(temp[i])

                    elif black_turn and self.black_pawns==1:
                        a = int(input("1-graj dalej, 0- skoncz gre "))
                        if(a == 1):
                            images.append([x, y, black_IMAGE])
                            white_turn = True
                            black_turn = False
                            game_array[i][j] = (x, y, 'b', False)
                            self.black_pawns = self.black_pawns - 1
                        else:
                            self.black_pawns -= 1
                         
      
