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
        pygame.draw.line(win, BLACK, (10*gap, 0), (10*gap, WIDTH), 1)
        self.display_message("Tura gracza:", 615, 100)
        

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
        
        # Drawing figures
        for image in images:
            x, y, IMAGE = image
            win.blit(IMAGE, (x - IMAGE.get_width() // 2, y - IMAGE.get_height() // 2))

        if(white_turn):
            self.display_message("Biały", 660, 160)
        else:
            self.display_message("Czarny", 650, 160)
        pygame.display.update()

    def display_message(self,content,x,y):
        #win.fill(WHITE)
        text = END_FONT.render(content, 1, BLACK)
        win.blit(text, (x, y))
        pygame.display.update()
    
    def finish(self):
        if (self.white_pawns == 0 and self.black_pawns == 0):
            return True

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
                                    self.next_move=[[x,y-60],[x-60,y], [x-60, y-60]]
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
                                   self.next_move=[[x,y-60],[x-60,y], [x-60, y-60]]
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
                        elif (self.next_move ==[]):
                            images.append((x, y, white_IMAGE))
                            white_turn = False
                            black_turn = True
                            game_array[i][j] = (x, y, 'w', False)
                            self.white_pawns = self.white_pawns - 1
                            if(y == 570):
                                if(x == 30):
                                    self.next_moveb=[[x,y+60],[x+60,y], [x+60, y-60]]
                                elif(x == 570):
                                    self.next_moveb=[[x,y-60],[x-60,y], [x-60, y-60]]
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
                        
                        

                    elif black_turn:  # black turn
                        if([x,y] in self.next_moveb):
                            
                            images.append([x, y, black_IMAGE])
                            white_turn = True
                            black_turn = False
                            game_array[i][j] = (x, y, 'b', False)
                            self.black_pawns = self.black_pawns- 1

                            if(y == 570):
                                if(x == 30):
                                    self.next_move=[[x,y-60],[x+60,y], [x+60, y-60]]
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
                        elif self.next_moveb ==[]:
                            images.append([x, y, black_IMAGE])
                            white_turn = True
                            black_turn = False
                            game_array[i][j] = (x, y, 'b', False)
                            self.black_pawns = self.black_pawns- 1
                        
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


                        temp = [element for element in self.next_move if element in a]
                        
                        for i in range(len(temp)):
                            self.next_move.remove(temp[i])
        
        if not(self.finish()):
            #sprawdzanie wierszy
            for row in range(len(game_array)):
                q= game_array[row]
                if(q[t[0]][2] == q[t[1]][2] == q[t[2]][2] == q[t[3]][2]) and q[t[0]][2] == "b":
                    self.points_black += 1
                                
                elif (q[0][2] == q[1][2] == q[2][2] == q[3][2]) and q[0][2] == "w":
                    self.points_white += 1

            #sprawdzanie kolumn
            for col in range(len(game_array)):
                if (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2] == game_array[3][col][2]) and game_array[0][col][2] == "b":
                    self.points_black += 1
                elif (game_array[0][col][2] == game_array[1][col][2] == game_array[2][col][2] == game_array[3][col][2]) and game_array[0][col][2] == "w":
                    self.points_white += 1


            #print(self.points_black, self.points_black)
            for index, elem in enumerate(game_array):
                print("PREV: ", game_array[index][index-1])
                print("EL: ", elem[index])
                if (index+1 < len(game_array) and index+2 < len(game_array) and index - 1 >= 0):
                    prev_el = game_array[index][index-1][2]
                    curr_el = elem[index]
                    next_el = game_array[index][index+1][2]
                    next2_el = game_array[index][index+2][2]
                    if(prev_el == curr_el == next_el == next2_el):
                        print("1")
        
            
            #for index, elem in enumerate(images):
                #print("PREV: ", images[index-1][2])
                #print("EL: ", elem[2])
                #if (index+1 < len(images) and index+2 < len(images) and index - 1 >= 0):
                   # prev_el = images[index-1][2]
                   # curr_el = elem[2]
                   # next_el = images[index+1][2]
                   # next2_el = images[index+2][2]
                   # if(prev_el == curr_el == next_el == next2_el):
                      #  print("1")
        
                        

                       
                        
                                


                

            








