import pygame
from settings import *
from imagenes import *
from funciones import *
from ModoDesarrollador import *
from Personaje import *
from Plataforma import Plataforma
from Ogros import Ogros
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

tamaño_personaje = (40,60)
x_inicial = 50
y_inicial = H - tamaño_personaje[0] -50

vin = Personaje(tamaño_personaje,(x_inicial, y_inicial),diccionario_vin,0,"VIN",25,0,50,lista_proyectil)

#/-----PERSONAJE-------
#---OGRO---

ogro1 = Ogros((100,100),(1200,H-130),diccionario_ogro,100,1,"ida_vuelta")
ogro2 = Ogros((100,100),(390,H-130),diccionario_ogro,50,4,"ida_vuelta")
ogro3 = Ogros((200,200),(1090, 200),diccionario_ogro,200,5,"ida_vuelta")

lista_ogros = [ogro1,ogro2,ogro3]
#/--OGRO---
#------MONEDAS-------a
coin_1 = Coin((30,30),(400,500),path_monedas,20)

coin_2= Coin((30,30),(150,550),path_monedas,20)
coin_3= Coin((30,30),(163, 666),path_monedas,20)
coin_4= Coin((30,30),(258, 666),path_monedas,20)
coin_5= Coin((30,30),(633, 335),path_monedas,20)
coin_6= Coin((30,30),(700, 390),path_monedas,20)
coin_7= Coin((30,30),(1444, 455),path_monedas,20)
coin_8= Coin((30,30),(740, 450),path_monedas,20)
coin_9= Coin((30,30),(900,H-200),path_monedas,20)

lista_monedas = [coin_1,coin_2,coin_3,coin_4,coin_5,coin_6,coin_7,coin_8,coin_9]
#/-----MONEDAS-------



#------Piso-----
piso = Plataforma((W,20),(0,715),lista_plataforma1)
#/-----Piso-----    

#-------plataformas------
plataforma1 = Plataforma((200,30),(100,600),lista_plataforma1)
plataforma2 = Plataforma((250,30),(311, 454),lista_plataforma1)
plataforma3 = Plataforma((200,30),(100,200) ,lista_plataforma1)
plataforma4 = Plataforma((200,30),(800,300),lista_plataforma1)
plataforma5 = Plataforma((200,30),(1000,300),lista_plataforma1)
plataforma6 = Plataforma((200,30),(1200,300),lista_plataforma1)
plataforma7 = Plataforma((100,30),(1400,500),lista_plataforma1)

plataforma9 = Plataforma((30,300),(550, 455),lista_viga1)
plataforma8 = Plataforma((30,130),(100,630),lista_viga1)
lista_plataforma1 = [piso,plataforma1,plataforma2,plataforma3,plataforma4,plataforma5,plataforma6,plataforma7,plataforma8,plataforma9]

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
        elif evento.type == pygame.MOUSEBUTTONDOWN:
            # Obtener la posición del clic
            click_position = pygame.mouse.get_pos()
            print("Posición del clic:", click_position)
            
            
            
    lista_teclas = pygame.key.get_pressed()
            
    esta_pisando = piso
    esta_pisando = pisando_plataforma(lista_plataforma1,vin,piso)
    if vin._con_vida :
        
        acciones_personaje(lista_teclas,PANTALLA,fondo_lvl_1,vin,esta_pisando,lista_plataforma1,lista_ogros)
    else: 
        PANTALLA.blit(vin._dict_imagenes["muerta"],(vin._rectangulo.center))
          
                
    monedas(PANTALLA,lista_monedas,vin)
    ogros(PANTALLA,lista_ogros,vin)
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
        
    
        
  
    pygame.display.update()

    
pygame.quit()
#/-----BUCLE------
