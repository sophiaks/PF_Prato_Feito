
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

# tortilla = pygame.transform.scale(
#     (pygame.image.load('tortilla.png')), (250, 250))

bx = -150
by = 400
dindin = 1000
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
ORANGE = (255,140,0)
BROWN = (139,69,19)

# Desenhando o retângulo de ingredientes

# Classe da tortilla


class Tortilla(pygame.sprite.Sprite):
    def __init__(self, x,y):
        pygame.sprite.Sprite.__init__(self)
        self.x = y
        self.y = x
        self.image = pygame.Surface(tortilla.large_ing, tortilla.alt_ing)
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.image = pygame.transform.scale(player_img, (200, 200))
        self.radius = 100

    def update(self):
        self.rect.x += 1

    def trocaIngrediente(self):
        // TODO:
    
# Classe de ingredientes?


class Ingrediente(pygame.sprite.Sprite):
    larg_ing = 100
    alt_ing = 100

    def __init__(self, color, color_selecionado, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = y
        self.y = x
        self.color_selecionado = color_selecionado
        self.color = color
        self.image = pygame.Surface(
            (Ingredientes.larg_ing, Ingredientes.alt_ing))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def selecionado(self):
        self.image.fill(self.color_selecionado)



all_sprites = pygame.sprite.Group()
ingredientes=[]
ingredientes.append(Ingrediente(RED, DARK_RED, 100, 50))
ingredientes.append(Ingrediente(BLUE, DARK_RED, 100, 200))
ingredientes.append(Ingrediente(GREEN, DARK_RED, 100, 350))
ingredientes.append(Ingrediente(BLACK, DARK_RED, 100, 500))
ingredientes.append(Ingrediente(GOLD, DARK_RED, 100, 650))
ingredientes.append(Ingrediente(PINK, DARK_RED, 100, 800))
for i in ingredientes:
    all_sprites.add(i)
ingrediente_selecionado = None

tortilla = Tortilla(bx, by)
all_sprites.add(tortilla)

screen.fill(WHITE)

# Loop principal

while True:
    # bx += 1
    # screen.blit(tortilla, (bx, by))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            '''
            q1 = False
            q2 = False
            q3 = False
            q4 = False
            q5 = False
            q6 = False
            solta = False
            '''
            for ing in ingredientes:
                r = ing.rect
                if r.x <= mx and mx <= r.x + 100 and r.y <= my and my <= r.y + 100:
                    ingrediente_selecionado = ing
                    ing.selecionado()
                    pygame.display.update()
                    break
            # if 50 < mx < 150 and 100 < my < 200:
            #     ing12 = Ingredientes(DARK_RED, 100, 50)
            #     all_sprites.add(ing12)
            #     pygame.display.update()
            #     ingrediente_selecionado = ing12
            #     #q1 = True
            # if 200 < mx < 300 and 100 < my < 200:
            #     ing13 = Ingredientes(NAVY, 100, 200)
            #     all_sprites.add(ing13)
            #     pygame.display.update()
            #     #q2 = True
            # if 350 < mx < 450 and 100 < my < 200:
            #     ing14 = Ingredientes(DARK_GREEN, 100, 350)
            #     all_sprites.add(ing14)
            #     pygame.display.update()
            #     #q3 = True
            # if 500 < mx < 600 and 100 < my < 200:
            #     ing15 = Ingredientes(GRAY, 100, 500)
            #     all_sprites.add(ing15)
            #     pygame.display.update()
            #     #q4 = True
            # if 650 < mx < 750 and 100 < my < 200:
            #     ing16 = Ingredientes(OLIVE, 100, 650)
            #     all_sprites.add(ing16)
            #     pygame.display.update()
            #     #q5 = True
            # if 800 < mx < 900 and 100 < my < 200:
            #     ing17 = Ingredientes(BLUE, 100, 800)
            #     all_sprites.add(ing17)
            #     pygame.display.update()
            #     #q6 = True
        
            #if event.type == pygame.MOUSEBUTTONUP:
            #    solta = True

        if event.type == pygame.MOUSEBUTTONDOWN and ingrediente_selecionado is not None: #and q1 == True and solta == True:
            cx, cy = pygame.mouse.get_pos()
            tortilla.
            if (bx-125) < cx < (bx+125) and (by-125) < cy < (by+125):
                print("acerti")
                ing_teste = ingrediente_selecionado
                all_sprites.add(ing_teste)
                pygame.display.update()
                ingrediente_selecionado = None
            else:
                ing_testee = Ingredientes(BROWN, 100, 50)
                all_sprites.add(ing_testee)
                pygame.display.update()
                q1 = True
            if 200 < mx < 300 and 100 < my < 200:
                ing13 = Ingredientes(NAVY, 100, 200)
                all_sprites.add(ing13)
                pygame.display.update()
                q2 = True
            if 350 < mx < 450 and 100 < my < 200:
                ing14 = Ingredientes(DARK_GREEN, 100, 350)
                all_sprites.add(ing14)
                pygame.display.update()
                q3 = True
            if 500 < mx < 600 and 100 < my < 200:
                ing15 = Ingredientes(GRAY, 100, 500)
                all_sprites.add(ing15)
                pygame.display.update()
                q4 = True
            if 650 < mx < 750 and 100 < my < 200:
                ing16 = Ingredientes(OLIVE, 100, 650)
                all_sprites.add(ing16)
                pygame.display.update()
                q5 = True
            if 800 < mx < 900 and 100 < my < 200:
                ing17 = Ingredientes(BLUE, 100, 800)
                all_sprites.add(ing17)
                pygame.display.update()
                q6 = True
        # screen.get_rect()
            # if rect.left > 1000:
                #dindin -= 100

        # if q1==True and (bx-125)<mx<(bx-125) and (by-125)<my<(by-125):
        #    ing1 = Ingredientes(RED, 100, 150)
        #    pygame.display.update()
        # if q2==True and (bx-125)<mx<(bx-125) and (by-125)<my<(by-125):
        #    ing2 = Ingredientes(BLUE, 100, 450)
        #    pygame.display.update()
        # if q3==True and (bx-125)<mx<(bx-125) and (by-125)<my<(by-125):
        #    ing3 = Ingredientes(GREEN, 100, 350)
        #    pygame.display.update()

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    screen.blit(tortilla, (bx, by))
    pygame.display.update()
    fpsClock.tick(FPS)
