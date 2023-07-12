import pygame

W,H = 1500,750
TAMAÑO_PANTALLA = (W,H)
FPS = 120


PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
RELOJ = pygame.time.Clock()

#fondos del menu
BG = "src/fondos/Background.png"
BG = pygame.image.load(BG)
BG = pygame.transform.scale(BG,TAMAÑO_PANTALLA)
 
introduccion1 = "src/menu/introduccion.png"
introduccion1 = pygame.image.load(introduccion1)
introduccion1 = pygame.transform.scale(introduccion1,TAMAÑO_PANTALLA)

introduccion2 = "src/menu/introduccion2.png"
introduccion2 = pygame.image.load(introduccion2)
introduccion2 = pygame.transform.scale(introduccion2,TAMAÑO_PANTALLA)

introduccion3 = "src/menu/prefinal.png"
introduccion3 = pygame.image.load(introduccion3)
introduccion3 = pygame.transform.scale(introduccion3 ,TAMAÑO_PANTALLA)