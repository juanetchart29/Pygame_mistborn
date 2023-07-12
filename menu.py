
import pygame,sys
from settings import *
from imagenes import *
from funciones import *
from ModoDesarrollador import *
from Personaje import Personaje
from Plataforma import Plataforma
from Ogros import Ogros
from Arquero import Arquero
from Coin import Coin
from Trampa import Trampa
from Boos import Boss
from Button import Button


from tercer_nivel import nivel_3
from segundo_nivel import nivel_2
from primer_nivel import nivel_1




pygame.init()

#fondos del menu
BG = "src/fondos/Background.png"
BG = pygame.image.load(BG)
BG = pygame.transform.scale(BG,TAMAÑO_PANTALLA)
 
introduccion1 = "src/menu/introduction.png"
introduccion1 = pygame.image.load(introduccion1)
introduccion1 = pygame.transform.scale(introduccion1,TAMAÑO_PANTALLA)

introduccion2 = "src/menu/introduccion2.png"
introduccion2 = pygame.image.load(introduccion2)
introduccion2 = pygame.transform.scale(introduccion2,TAMAÑO_PANTALLA)

introduccion3 = "src/menu/prefinal.png"
introduccion3 = pygame.image.load(introduccion3)
introduccion3 = pygame.transform.scale(introduccion3 ,TAMAÑO_PANTALLA)


def get_font(size): # Returns Press-Start-2P in the desired size
    return pygame.font.Font("src/menu/font.ttf", size)

# def ingresar_nombre()

def muerte():
    while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            PANTALLA.blit(BG,(0,0))
            FIRST_LVL = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 569), 
                            text_input="Go Menu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if  FIRST_LVL.checkForInput(MENU_MOUSE_POS):
                        pass
                        
                    

def historia(x):
    if x == 1:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            PANTALLA.blit(introduccion1, (0, 0))
            FIRST_LVL = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 400),
                               text_input="Start", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            BACK_MENU = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(120, 400),
                               text_input="Menu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

            PANTALLA.blit(introduccion1, (0, 0))
            FIRST_LVL.update(PANTALLA)
            BACK_MENU.update(PANTALLA)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if FIRST_LVL.checkForInput(MENU_MOUSE_POS):
                        return 1
                    if BACK_MENU.checkForInput(MENU_MOUSE_POS):
                        return 0

    if x == 2:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            NEXT_LVL = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 400),
                              text_input="Next", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            BACK_MENU = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(120, 400),
                               text_input="Menu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

            PANTALLA.blit(introduccion2, (0, 0))
            NEXT_LVL.update(PANTALLA)
            BACK_MENU.update(PANTALLA)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if NEXT_LVL.checkForInput(MENU_MOUSE_POS):
                        return 1
                    if BACK_MENU.checkForInput(MENU_MOUSE_POS):
                        return 0

    if x == 3:
        while True:
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            PANTALLA.blit(introduccion3, (0, 0))
            LAST_LVL = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 569),
                              text_input="Last", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            BACK_MENU = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(120, 569),
                               text_input="Menu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")

            PANTALLA.blit(introduccion3, (0, 0))
            LAST_LVL.update(PANTALLA)
            BACK_MENU.update(PANTALLA)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if LAST_LVL.checkForInput(MENU_MOUSE_POS):
                        return 1
                    if BACK_MENU.checkForInput(MENU_MOUSE_POS):
                        return 0

    
    
    # muestro la tabla de scores

    # if x == 4:         
    #     while True: 
    #         MENU_MOUSE_POS = pygame.mouse.get_pos()
    #         PANTALLA.blit(BG,(0,0))
    #         LAST_LVL = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 569), 
    #                         text_input="Last", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
    #         BACK_MENU = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(0, 569), 
    #                         text_input="Menu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        
            
    #         for event in pygame.event.get():
    #             if event.type == pygame.QUIT:
    #                 sys.exit()
    #             if event.type == pygame.MOUSEBUTTONDOWN:
    #                 if  LAST_LVL.checkForInput(MENU_MOUSE_POS):
    #                     return 1
    #                 if  BACK_MENU.checkForInput(MENU_MOUSE_POS):
    #                     return 0
    
        
        
                    
                        
            
def input_name():
    nombre = ""
    while True:
        font = pygame.font.Font(None, 36)
        reloj = pygame.time.Clock()
        PANTALLA.blit(BG,(0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SEND_NAME = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 569), 
        text_input="Done", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  SEND_NAME.checkForInput(MENU_MOUSE_POS):
                        return nombre
            if event.type == pygame.KEYDOWN:
                if len(nombre) < 30:
                    nombre += event.unicode
        
        
        
        
        label_text = font.render("Ingrese su nombre:", True, (255, 255, 255))
        label_rect = label_text.get_rect()
        label_rect.center = (TAMAÑO_PANTALLA[0]/ 2 -60, TAMAÑO_PANTALLA[1]/2 -100)
        

        input_name = pygame.Rect((TAMAÑO_PANTALLA[0]/2 - 60, TAMAÑO_PANTALLA[1]//2 , 400, 50))
        pygame.draw.rect(PANTALLA, (0, 0, 0), input_name)  
        texto_superficie = font.render(nombre, True, (255,255, 255))
        PANTALLA.blit(texto_superficie, (input_name.x + 10, input_name.y + 10))
        PANTALLA.blit(label_text, label_rect)
        
        SEND_NAME.update(PANTALLA)
        

        pygame.display.update()
        reloj.tick(60)
            
            
pygame.display.set_caption("Menu")

def main_menu():
    #imagen del fondo del menu
    
    #titulo ventana
    while True:
        PANTALLA.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MISTBORN", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(720, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(720, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("src/menu/Options Rect.png"), pos=(720, 400), 
                            text_input="OPTIONS", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("src/menu/Quit Rect.png"), pos=(720, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        PANTALLA.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(PANTALLA)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    manager = historia(1)
                    if manager == 1:
                        nivel_uno = nivel_1()
                        if nivel_uno == 1:
                            manager = historia(2)
                            if manager == 1:
                                nivel_dos = nivel_2()
                                if nivel_dos == 1:
                                    manager = historia(3)
                                    if manager == 1:
                                        nivel_tres = nivel_3()
                                        if nivel_tres == 1:
                                            nombre = input_name()

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    nivel_1()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    
                    sys.exit()

        pygame.display.update()

main_menu()
pygame.quit()