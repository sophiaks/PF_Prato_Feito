#PROJETO FINAL
import pygame
#PRIMEIRA PARTE: BACKGROUND
class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        player_img = pygame.image.load(path.join(img_dir, "")).convert()