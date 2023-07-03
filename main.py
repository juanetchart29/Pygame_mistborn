import pygame
from settings import *
from imagenes import *
from funciones import *
from ModoDesarrollador import *
from Personaje import *
from Plataforma import Plataforma
#-------CONSTANTES-------






#/------CONSTANTES-------






#-------SETTINGS-------
pygame.init()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)
RELOJ = pygame.time.Clock()
#/------SETTINGS-------
 
#-------PANTALLLA-------
fondo_lvl_1 = lista_fondos_lvl_1
fondo_lvl_1[0]=pygame.image.load(lista_fondos_lvl_1[0])
fondo_lvl_1[0]=pygame.transform.scale(fondo_lvl_1[0],TAMAÑO_PANTALLA)

#/------PANTALLLA-------

#------PERSONAJE--------
flag_lado = "derecha"

contador_pasos = 0

path_personaje = vin_quieta_derecha

tamaño_personaje = (30,80)
x_inicial = W/2 - 300
y_inicial = H - tamaño_personaje[0  ] -50

vin = Personaje(tamaño_personaje,(x_inicial, y_inicial),diccionario_vin,0,"VIN",30,0,50,lista_proyectil)

#/-----PERSONAJE-------

#------MONEDAS-------
coin_uno = Coin((50,50),(400,500),path_monedas,20)

coin_dos = Coin((50,50),(400,H-300),path_monedas,20)
coin_tres= Coin((50,50),(800,H-200),path_monedas,20)

lista_monedas = [coin_dos,coin_tres,coin_uno]
#/-----MONEDAS-------



#------Piso-----
piso = Plataforma((W,20),(0,vin._lados["main"].bottom-1),lista_plataformas)
#/-----Piso-----    

#-------plataformas------
plataforma1 = Plataforma((200,30),(300,400),lista_plataformas)
plataforma2 = Plataforma((200,30),(800,H -100),lista_plataformas)
plataforma3 = Plataforma((200,30),(100,200) ,lista_plataformas)
plataforma4 = Plataforma((200,30),(500,300),lista_plataformas)

lista_plataformas = [piso,plataforma1,plataforma2,plataforma3,plataforma4]

#/-----Piso-----
 

#------BUCLE------

flag = True
while flag:
    RELOJ.tick(FPS)
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
 
    lista_teclas = pygame.key.get_pressed()
            
    esta_pisando = piso
    esta_pisando = pisando_plataforma(lista_plataformas,vin,piso)
    acciones_personaje(lista_teclas,PANTALLA,fondo_lvl_1,vin,esta_pisando)
    
    monedas(PANTALLA,lista_monedas,vin)
    blitear_pisos(lista_plataformas,PANTALLA)   
    if get_modo()==True:
        for lado in piso._lados:
            pygame.draw.rect(PANTALLA,"Blue",piso._lados[lado],1)
        for lado in vin._lados:
            pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1)
        for lado in plataforma1._lados:
            pygame.draw.rect(PANTALLA,"blue",plataforma1._lados[lado],1)  
        for lado in plataforma2._lados:
            pygame.draw.rect(PANTALLA,"red",plataforma2._lados[lado],1)
        for lado in plataforma3._lados:
            pygame.draw.rect(PANTALLA,"orange",plataforma3._lados[lado],1)
        for lado in plataforma4._lados:
            pygame.draw.rect(PANTALLA,"white",plataforma4._lados[lado],1)
        for proyectil in vin._lista_proyectiles:
            if proyectil._activo == True:
                pygame.draw.rect(PANTALLA,"red",proyectil._rectangulo)
        
    
        
  
    pygame.display.update()

    
pygame.quit()
#/-----BUCLE------
