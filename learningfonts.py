import pygame
pygame.init()
wind-pygame.display.set_mode((700,700))


#create different font type

TITLE_FNT=pygame.font.SysFont('comicsans', 80)
MENU_FNT=pygame.font.SysFont('comicsans', 40)
INST_FNT=pygame.font.SysFont('comicsans', 25)
text=TITLE_FNT.render('The Game', 1, (255, 0, 0))
wind.blit(text,)