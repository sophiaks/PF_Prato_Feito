keys = pygame.key.get_pressed()
        win.fill((0, 0, 0))  # Fills the screen with black
        pygame.draw.rect(win, (255, 0, 0), (x, y, width, height))
        pygame.display.update()