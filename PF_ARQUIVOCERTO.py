import pygame
import sys
from os import path
from pygame.locals import *
import random

# Inicializa o jogo
pygame.init()
pygame.mixer.init()
# FPS e o Clock
FPS = 120
fpsClock = pygame.time.Clock()
lista_ingredientes = ['salada', 'arroz', 'peixe', 'feijao', 'cogumelo']
listacomb = random.randint(1,5)
vel = 5

screen = pygame.display.set_mode((1000, 750), 0, 32)

pygame.display.set_caption('Burrito Animado')

tortilla = pygame.transform.scale(
    pygame.image.load('tortilla.png'), (250, 250))


bx = 300
by = -100

#Começa com 1000 de dinheiro
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
        self.image = tortilla #pygame.transform.scale(tortilla, (250, 250))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen_rect = screen.get_rect()
        self.image.set_colorkey(BLACK)

        #Carregar as imagens
        lista = ['A', 'AFP', 'AFPC', 'AF', 'AFPCC', 'S', 'SF', 'SFA', 'SFAC', 'SFACP', 'SS', 'SSP', 'SSPC', 'SSPCC']
        self.images = {}
        for nome in lista_ingredientes:
            self.images[nome] = pygame.transform.scale(pygame.image.load('{0}.png'.format(nome)), (20, 20))
        self.images['ERRO'] = pygame.image.load('ERRO.png').convert()
        self.combo = ''

    #Loop do combo
        i = 1
        while i < len(lista):
            if lista[i] > lista[i - 1]:
                self.combo = lista[i]
            i += 1

    #Atualiza a posição do sprite
    def update(self):
        self.rect.x += vel

    def troca_ingrediente(self, ingrediente):
        self.combo += ingrediente
        center = self.rect.center
        if self.combo in self.images:
            self.image = self.images[self.combo]
        else:
            self.image = self.images['ERRO']
        self.rect = self.image
        self.rect.center = center

# Classe da esteira
class Esteira(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        esteira = pygame.transform.scale(pygame.image.load('esteirapixel.png'), (1000, 300))
        self.image = pygame.transform.scale(esteira, (1000, 300))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# Classe de ingredientes
class Ingrediente(pygame.sprite.Sprite):
    larg_ing = 100
    alt_ing = 100
    def __init__(self, image, x, y, letra):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        #for ingrediente in lista_ingredientes:
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.letra = letra

    # def selecionado(self):
    #     self.image.fill(self.color_selecionado)

    # def nao_selecionado(self):
    #     self.image.fill(self.color)


all_sprites = pygame.sprite.Group()
ingredientes = []
ingredientes.append(Ingrediente('arroz.png', 50, 100, 'A'))
ingredientes.append(Ingrediente('salada.png', 200, 100, 'S'))
ingredientes.append(Ingrediente('cogumelo.png', 350, 100, 'C'))
ingredientes.append(Ingrediente('peixe.png', 500, 100, 'P'))
ingredientes.append(Ingrediente("feijao.png", 650, 100, 'F'))
for i in ingredientes:
    all_sprites.add(i)
ingrediente_selecionado = None

esteira = Esteira(0, 400)
all_sprites.add(esteira)

tortilla = Tortilla(bx, by)
all_sprites.add(tortilla)

# tela de fundo
background = pygame.image.load('planofundo.png').convert()
background_rect = background.get_rect()


# Loop principal

try:

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)

        # Se a pessoa clicar com o mouse:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
        # Para cada ingrediente na lista de ingredientes se a pessoa clicar dentro do retângulo do ingrediente
                for ing in ingredientes:
                    r = ing.rect
                    if r.x <= mx and mx <= r.x + 100 and r.y <= my and my <= r.y + 100:
                        print("click")
                        ing = ingrediente_selecionado
                    #Selecionou o arroz
                        if ingrediente_selecionado == Ingrediente('{0}.png'.format(ing), 100, 350, ingrediente_selecionado.letra):
                            print("arroz")
                            tortilla.troca_ingrediente(ingrediente_selecionado.letra)
                            pygame.display.update()
                        #Selecionou a salada
                        if ingrediente_selecionado == Ingrediente('salada.png', 100, 500, 'S'):
                            print("salada")
                            pygame.display.update()
                        #Selecionou o cogumelo
                        if ingrediente_selecionado == Ingrediente('cogumelo.png', 100, 650, 'C'):
                            print("cogumelo")
                            pygame.display.update()
                        #Selecionou o feijao
                        if ingrediente_selecionado == Ingrediente('feijao.png', 100, 800, 'F'):
                            print("feijao")
                            pygame.display.update()
                        #Selecionou o peixe
                        if ingrediente_selecionado == Ingrediente('peixe.png', 100, 950, 'p'):
                            print("peixe")
                            pygame.display.update()
                            break

            if event.type == pygame.MOUSEBUTTONDOWN and ingrediente_selecionado is not None:
                cx, cy = pygame.mouse.get_pos()
                t = tortilla.rect
                print(cx,cy)
                if t.x <= cx and cx <= t.x+250 and t.y <= cy and cy <= t.y + 250:
                    tortilla.troca_ingrediente(ingrediente_selecionado.letra)
                    print("BIA DEU CERTO")
                    print('uhullll')

            # if listacomb == []:
            # if num_menu == 2:
        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        fpsClock.tick(FPS)
        pygame.display.update()
finally:
    pygame.quit()
    sys.exit(0)
