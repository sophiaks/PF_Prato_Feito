import pygame
from os import path
img_dir = path.join(path.dirname(__file__), 'img')
WIDTH = 480  # Largura da tela
HEIGHT = 600  # Altura da tela
FPS = 60  # Frames por segundo
# Define algumas variáveis com as cores básicas
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(
            path.join(img_dir, "cliente.png")).convert()
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10

        screen.fill(BLACK)
        screen.blit(background, background_rect)
        all_sprites.draw(screen)
        pygame.displayflip()


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()
# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Nome do jogo
pygame.display.set_caption("FamFam")
# Carrega o fundo do jogo
background = pygame.image.load(path.join(img_dir, 'planofundo.png')).convert()
background_rect = background.get_rect()
player = Player()
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
# Comando para evitar travamentos.
try:

    # Loop principal.
    running = True
    while running:

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            all_sprites.update()
    # A cada loop, redesenha o fundo e os sprites
    screen.fill(BLACK)
    screen.blit(background, background_rect)
    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()
finally:
    pygame.quit()
