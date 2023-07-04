import pygame
from settings import *
from imagenes import *
from funciones import *
from ModoDesarrollador import *
from Personaje import *
from Plataforma import Plataforma
from Ogros import Ogros
from primer_nivel import vin  



#FONDO
fondo_lvl_2 = lista_fondos_lvl_2
fondo_lvl_2[0]=pygame.image.load(lista_fondos_lvl_2[0])
fondo_lvl_2[0]=pygame.transform.scale(fondo_lvl_2[0],TAMAÑO_PANTALLA)
#/FONDO

piso = Plataforma((W,20),(0,715),lista_plataforma1)


#plataformas
lista



flag = True
while flag:
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            flag = False
        elif evento.type == pygame.KEYDOWN:
            if evento.key == pygame.K_TAB:
                cambiar_modo()
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posición del clic
            click_position = pygame.mouse.get_pos()
            print("Posición del clic:", click_position)
    
    lista_teclas = pygame.key.get_pressed()
            
    esta_pisando = piso
    esta_pisando = pisando_plataforma(lista_plataforma1,vin,piso)
    if vin._con_vida :
        
        acciones_personaje(lista_teclas,PANTALLA,fondo_lvl_1,vin,esta_pisando,lista_plataforma1,lista_ogros)
        monedas(PANTALLA,lista_monedas,vin)
        ogros(PANTALLA,lista_ogros,vin)
    else: 
        PANTALLA.blit(vin._dict_imagenes["muerta"],(vin._rectangulo.center))
        RELOJ.tick(FPS)
        
          
                
    blitear_pisos(lista_plataforma1,PANTALLA)   
    if get_modo()==True:
        for lado in piso._lados:
            pygame.draw.rect(PANTALLA,"Blue",piso._lados[lado],1)
        for lado in vin._lados:
            pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1)
            # if lado == "right":
            #     pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1) 
        try:
            pygame.draw.rect(PANTALLA,"yellow",vin._rectangulo_ataque,1)
        except :
            print("TODAVIAN NO SE HA ESTABLECIDO EL RECTANGULO DEL ATAQUE, ATACA PARA PONER EL MODO DESARROLLADOR")
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
        
    
        
  
    RELOJ.tick(FPS)
    pygame.display.update()

    
pygame.quit()