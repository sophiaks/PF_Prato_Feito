import pygame
import sys
from os import path
from pygame.locals import *
import random
pygame.font.init()
# Inicializa o jogo
pygame.init()
pygame.mixer.init()

# Variável pra ver se o burrito tá pronto:
pronto = False

# FPS e o Clock
FPS = 120
fpsClock = pygame.time.Clock()

# String Vazia - para carregar a string.png depois
palavra = ''

# Lista com ingredientes individuais
lista_ingredientes = ['salada', 'arroz', 'peixe', 'feijao', 'cogumelo']

# Lista de combinações de menu diferentes
listacomb = random.randint(1, 3)
print(listacomb)

# Lista de letras
lista_letras = []

# LISTA DO MENU #
comb1 = ['A', 'F', 'P', 'C', 'C']
comb2 = ['S', 'F', 'A', 'C', 'P']
comb3 = ['S', 'S', 'P', 'C', 'C']
combcompleto = ['AFPCC', 'SFACP', 'SSPCC']
lista_menu = [comb1, comb2, comb3]

# VELOCIDADE #
vel = 1
counter = 1
# Desenha a tela
screen = pygame.display.set_mode((1000, 750), 0, 32)

# Nome do jogo
pygame.display.set_caption('Quatá City Burritos')

# Carrega imagem da campainha
campainha = pygame.transform.scale(
    pygame.image.load('bell.png'), (70, 70))

# Coordenadas iniciais da tortilla
bx = 520
by = -200

# Coordenadas inicias do +100
gdx = 500
gdy = -400

# Coordenadas iniciais do -100
pdx = 500
pdy = -400

# Começa com 1000 de dinheiro
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

DINDIN_IMG_GANHOU = pygame.transform.scale(
    pygame.image.load('ganhoudindin.png'), (100, 100))
DINDIN_IMG_PERDEU = pygame.transform.scale(
    pygame.image.load('perdeudindin.png'), (100, 100))

# score = 0

# assets["score_font"] = pygame.font.Font(path.join(dindin.ttf), 28)
# score_font = assets["score_font"]
# text_surface = score_font.render("{:08d}".format(score), True, NAVY)

# Classe do dinheiro


class Dindin(pygame.sprite.Sprite):
    def __init__(self, img, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.image = img
        self.x = y
        self.y = x
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.rect.y -= 5

# Classe da tortilla


class Tortilla(pygame.sprite.Sprite):

    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)

        self.img_tortilla_vazia = pygame.transform.scale(
            pygame.image.load('tortilla.png'), (250, 250))

        self.x = y
        self.y = x
        # pygame.transform.scale(tortilla, (250, 250))
        self.image = self.img_tortilla_vazia
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen_rect = screen.get_rect()

        # Lista de letras do menu
        lista = ['A', 'AF', 'AFP', 'AFPC', 'AFPCC', 'S', 'SF', 'SFA',
                 'SFAC', 'SFACP', 'S', 'SS', 'SSP', 'SSPC', 'SSPCC']

        # Carregar as imagens dos ingredientes
        self.images = {}
        for nome in lista_ingredientes:
            self.images[nome] = pygame.transform.scale(
                pygame.image.load('{0}.png'.format(nome)), (40, 40))
            self.images[nome].set_colorkey(WHITE)
        self.images['ERRO'] = pygame.transform.scale(
            pygame.image.load('ERRO.png'), (2, 2))

# Assim que você clica na tortilla, a imagem é atualizada para o combo.

    # Atualiza a posição do sprite

    def update(self):
        self.rect.x += vel

    # def troca_ingrediente(self, ingrediente, combo):
    #     self.combo += ingrediente
    #     center = self.rect.center
    #     if self.combo in self.images:
    #         self.image = self.images[self.combo]
    #     else:
    #         self.image = self.images['ERRO']
    #         print("Esse burrito vai pro lixo")
    #     self.rect = self.image
    #     self.rect.center = center


