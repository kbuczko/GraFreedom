import pygame
import time
import random

from game import Game


pygame.init()

#zdjecie tla
background_image = pygame.image.load("images/tlo.jpg")

def game_loop():
    game = Game(600)
    game.run()

display_width = 800
display_height = 600

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)

block_color = (53, 115, 255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Freedom')
clock = pygame.time.Clock()




def text_objects(text, font):
    textSurface = font.render(text, True, black)
    return textSurface, textSurface.get_rect()


def message_display(text):
    largeText = pygame.font.SysFont('Helvetica', 100)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((display_width / 2), (display_height / 2))
    gameDisplay.blit(TextSurf, TextRect)
    gameDisplay.blit(background_image, [0, 0])
    pygame.display.update()

    time.sleep(2)


def quitGame():
    pygame.quit()
    quit()


def button(msg, x, y, w, h, ic, ac, action=None):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()

    if x + w > mouse[0] > x and y + h > mouse[1] > y:
        pygame.draw.rect(gameDisplay, ac, (x, y, w, h))

        if click[0] == 1 and action != None:
            action()
    else:
        pygame.draw.rect(gameDisplay, ic, (x, y, w, h))

    smallText = pygame.font.SysFont('Helvetica', 20)
    textSurf, textRect = text_objects(msg, smallText)
    textRect.center = ((x + (w / 2)), (y + (h / 2)))
    gameDisplay.blit(textSurf, textRect)



def play_choice():
    running = True
    while running:
        gameDisplay.fill(white)

        # wyswietlenie tla
        gameDisplay.blit(background_image, [0, 0])

        largeText = pygame.font.SysFont('Helvetica', 50)
        TextSurf, TextRect = text_objects("Choose a mode", largeText)
        TextRect.center = ((display_width / 2), (display_height - 500))
        gameDisplay.blit(TextSurf, TextRect)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False


        button("Player vs Player", 300, 190, 195, 75, (235, 161, 52), (235, 143, 52), game_loop)
        button("Player vs Computer", 300, 340, 195, 75, (235, 161, 52), (235, 143, 52), game_loop)
        button("Back", 300, 490, 195, 75, (235, 161, 52), (235, 143, 52), game_intro)

        pygame.display.update()
        clock.tick(15)

def loop():
    running = True

    while running:
        exit()



def game_intro():
    intro = True

    while intro:
        for event in pygame.event.get():
            print(event)
            if event.type == pygame.QUIT:
                pygame.display.quit()
                pygame.quit()
                quit()

        gameDisplay.fill(white)
        #wyswietlenie tla
        gameDisplay.blit(background_image, [0, 0])
        largeText = pygame.font.SysFont('Helvetica', 100)
        TextSurf, TextRect = text_objects("Freedom Game", largeText)
        TextRect.center = ((display_width / 2), (display_height - 400))
        gameDisplay.blit(TextSurf, TextRect)


        button("Play", 150, 450, 100, 50, (235, 161, 52), (235, 143, 52), play_choice)
        button("Quit", 550, 450, 100, 50, (235, 161, 52), (235, 143, 52), quitGame)

        pygame.display.update()
        clock.tick(15)





game_intro()
pygame.quit()
quit()
