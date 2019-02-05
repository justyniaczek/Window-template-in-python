import pygame

#SZEROKOSC I DLUGOSC OKNA
DISPLAYWIDTH = 800
DISPLAYHEIGHT = 600

#INICJALIZUJE PYGAME
pygame.init()
gameDisplay = pygame.display.set_mode((DISPLAYWIDTH, DISPLAYHEIGHT))

intro = True
while (intro):
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    pygame.display.update()
