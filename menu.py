#!/usr/bin/python3.4
# Setup Python ----------------------------------------------- #
import pygame, sys
import os
 
# Setup pygame/window ---------------------------------------- #
mainClock = pygame.time.Clock()
from pygame.locals import *
pygame.init()
pygame.display.set_caption('game base')
screen = pygame.display.set_mode((1280, 720),0,32)
 
font = pygame.font.SysFont(None, 20)
buttonFont = pygame.font.SysFont(None, 50)
titleFont =  pygame.font.SysFont('Comic Sans MS', 100)
 
def draw_text(text, font, color, surface, x, y):
    textobj = font.render(text, 1, color)
    textrect = textobj.get_rect()
    textrect.topleft = (x, y)
    surface.blit(textobj, textrect)
 
click = False
menu = True

def main_menu():
    while menu == True:
 
        screen.fill((0,0,0))
        draw_text('Puissance 4', titleFont, (255, 255, 255), screen, 350, 0)
 
        mx, my = pygame.mouse.get_pos()
        button_1 = pygame.Rect(475, 300, 300, 50)
        button_2 = pygame.Rect(475, 400, 300, 50)
        button_3 = pygame.Rect(475, 500, 300, 50)
        
    
        if button_1.collidepoint((mx, my)):
            if click:
                game()
        if button_2.collidepoint((mx, my)):
            if click:
                options()
        if button_3.collidepoint((mx, my)):
            if click:
                quit()
        pygame.draw.rect(screen, (255, 0, 0), button_1)
        pygame.draw.rect(screen, (255, 0, 0), button_2)
        pygame.draw.rect(screen, (255, 0, 0), button_3)

        draw_text('2 Joueurs', buttonFont, (255, 255, 255), screen, 500, 310)
        draw_text('Joueur vs IA', buttonFont, (255, 255, 255), screen, 500, 410)
        draw_text('Quit', buttonFont, (255, 255, 255), screen, 500, 510)
 
        click = False
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            if event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    sys.exit()
            if event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
 
        pygame.display.update()
        mainClock.tick(60)
 
def game():
    os.system('connect4.py')
 
def options():
    os.system('connect4_with_ai.py')
 
def quit():
    sys.exit()

main_menu()