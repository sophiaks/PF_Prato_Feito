import pygame
WIDTH = 1000  # Largura da tela
HEIGHT = 600  # Altura da tela
FPS = 60  # Frames por segundo
# Define algumas variáveis com as cores básicas
import pygame.locals

# Inicializa o jogo
pygame.init()

# FPS e o Clock
FPS = 120
fpsClock = pygame.time.Clock()

# janela (screen)

screen = pygame.display.set_mode((1000, 750), 0, 32)

pygame.display.set_caption('Burrito Animado')

burrito = pygame.transform.scale(
    (pygame.image.load('tortilla.png')), (100, 100))

bx = -150
by = 400


# cores
BLACK = (0,   0,   0)
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
RED = (255,   0,   0)
GREEN = (0, 255,   0)
BLUE = (0,   0, 255)
OLIVE = (128, 128, 0)

# Classe de ingredientes?

class Ingredientes(pygame.sprite.Sprite):
    larg_ing = 100
    alt_ing = 100

    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(
            path.join(img_dir, "burrito.png")).convert()
        self.image = player_img
        self.image = pygame.transform.scale(player_img, (50, 38))
        self.image.set_colorkey(BLACK)
        self.x = y
        self.y = x
        self.color = color
        self.image = pygame.Surface(
            (Ingredientes.larg_ing, Ingredientes.alt_ing))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.centerx = WIDTH / 2
        self.rect.bottom = HEIGHT - 10
        all_sprites = pygame.sprite.Group()
        screen.fill(BLACK)
        all_sprites.draw(screen)
        pygame.display.flip()
        self.rect.x = self.x
        self.rect.y = self.y


# Inicialização do Pygame.
pygame.init()
pygame.mixer.init()
# Tamanho da tela.
screen = pygame.display.set_mode((WIDTH, HEIGHT))
# Nome do jogo
pygame.display.set_caption("FamFam")
# Carrega o fundo do jogo
all_sprites = pygame.sprite.Group()
# Comando para evitar travamentos.
try:
    # LOOP PRINCIPAL
    running = True
    while running:

        # Processa os eventos (mouse, teclado, botão, etc).
        for event in pygame.event.get():
            all_sprites.update()
            # A cada loop, redesenha o fundo e os sprites
    #screen.blit(background, background_rect)
    # Depois de desenhar tudo, inverte o display.
    pygame.display.flip()
finally:
    pygame.quit()

ing1 = Ingredientes(RED, 100, 150)
ing2 = Ingredientes(BLUE, 100, 450)
ing3 = Ingredientes(GREEN, 100, 750)
all_sprites.add(ing1, ing2, ing3)

screen.fill(WHITE)

# Loop principal

while True:
    bx += 3
    screen.blit(burrito, (bx, by))

    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()

        if event.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            print(mx, my)
            if 150 < mx < 250 and 100 < my < 200:
                ing12 = Ingredientes(OLIVE, 100, 150)
                all_sprites.add(ing12)
                pygame.display.update()
            if 450 < mx < 550 and 100 < my < 200:
                ing13 = Ingredientes(OLIVE, 100, 450)
                all_sprites.add(ing13)
                pygame.display.update()
            if 750 < mx < 850 and 100 < my < 200:
                ing14 = Ingredientes(OLIVE, 100, 750)
                all_sprites.add(ing14)
                pygame.display.update()

    all_sprites.update()
    screen.fill(WHITE)
    all_sprites.draw(screen)
    screen.blit(burrito, (bx, by))
    pygame.display.update()
    fpsClock.tick(FPS)

