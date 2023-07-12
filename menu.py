
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
    BG_muerte = "src/menu/muerte.png"
    BG_muerte = pygame.image.load(BG_muerte)
    BG_muerte = pygame.transform.scale(BG_muerte,TAMAÑO_PANTALLA)

    while True:
            reloj = pygame.time.Clock()
            MENU_MOUSE_POS = pygame.mouse.get_pos()
            
            FIRST_LVL = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 569), 
                            text_input="Go Menu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
            
            
            
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    return sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if  FIRST_LVL.checkForInput(MENU_MOUSE_POS):
                        return 1
                   
            PANTALLA.blit(BG_muerte,(0,0)) 
            FIRST_LVL.update(PANTALLA)
            
            pygame.display.update()
            reloj.tick(60)
    
                        
                    

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
def top_5(lista_usuarios):
    image_top = pygame.image.load("src/menu/Play Rect.png")
    image_top = pygame.transform.scale(image_top,(600,100))
    while True: 
        font = pygame.font.Font(None, 36)
        reloj = pygame.time.Clock()
        PANTALLA.blit(BG,(0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        PANTALLA.blit(BG,(0,0))
        MENU_BUTTON = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 569), 
                        text_input="Menu", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
      
    
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                 return sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  MENU_BUTTON.checkForInput(MENU_MOUSE_POS):
                    return 1
        
        posicion_x = TAMAÑO_PANTALLA[0]/ 2 -60
        posicion_y = TAMAÑO_PANTALLA[1]/2 -100
        
        PANTALLA.blit(BG,(0,0))
        label_text2 = font.render("RANKING DE MEJORES JUGADORES:", True, (255, 255, 255))
        label_rect2 = label_text2.get_rect()
        label_rect2.center = (posicion_x,posicion_y )
        
        MENU_BUTTON.update(PANTALLA)
        for user_data in lista_usuarios:
            LABEL_BUTTON_USER = Button(image_top, pos=(posicion_x, posicion_y), 
                        text_input=user_data, font=get_font(20), base_color="#d7fcd4", hovering_color="White")
            LABEL_BUTTON_USER.update(PANTALLA)
            posicion_y += 100

                  
        pygame.display.update()
        reloj.tick(60)
    
        
        
                    
                        
            
def input_name(score):
    nombre = ""
    while True:
        font = pygame.font.Font(None, 36)
        reloj = pygame.time.Clock()
        PANTALLA.blit(BG,(0,0))
        
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SEND_NAME = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(1346, 569), 
        text_input="Done", font=get_font(30), base_color="#d7fcd4", hovering_color="White")
        
        TEXT_SCORE = "Tu puntaje fue: " + str(score)
   
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if  SEND_NAME.checkForInput(MENU_MOUSE_POS):
                        return nombre
            if event.type == pygame.KEYDOWN:
                if len(nombre) < 15:
                    nombre += event.unicode
        
        label_text1 = font.render("Ingrese su nombre:", True, (255, 255, 255))
        label_rect1 = label_text1.get_rect()
        label_rect1.center = (TAMAÑO_PANTALLA[0]/ 2 -60, TAMAÑO_PANTALLA[1]/2 -100)
        
        label_text2 = font.render(TEXT_SCORE, True, (255, 255, 255))
        label_rect2 = label_text2.get_rect()
        label_rect2.center = (TAMAÑO_PANTALLA[0]/ 2 -60, TAMAÑO_PANTALLA[1]/2 -200)

        input_name = pygame.Rect((TAMAÑO_PANTALLA[0]/2 - 60, TAMAÑO_PANTALLA[1]//2 , 400, 50))
        pygame.draw.rect(PANTALLA, (0, 0, 0), input_name)  
        texto_superficie = font.render(nombre, True, (255,255, 255))
        PANTALLA.blit(texto_superficie, (input_name.x + 10, input_name.y + 10))
        PANTALLA.blit(label_text1, label_rect1)
        PANTALLA.blit(label_text2, label_rect2)
        
        SEND_NAME.update(PANTALLA)
        

        pygame.display.update()
        reloj.tick(60)
            
            
pygame.display.set_caption("Menu")

def main_menu():
    #imagen del fondo del menu
    nivel_uno = 2
    nivel_dos = 2
    nivel_tres = 2
    #titulo ventana
    while True:
        PANTALLA.blit(BG,(0,0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        MENU_TEXT = get_font(100).render("MISTBORN", True, "#b68f40")
        MENU_RECT = MENU_TEXT.get_rect(center=(720, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("src/menu/Play Rect.png"), pos=(720, 250), 
                            text_input="PLAY", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        OPTIONS_BUTTON = Button(image=pygame.image.load("src/menu/Options Rect.png"), pos=(720, 400), 
                            text_input="TOP_5", font=get_font(75), base_color="#d7fcd4", hovering_color="White")
        QUIT_BUTTON = Button(image=pygame.image.load("src/menu/Quit Rect.png"), pos=(720, 550), 
                            text_input="QUIT", font=get_font(75), base_color="#d7fcd4", hovering_color="White")

        PANTALLA.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)
            button.update(PANTALLA)
        
        if nivel_uno == 0 or nivel_dos == 0 or nivel_tres == 0:
            manager = muerte()
            if manager == 1:
                nivel_tres = 2
                nivel_dos = 2
                nivel_uno = 2
                restart_score()
        
        
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
                                            score = get_score()
                                            nombre = input_name(score)
                                            #SUBO A LA BASE DE DATOS
                                            add_database(nombre,score)
                                            lista_usuarios = get_database()
                                            top_5(lista_usuarios)
                                            

                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                    lista_usuarios = get_database()
                    top_5(lista_usuarios)
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    
                    sys.exit()

        pygame.display.update()

main_menu()
pygame.quit()