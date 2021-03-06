import sys
import random
import pygame
from pygame.locals import*

# Inicializa o jogo

pygame.init()
pygame.font.init()

# Música
musica = 'musicapizza.mp3'
pygame.mixer.init()
pygame.mixer.music.load(musica)

# Arquivo de highscore:
arq = open('HIGHCORES.txt', 'w')

# Variáveis para a quantidade de burritos e highscore
burritos_prontos = 0

# FPS e o Clock
FPS = 120
fpsClock = pygame.time.Clock()

# String Vazia - para carregar a string.png depois
palavra = ''

# Lista com ingredientes individuais
lista_ingredientes = ['salada', 'arroz', 'peixe', 'feijao', 'cogumelo']

# Lista de combinações de menu diferentes
listacomb = random.randint(1, 3)

# Lista de letras
lista_letras = []

# Lista de letras do menu
listatudo = ['A', 'AF', 'AFP', 'AFPC', 'AFPCC', 'S', 'SF',
             'SFA', 'SFAC', 'SFACP', 'S', 'SS', 'SSP', 'SSPC', 'SSPCC']

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
screen = pygame.display.set_mode((1000, 750))

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

DINDIN_IMG_GANHOU = pygame.transform.scale(
    pygame.image.load('ganhoudindin.png'), (100, 100))
DINDIN_IMG_PERDEU = pygame.transform.scale(
    pygame.image.load('perdeudindin.png'), (100, 100))

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
        self.image = self.img_tortilla_vazia
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.screen_rect = screen.get_rect()

        # Carregar as imagens dos burritos com ingredientes
        self.images = {}
        for nome in lista_ingredientes:
            self.images[nome] = pygame.transform.scale(pygame.image.load(
                '{0}.png'.format(nome)), (250, 250))
            self.images[nome].set_colorkey(BLACK)
        self.images['ERRO'] = pygame.image.load('ERRO.png')
# Assim que você clica na tortilla, a imagem é atualizada para o combo.

    # Atualiza a posição do sprite

    def update(self):
        self.rect.x += vel

# Classe da esteira


