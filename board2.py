import pygame
import math
from operator import itemgetter
pygame.init()

#DODAC ZLICZANIE FIGUR, DODAC DOWOLNE PORUSZANIE GDY POLA SĄSIADUJĄCE SĄ ZAJĘTE

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
END_FONT = pygame.font.SysFont('arial', 32)

images = []
draw = False

run = True

      

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
        pygame.draw.line(win, BLACK, (10*gap, 0), (10*gap, WIDTH), 1)
        

    def initialize_grid(self):
        dis_to_cen = WIDTH // ROWS // 2

        # Initializing the array
        game_array = []
        for i in range(10):
            game_array.append([None,None,None, None,None,None,None,None,None,None ])
    

    
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
        self.display_message("Tura gracza:", 615, 100)
        if(white_turn):
            self.display_message("Biały", 660, 160)
        else:
            self.display_message("Czarny", 650, 160)
        # Drawing figures
        for image in images:
            x, y, IMAGE = image
            win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

        pygame.display.update()

    def display_message(self,content,x,y):
        #win.fill(WHITE)
        text = END_FONT.render(content, 1, BLACK)
        win.blit(text, (x, y))
        pygame.display.update()

    def player_move(self, game_array):
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
                            if(y == 570):
                                if(x == 30):
                                    self.next_moveb=[[x,y-60],[x+60,y], [x+60, y-60]]
                                elif(x == 570):
                                    self.next_moveb=[[x,y+60],[x+60,y], [x+60, y+60]]
                                else:
                                    self.next_moveb = [[x-60,y],[x+60,y],[x-60,y-60],[x+60,y-60],[x,y-60]]
                            elif(y == 30):
                                if(x == 30):
                                    self.next_moveb = [[x, y+60],[x+60,y],[x+60,y+60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y+60],[x-60, y], [x-60,y+60]]
                                else:
                                    self.next_moveb = [[x-60,y],[x+60,y],[x-60,y+60],[x+60,y+60],[x,y+60]]
                            else:
                                if(x==30):
                                    self.next_moveb = [[x,y+60],[x,y-60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                                elif(x==570):
                                    self.next_moveb= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60]]
                                else:
                                    self.next_moveb= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60],[x+60,y],[x+60,y-60],[x+60,y+60]]

                        elif [x,y] in self.next_move:
                            images.append((x, y, white_IMAGE))
                            white_turn = False
                            black_turn = True
                            game_array[i][j] = (x, y, 'w', False)
                            self.white_pawns = self.white_pawns - 1
                            if(y == 570):
                                if(x == 30):
                                    self.next_moveb=[[x,y-60],[x+60,y], [x+60, y-60]]
                                elif(x == 570):
                                    self.next_moveb=[[x,y+60],[x-60,y], [x-60, y+60]]
                                else:
                                    self.next_moveb = [[x-60,y],[x+60,y],[x-60,y-60],[x+60,y-60],[x,y-60]]
                            elif(y == 30):
                                if(x == 30):
                                    self.next_moveb = [[x, y+60],[x+60,y],[x+60,y+60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y+60],[x-60, y], [x-60,y+60]]
                                else:
                                    self.next_moveb = [[x-60,y],[x+60,y],[x-60,y+60],[x+60,y+60],[x,y+60]]
                            else:
                                if(x==30):
                                    self.next_moveb = [[x,y+60],[x,y-60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                                elif(x==570):
                                    self.next_moveb= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60]]
                                else:
                                    self.next_moveb= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                        else:
                            images.append((x, y, white_IMAGE))
                            white_turn = False
                            black_turn = True
                            game_array[i][j] = (x, y, 'w', False)
                            self.white_pawns = self.white_pawns - 1
                            if(y == 570):
                                if(x == 30):
                                    self.next_moveb=[[x,y-60],[x+60,y], [x+60, y-60]]
                                elif(x == 570):
                                    self.next_moveb=[[x,y+60],[x-60,y], [x-60, y+60]]
                                else:
                                    self.next_moveb = [[x-60,y],[x+60,y],[x-60,y-60],[x+60,y-60],[x,y-60]]
                            elif(y == 30):
                                if(x == 30):
                                    self.next_moveb = [[x, y+60],[x+60,y],[x+60,y+60]]
                                elif (x == 570):
                                    self.next_moveb = [[x, y+60],[x-60, y], [x-60,y+60]]
                                else:
                                    self.next_moveb = [[x-60,y],[x+60,y],[x-60,y+60],[x+60,y+60],[x,y+60]]
                            else:
                                if(x==30):
                                    self.next_moveb = [[x,y+60],[x,y-60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                                elif(x==570):
                                    self.next_moveb= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60]]
                                else:
                                    self.next_moveb= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                                   
                        a = [[item[0], item[1]] for item in images]
                        temp = [element for element in self.next_moveb if element in a]
                        
                        for i in range(len(temp)):
                            self.next_moveb.remove(temp[i])
                        
                        print("Biały: ",x,y)
                        print("Ruchy: ", self.next_moveb)
                        

                    elif black_turn:  # black turn
                        if([x,y] in self.next_moveb):  
                            images.append([x, y, black_IMAGE])
                            white_turn = True
                            black_turn = False
                            game_array[i][j] = (x, y, 'b', False)
                            self.black_pawns = self.black_pawns- 1
                            self.a = x+60
                            self.b = y+60
                            if(y == 570):
                                if(x == 30):
                                    self.next_move=[[x,y-60],[x-60,y], [x-60, y+60]]
                                elif(x == 570):
                                    self.next_move=[[x,y-60],[x-60,y], [x-60, y-60]]
                                else:
                                    self.next_move = [[x-60,y],[x+60,y],[x-60,y-60],[x+60,y-60],[x,y-60]]
                            elif(y == 30):
                                if(x == 30):
                                    self.next_move = [[x, y+60],[x+60,y],[x+60,y+60]]
                                elif (x == 570):
                                    self.next_move = [[x, y+60],[x-60, y], [x-60,y+60]]
                                else:
                                    self.next_move = [[x-60,y],[x+60,y],[x-60,y+60],[x+60,y+60],[x,y+60]]
                            else:
                                if(x==30):
                                    self.next_move = [[x,y+60],[x,y-60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                                elif(x==570):
                                    self.next_move= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60]]
                                else:
                                    self.next_move= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                        else:
                            images.append([x, y, black_IMAGE])
                            white_turn = True
                            black_turn = False
                            game_array[i][j] = (x, y, 'b', False)
                            self.black_pawns = self.black_pawns- 1
                            self.a = x+60
                            self.b = y+60
                            if(y == 570):
                                if(x == 30):
                                    self.next_move=[[x,y-60],[x-60,y], [x-60, y+60]]
                                elif(x == 570):
                                    self.next_move=[[x,y-60],[x-60,y], [x-60, y-60]]
                                else:
                                    self.next_move = [[x-60,y],[x+60,y],[x-60,y-60],[x+60,y-60],[x,y-60]]
                            elif(y == 30):
                                if(x == 30):
                                    self.next_move = [[x, y+60],[x+60,y],[x+60,y+60]]
                                elif (x == 570):
                                    self.next_move = [[x, y+60],[x-60, y], [x-60,y+60]]
                                else:
                                    self.next_move = [[x-60,y],[x+60,y],[x-60,y+60],[x+60,y+60],[x,y+60]]
                            else:
                                if(x==30):
                                    self.next_move = [[x,y+60],[x,y-60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                                elif(x==570):
                                    self.next_move= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60]]
                                else:
                                    self.next_move= [[x,y+60],[x,y-60],[x-60,y],[x-60,y-60],[x-60,y+60],[x+60,y],[x+60,y-60],[x+60,y+60]]
                            
                        a = [[item[0], item[1]] for item in images]
                        print("CZARNY: ",x,y)
                        
                       

                        temp = [element for element in self.next_move if element in a]
                        
                        for i in range(len(temp)):
                            self.next_move.remove(temp[i])

                        print("Ruchy: ", self.next_move)
                        

                       
                        
                                


                

            