# Classe da esteira
class Esteira(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        esteira = pygame.image.load('planofundoesteira3.png')
        self.image = pygame.transform.scale(esteira, (1000, 850))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

# Classe da campainha


class Campainha(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        campainha = pygame.image.load('bell.png')
        self.image = pygame.transform.scale(campainha, (75, 75))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


# Classe de ingredientes
class Ingrediente(pygame.sprite.Sprite):
    def __init__(self, image, x, y, letra):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.letra = letra


# # Ingrediente fica maior quando selecionado

#     def selecionado(self):
#         self.image = pygame.transform.scale(self.image, (110, 110))
# # Ingrediente fica menor quando não selecionado

#     def nao_selecionado(self):
#         self.image = pygame.transform.scale(self.image, (100, 100))


# Classe do pedido (o primeiro burrito vai sempre ser o AFPCC)


class Pedido(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        pedido = pygame.image.load(
            '{0}.png'.format(combcompleto[listacomb-1])).convert()
        self.image = pedido
        self.image = pygame.transform.scale(self.image, (130, 130))
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


# Adiciona os ingredientes em uma lista e define que nenhum ingrediente está selecionado
all_sprites = pygame.sprite.Group()
ingredientes = []
ingredientes.append(Ingrediente('arroz.png', 70, 430, 'A'))
ingredientes.append(Ingrediente('salada.png', 270, 430, 'S'))
ingredientes.append(Ingrediente('cogumelo.png', 470, 430, 'C'))
ingredientes.append(Ingrediente('peixe.png', 650, 430, 'P'))
ingredientes.append(Ingrediente("feijao.png", 830, 430, 'F'))
for i in ingredientes:
    all_sprites.add(i)
ingrediente_selecionado = None

# Adiciona a esteira na lista de sprites
esteira = Esteira(0, 0)
all_sprites.add(esteira)

# Adiciona a tortilla na lista de sprites
tortilla = Tortilla(bx, by)
all_sprites.add(tortilla)

# Adiciona a campainha na lista de sprites
campainha = Campainha(700, 370)
all_sprites.add(campainha)

# Adiciona o pedido na lista de sprites
pedido = Pedido('AFPCC.png', 820, 205)
all_sprites.add(pedido)

# Adiciona o +100 na lista de sprites
ganhou_dindin = Dindin(DINDIN_IMG_GANHOU, gdx, gdy)
all_sprites.add(ganhou_dindin)

# Adiciona o -100 na lista de sprites
perdeu_dindin = Dindin(DINDIN_IMG_PERDEU, pdx, pdy)
all_sprites.add(perdeu_dindin)

# Tela de fundo
background = pygame.image.load('planofundo1.jpg').convert()
background_rect = background.get_rect()

#------------------------------------------------------------#
#------------------------------------------------------------#


# LOOP PRINCIPAL
try:

    while True:

        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit(0)
        # Se a pessoa clicar com o mouse:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                print(mx, my)
        # Para cada ingrediente na lista de ingredientes, se a pessoa clicar dentro do retângulo do ingrediente
                for ing in ingredientes:
                    r = ing.rect
                    if r.x <= mx and mx <= r.x + 100 and r.y <= my and my <= r.y + 100:
                        ingrediente_selecionado = ing
        # Se clicar e existir um ingrediente selecionado
                if event.type == pygame.MOUSEBUTTONDOWN and ingrediente_selecionado is not None:
                    cx, cy = pygame.mouse.get_pos()
                    t = tortilla.rect
                    # Se clicar dentro da área do burrito:
                    if t.x <= cx and cx <= t.x+250 and t.y <= cy and cy <= t.y + 250:
                        lista_letras.append(ingrediente_selecionado.letra)
                        palavra += ingrediente_selecionado.letra
                        print(palavra)
                        if palavra in lista_letras:
                            tortilla.image = pygame.image.load(
                                "{0}.png".format(palavra))
                        elif palavra not in lista_letras:
                            tortilla.image = pygame.image.load('ERRO.png')
                        ingrediente_selecionado = None

                if event.type == pygame.MOUSEBUTTONDOWN and ingrediente_selecionado is None:
                    ca = campainha.rect
                    dx, dy = pygame.mouse.get_pos()
                    # Se você clicar na campainha
                    if ca.x <= dx <= ca.x+75 and ca.y <= dy <= ca.y + 75:
                        t = tortilla.rect
                        verifica = all(
                            e in lista_letras for e in lista_menu[listacomb-1])
                        if verifica == True:
                            if pronto == False:
                                print("UHUL TÁ CERTO")
                                dindin += 100
                                print("Seu dinheiro: {0}".format(dindin))
                                vel = 50
                                pronto = True
                                counter += 1
                                listacomb = random.randint(1, 3)
                                print("Antes")
                                dinheiromais = Dindin(
                                    DINDIN_IMG_GANHOU, 500, 400)
                                all_sprites.add(dinheiromais)
                                # score +=1
                                print(dinheiromais)
                                print("depois")
                                print(listacomb)
                                # print(score)

                        elif verifica == False:
                            print("Sequência incorreta")
                            dindin -= 100
                            listacomb = random.randint(1, 3)
                            dinheiromenos = Dindin(
                                DINDIN_IMG_PERDEU, 500, 400)
                            all_sprites.add(dinheiromenos)
                            print(listacomb)
                            print("Ihhh... Seu dinheiro: {0}".format(dindin))
                            vel = 50
                            pronto = True
                            if dindin <= 0:
                                print("É sério que você perdeu um jogo tão fácil?")
                                print("Okay né")
                                print('Se quiser tentar de novo roda o jogo aí')
                                burrito.kill()
                            all_sprites.update()
                if t.x > 1000:
                    vel = counter
                    palavra = ''
                    lista_letras = []
                    print(lista_letras)
                    t.x = -200
                    pronto = False
                    listacomb = random.randint(1, 3)
                    tortilla.image = tortilla.img_tortilla_vazia
                    filename = "{0}.png".format(combcompleto[listacomb - 1])
                    pedido.image = pygame.image.load(filename)

        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        fpsClock.tick(FPS)
        pygame.display.update()

# except:
#     pass

finally:
    pygame.quit()
    sys.exit(0)


# Ingrediente('{0}.png'.format(ing), r.x, r.y, Ingrediente.ing.letra)
