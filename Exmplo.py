import pygame
import sys
import time
pygame.init()

win = pygame.display.set_mode((500, 500))
pygame.display.set_caption("JOGO")

x = 225
y = 225
width = 50
height = 50

run = True

while run:
    pygame.time.delay(100)

    for event in pygame.event.get():
        keys = pygame.key.get_pressed()
        win.fill((0, 0, 0))  # Fills the screen with black
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()

        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        mx, my = pygame.mouse.get_pos()
        print(mx, my)
        if 225 < mx < 275 and 225 < my < 275:
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                # if "tamanho burrito" < mx < "tamanho burrito" and "tamanho burrito" < my < "tamanho burrito":
            pygame.draw.rect(win, (0, 255, 0), (50, 50, width, height))
            pygame.display.update()
        else:
            pygame.draw.rect(win, (0, 0, 255), (30, 40, width, height))
            pygame.display.update()
pygame.quit()
# A cada loop, redesenha o fundo e os sprites