class Esteira(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        esteira = pygame.image.load('planofundoesteira.png')
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
        self.image = pygame.image.load(image)
        self.image = pygame.transform.scale(self.image, (100, 100))
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
        self.letra = letra

# Classe do pedido (o primeiro burrito vai sempre ser o AFPCC)


class Pedido(pygame.sprite.Sprite):
    def __init__(self, image, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        pedido = pygame.image.load(
            '{0}.png'.format(combcompleto[listacomb-1]))
        self.image = pedido
        self.image = pygame.transform.scale(self.image, (250, 250))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


all_sprites = pygame.sprite.Group()
# Adiciona a esteira na lista de sprites
esteira = Esteira(0, 0)
all_sprites.add(esteira)

# Adiciona os ingredientes em uma lista e define que nenhum ingrediente está selecionado
ingredientes = []
ingredientes.append(Ingrediente('arroz.png', 70, 430, 'A'))
ingredientes.append(Ingrediente('salada.png', 270, 430, 'S'))
ingredientes.append(Ingrediente('cogumelo.png', 470, 430, 'C'))
ingredientes.append(Ingrediente('peixe.png', 650, 430, 'P'))
ingredientes.append(Ingrediente("feijao.png", 830, 430, 'F'))
ingrediente_selecionado = None
for ingrediente in ingredientes:
    all_sprites.add(ingrediente)

# Adiciona a tortilla na lista de sprites
tortilla = Tortilla(bx, by)
all_sprites.add(tortilla)

# Adiciona a campainha na lista de sprites
campainha = Campainha(700, 370)
all_sprites.add(campainha)

# Adiciona o pedido na lista de sprites
pedido = Pedido('AFPCC.png', 740, 160)
all_sprites.add(pedido)

# Adiciona o +100 na lista de sprites
ganhou_dindin = Dindin(DINDIN_IMG_GANHOU, gdx, gdy)
all_sprites.add(ganhou_dindin)

# Adiciona o -100 na lista de sprites
perdeu_dindin = Dindin(DINDIN_IMG_PERDEU, pdx, pdy)
all_sprites.add(perdeu_dindin)

# Tela de fundo
background = pygame.image.load('planofundo.jpg').convert()
background_rect = background.get_rect()

# Fonte
font = pygame.font.SysFont('PressStart2P.ttf', 50, True)
numero = font.render(str(burritos_prontos), False, BLACK)
din = font.render(str(dindin), False, BLACK)

# Carrega a imagem de início
running = True
while running:
    telainicio = pygame.transform.scale(
        pygame.image.load('telainicio.png'), (1000, 750))
    screen.blit(telainicio, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            running = False

screen.blit(telainicio, [0, 0])

instru = True
while instru:
    instrucoes = pygame.transform.scale(
        pygame.image.load('instrucoes.png'), (1000, 750))
    screen.blit(instrucoes, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            instru = False

screen.blit(instrucoes, [0, 0])

instru2 = True
while instru2:
    instrucoes2 = pygame.transform.scale(
        pygame.image.load('instrucoes2.png'), (1000, 750))
    screen.blit(instrucoes2, (0, 0))
    pygame.display.update()
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            instru2 = False

screen.blit(instrucoes2, [0, 0])

pygame.mixer.music.play(-1)
#------------------------------------------------------------#
#------------------------------------------------------------#
nao_campainha = True
t = tortilla.rect

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
                        if tortilla.image != pygame.image.load('ERRO.png'):
                            lista_letras.append(ingrediente_selecionado.letra)
                            palavra += ingrediente_selecionado.letra
                            if palavra in listatudo:
                                tortilla.image = pygame.transform.scale(pygame.image.load(
                                    "{0}.png".format(palavra)), (250, 250))

                            elif palavra not in listatudo:
                                tortilla.image = pygame.image.load('ERRO.png')
                                vel = 50
                            ingrediente_selecionado = None

                if event.type == pygame.MOUSEBUTTONDOWN and ingrediente_selecionado is None:
                    ca = campainha.rect
                    dx, dy = pygame.mouse.get_pos()
                    # Se você clicar na campainha
                    if ca.x <= dx <= ca.x+75 and ca.y <= dy <= ca.y + 75:
                        verifica = all(
                            e in lista_letras for e in lista_menu[listacomb-1])
                        nao_campainha = False
                        if verifica == True:
                            if len(lista_letras) == 5:
                                dindin += 100
                                vel = 50
                                counter += 1
                                listacomb = random.randint(1, 3)
                                dinheiromais = Dindin(
                                    DINDIN_IMG_GANHOU, 500, 400)
                                all_sprites.add(dinheiromais)
                                burritos_prontos += 1
                                numero = font.render(
                                    str(burritos_prontos), False, BLACK)
                                din = font.render(str(dindin), False, BLACK)
                                screen.blit(numero, [340, 10])
                                pygame.display.update()
                        elif verifica == False:
                            dindin -= 100
                            listacomb = random.randint(1, 3)
                            dinheiromenos = Dindin(
                                DINDIN_IMG_PERDEU, 500, 400)
                            all_sprites.add(dinheiromenos)
                            din = font.render(str(dindin), False, BLACK)
                            vel = 50
                            screen.fill(pygame.Color("BLACK"))
                            screen.blit(numero, [340, 10])
                            pygame.display.update()
                            if dindin <= 0:
                                # ADD TO HIGHSCORE
                                # texto = "{0}".format(burritos_prontos)
                                # arq.write(texto)
                                # arq.close()
                                # burrito.kill()
                                 # ADD TO HIGHSCORE
                                arq = open('HIGHCORES.txt', 'w')
                                texto = "{0}".format(burritos_prontos)
                                if burritos_prontos > score:
                                    arq.write(texto)
                                else:
                                    print("Oi")
                                arq.close()

                if t.x > 1000:
                    verifica = all(
                        e in lista_letras for e in lista_menu[listacomb-1])
                    vel = counter
                    palavra = ''
                    lista_letras = []
                    t.x = -200
                    listacomb = random.randint(1, 3)
                    tortilla.image = pygame.transform.scale(
                        tortilla.img_tortilla_vazia, (250, 250))
                    filename = "{0}.png".format(combcompleto[listacomb - 1])
                    pedido.image = pygame.transform.scale(
                        pygame.image.load(filename), (250, 250))
                    if verifica == True:
                        dinheiromais = Dindin(
                            DINDIN_IMG_GANHOU, 500, 400)
                        screen.blit(din, [300, 67])
                        dindin += 100
                        burritos_prontos += 1
                        numero = font.render(
                            str(burritos_prontos), False, BLACK)
                        din = font.render(str(dindin), False, BLACK)
                        pygame.display.flip()
                    elif verifica == False:
                        dinheiromenos = Dindin(
                            DINDIN_IMG_PERDEU, 500, 400)
                        dindin -= 100
                        screen.blit(din, [300, 67])
                        din = font.render(str(dindin), False, BLACK)

        screen.blit(background, background_rect)
        all_sprites.update()
        all_sprites.draw(screen)
        pygame.display.flip()
        screen.blit(numero, [340, 10])
        screen.blit(din, [300, 67])
        fpsClock.tick(FPS)
        pygame.display.update()


except Exception as e:
    print(e)
finally:
    pygame.quit()
    sys.exit(0)
