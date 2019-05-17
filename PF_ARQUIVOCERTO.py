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
# if toggle_fullscreen.full:
#     screen_res = pygame.display.set_mode((1000, 750), 0, 32),pygame.FULLSCREEN)
# else:
#     screen_res = pygame/display.set_mode((1000, 750), 0, 32)
#     toggle_fullscreen.full = not toggle_fullscreen.full
screen = pygame.display.set_mode((1000, 750), 0, 32)

pygame.display.set_caption('Burrito Animado')

tortilla = pygame.transform.scale(
    (pygame.image.load('tortilla.png')), (250, 250))

bx = 300
by = -100
dindin = 1000
# CORES
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
ORANGE = (255, 140, 0)
BROWN = (139, 69, 19)

# Desenhando o retângulo de ingredientes

# Classe da tortilla


class Tortilla(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = y
        self.y = x
        self.image = pygame.transform.scale(tortilla, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.radius = 100

    def update(self):
        self.rect.x += 1

    # def troca_ingrediente(self):
    #     //TODO

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
            (Ingrediente.larg_ing, Ingrediente.alt_ing))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def selecionado(self):
        self.image.fill(self.color_selecionado)


all_sprites = pygame.sprite.Group()
ingredientes = []
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

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit(0)
        
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            
            
            for ing in ingredientes:
                r = ing.rect
                if r.x <= mx and mx <= r.x + 100 and r.y <= my and my <= r.y + 100:
                    ingrediente_selecionado = ing
                    ing.selecionado()
                    pygame.display.update()
                    break

        if event.type == pygame.MOUSEBUTTONDOWN and ingrediente_selecionado is not None: 
            cx, cy = pygame.mouse.get_pos()
            t = tortilla.rect
            if t.x <= cx and cx <= t.x+250 and t.y <= cy and cy <= t.y + 250:
                print("acertei")
                ing_teste = ingrediente_selecionado
                #all_sprites.add(ing_teste)
                pygame.display.update()
                ingrediente_selecionado = None        

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
#screen.blit(tortilla.image, (bx, by))
    pygame.display.update()
    fpsClock.tick(FPS)
