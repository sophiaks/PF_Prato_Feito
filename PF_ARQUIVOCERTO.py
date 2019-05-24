import pygame
import sys
from os import path
from pygame.locals import *


# Inicializa o jogo
pygame.init()
pygame.mixer.init()
# FPS e o Clock
FPS = 120
fpsClock = pygame.time.Clock()
#listaing = [arroz, feijao, peixe, cogumelo, alface]
#listacomb = random.randint
vel = 1

screen = pygame.display.set_mode((1000, 750), 0, 32)

pygame.display.set_caption('Burrito Animado')

tortilla = pygame.transform.scale(
    (pygame.image.load('tortilla.png')), (250, 250))
esteira = pygame.transform.scale(
    (pygame.image.load('esteirapixel.png')), (250, 300))

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
        self.screen_rect = screen.get_rect()

        #Carregar as imagens
        lista = ['A','AF','AFA', 'AFAC']
        self.images = {}
        for nome in lista:
            self.images[nome] = pygame.image.load('{0}.png'.format(nome)).convert()
        self.images['ERRO'] = pygame.image.load('ERRO.png').convert()

        self.combo = ''


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



tortilla2 = pygame.transform.scale(
    (pygame.image.load('AF.png')), (250, 250))
tortilla3 = pygame.transform.scale(
    (pygame.image.load('AFA.png')), (250, 250))
tortilla4 = pygame.transform.scale(
    (pygame.image.load('AFAC.png')), (250, 250))
tortilla5 = pygame.transform.scale(
    (pygame.image.load('AFACP.png')), (250, 250))



# Classe da esteira
class Esteira(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = y
        self.y = x
        self.image = pygame.transform.scale(esteira, (250, 300))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# Classe de ingredientes


class Ingrediente(pygame.sprite.Sprite):
    larg_ing = 100
    alt_ing = 100

    def __init__(self, color, color_selecionado, x, y, letra):
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

        self.letra = letra

    def selecionado(self):
        self.image.fill(self.color_selecionado)

    def nao_selecionado(self):
        self.image.fill(self.color)


all_sprites = pygame.sprite.Group()
ingredientes = []
ingredientes.append(Ingrediente(RED, DARK_RED, 100, 50, 'A'))
ingredientes.append(Ingrediente(BLUE, OLIVE, 100, 200, 'F'))
ingredientes.append(Ingrediente(GREEN, DARK_GREEN, 100, 350, 'R'))
ingredientes.append(Ingrediente(BLACK, GRAY, 100, 500, 'C'))
ingredientes.append(Ingrediente(GOLD, NAVY, 100, 650, 'P'))
ingredientes.append(Ingrediente(PINK, BLACK, 100, 800, 'G'))
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

    # Se a pessoa clicar com o mouse:
        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
    # Para cada ingrediente na lista de ingredientes se a pessoa clicar dentro do retângulo do ingrediente
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
                for ing in ingredientes:
                    if ingrediente_selecionado == ing:
                        print("ing 2")
                        tortilla = tortilla2
                        ing.nao_selecionado()
                        pygame.display.update()
                    if ingrediente_selecionado == Ingrediente(GREEN, DARK_GREEN, 100, 350):
                        print("ing 3")
                        tortilla = tortilla3
                        ing.nao_selecionado()
                        pygame.display.update()
                    if ingrediente_selecionado == Ingrediente(BLACK, GRAY, 100, 500):
                        print("ing 4")
                        tortilla = tortilla4
                        ing.nao_selecionado()
                        pygame.display.update()
                    if ingrediente_selecionado == Ingrediente(GOLD, NAVY, 100, 650):
                        print("ing 5")
                        tortilla = tortilla5
                        ing.nao_selecionado()
                        pygame.display.update()
                # if ingrediente_selecionado == ing:
                #     print ("ing 2")
                #     tortilla = tortilla2
                #     pygame.display.update()
                # if ingrediente_selecionado == Ingrediente(GREEN, DARK_GREEN, 100, 350):
                #     print ("ing 3")
                #     tortilla = tortilla3
                #     pygame.display.update()
                # if ingrediente_selecionado == Ingrediente(BLACK, GRAY, 100, 500):
                #     print ("ing 4")
                #     tortilla = tortilla4
                #     pygame.display.update()
                # if ingrediente_selecionado == Ingrediente(GOLD, NAVY, 100, 650):
                #     print ("ing 5")
                #     tortilla = tortilla5
                #     pygame.display.update()
                tortilla.troca_ingrediente(ingrediente_selecionado.letra)

        # if listacomb == []:
        #     vel += 1
        # if num_menu == 1:
        # if num_menu == 2:
        # if num_menu == 3:
        # if num_menu == 4:
        # if num_menu == 5:

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    pygame.display.update()
    fpsClock.tick(FPS)
