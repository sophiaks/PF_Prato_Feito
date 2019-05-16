import pygame
import sys
from os import path
from pygame.locals import *

# Inicializa o jogo
pygame.init()
# FPS e o Clock
FPS = 120
fpsClock = pygame.time.Clock()

# janela (screen)

screen = pygame.display.set_mode((1000, 750), 0, 32)

pygame.display.set_caption('Burrito Animado')

Tortilla = pygame.transform.scale(
    (pygame.image.load('tortilla.png')), (250, 250))

bx = -150
by = 400

# cores
BLACK = (0,   0,   0)
GRAY = (96, 96, 96)
WHITE = (255, 255, 255)
RED = (255,   0,   0)
DARK_RED = (153, 0, 0)
GREEN = (0, 255,   0)
DARK_GREEN = (0, 102, 0)
BLUE = (0,   0, 255)
NAVY = (0, 0, 102)
OLIVE = (128, 128, 0)
GOLD = (255, 215, 0)
PINK = (255, 51, 153)

# Desenhando o retângulo de ingredientes

#Classe da tortilla

class Tortilla(pygame.sprite.Sprite):
    def __init__(self, color,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = y
        self.y = x
        self.color = color
        self.image = pygame.Surface(Tortilla.large_ing, Tortilla.alt_ing)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = pygame.transform.scale(player_img, (200, 200))
        self.radius = 100
    
# Classe de ingredientes?


class Ingredientes(pygame.sprite.Sprite):
    larg_ing = 100
    alt_ing = 100

    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = y
        self.y = x
        self.color = color
        self.image = pygame.Surface(
            (Ingredientes.larg_ing, Ingredientes.alt_ing))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


all_sprites = pygame.sprite.Group()
ing1 = Ingredientes(RED, 100, 50)
ing2 = Ingredientes(BLUE, 100, 200)
ing3 = Ingredientes(GREEN, 100, 350)
ing4 = Ingredientes(BLACK, 100, 500)
ing5 = Ingredientes(GOLD, 100, 650)
ing6 = Ingredientes(PINK, 100, 800)
all_sprites.add(ing1, ing2, ing3, ing4, ing5, ing6)


screen.fill(WHITE)

# Loop principal

while True:
    bx += 1
    screen.blit(Tortilla, (bx, by))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            if 50 < mx < 150 and 100 < my < 200:
                ing12 = Ingredientes(DARK_RED, 100, 50)
                all_sprites.add(ing12)
                pygame.display.update()
                q1= True
            if 200 < mx < 300 and 100 < my < 200:
                ing13 = Ingredientes(NAVY, 100, 200)
                all_sprites.add(ing13)
                pygame.display.update()
                q2=True
            if 350 < mx < 450 and 100 < my < 200:
                ing14 = Ingredientes(DARK_GREEN, 100, 350)
                all_sprites.add(ing14)
                pygame.display.update()
                q3=True
            if 500 < mx < 600 and 100 < my < 200:
                ing15 = Ingredientes(GRAY, 100, 500)
                all_sprites.add(ing15)
                pygame.display.update()
                q4=True
            if 650 < mx < 750 and 100 < my < 200:
                ing16 = Ingredientes(OLIVE, 100, 650)
                all_sprites.add(ing16)
                pygame.display.update()
                q5=True
            if 800 < mx < 900 and 100 < my < 200:
                ing17 = Ingredientes(BLUE, 100, 800)
                all_sprites.add(ing17)
                pygame.display.update()
                q6=True
                
'''
        if q1==True and :
            ing1 = Ingredientes(RED, 100, 150)
        if q2==True and :
            ing2 = Ingredientes(BLUE, 100, 450)
        if q3==True and :
'''                
all_sprites.update()
screen.fill(WHITE)
all_sprites.draw(screen)
screen.blit(Tortilla, (bx, by))
pygame.display.update()
fpsClock.tick(FPS)
