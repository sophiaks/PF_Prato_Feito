class Tortillas(pygame.sprite.Sprite):
    larg_tort = 250
    alt_tort = 250

    def __init__(self, color, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.x = y
        self.y = x
        self.color = color
        self.image = pygame.Surface(
            (Tortillas.larg_tort, Tortillas.alt_tort))
        self.image.fill(self.color)
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
