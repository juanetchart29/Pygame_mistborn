import pygame
from settings import *
from imagenes import *
from funciones import *
from ModoDesarrollador import *
from Personaje import *
from Plataforma import Plataforma
from Ogros import Ogros
from Reloj import Reloj
from Contador import Contador
from Portal import Portal





#-------SETTINGS-------
pygame.init()

#/------SETTINGS-------
 

lista_plataforma1 = lista_plataforma1
def nivel_1():
    
    
    global lista_plataforma1
    
    #-------PANTALLLA-------
    try:
        fondo_lvl_1 = lista_fondos_lvl_1
        fondo_lvl_1[0]=pygame.image.load(lista_fondos_lvl_1[0])
        
        fondo_lvl_1[0]=pygame.transform.scale(fondo_lvl_1[0],TAMAÑO_PANTALLA)
    except:
        fondo_lvl_1 = fondo_lvl_1[0]
    #----PROTAGONISTA----
    tamaño_personaje = (40,60)
    x_inicial = 50
    y_inicial = H - tamaño_personaje[0] -50

    vin = Personaje(tamaño_personaje,(x_inicial, y_inicial),diccionario_vin,0,"VIN",25,0,lista_proyectil)

    
    #---OGRO---
    ogro1 = Ogros((100,100),(1200,H-130),diccionario_ogro,100,1,"ida_vuelta")
    ogro2 = Ogros((100,100),(390,H-130),diccionario_ogro,50,4,"ida_vuelta")
    ogro3 = Ogros((300,300),(1150, 200),diccionario_ogro,150,5,"ida_vuelta")
    lista_ogros = [ogro1,ogro2,ogro3]
   
    #------MONEDAS-------a
    coin_1 = Coin((30,30),(400,500),path_monedas,20,False)

    coin_2= Coin((30,30),(150,550),path_monedas,20,False)
    coin_3= Coin((30,30),(163, 666),path_monedas,20,False)
    coin_4= Coin((30,30),(258, 666),path_monedas,20,False)
    coin_5= Coin((30,30),(633, 335),path_monedas,20,False)
    coin_6= Coin((30,30),(700, 390),path_monedas,20,False)
    coin_7= Coin((30,30),(1444, 455),path_monedas,20,False)
    coin_8= Coin((30,30),(740, 450),path_monedas,20,False)
    coin_9= Coin((30,30),(900,H-200),path_monedas,20,False)

    coin_10= Coin((30,30),(193, 149),path_moneda_roja,20,True)

    lista_monedas = [coin_1,coin_2,coin_3,coin_4,coin_5,coin_6,coin_7,coin_8,coin_9,coin_10]

    #--PORTAL--
    portal = Portal((50,100),(600,0),path_portal)


    #------Piso-----
    piso = Plataforma((W,20),(0,715),lista_plataforma1)

    #-------plataformas------
    plataforma1 = Plataforma((200,30),(100,600),lista_plataforma1)
    plataforma2 = Plataforma((269,30),(311, 454),lista_plataforma1)
    plataforma3 = Plataforma((200,30),(100,200) ,lista_plataforma1)
    plataforma4 = Plataforma((200,30),(800,200),lista_plataforma1)
    plataforma5 = Plataforma((400,30),(1000,300),lista_plataforma1)
    plataforma7 = Plataforma((100,30),(1400,500),lista_plataforma1)

    plataforma8 = Plataforma((30,130),(100,630),lista_viga1)
    plataforma6 = Plataforma((30,H),(1470,0),lista_viga1)
    plataforma9 = Plataforma((30,300),(550, 482),lista_viga1)
    plataforma10 = Plataforma((200,30),(600,100),lista_plataforma1)
    plataforma11 = Plataforma((30,125),(567, 0),lista_viga1)
    plataforma12 = Plataforma((30,100),(770, 128),lista_viga1)
    lista_plataforma1 = [piso,plataforma1,plataforma2,plataforma3,plataforma4,plataforma5,plataforma6,plataforma7,plataforma8,plataforma9,plataforma10,plataforma11,plataforma12]

    #/-----Piso-----
    

    #------BUCLE------
    cronometro = Reloj(60,(0,0))
    contador = Contador((35,35),(58,0),path_contador,vin)

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
                # print("Posición del clic:", click_position)
                
        lista_teclas = pygame.key.get_pressed()
                
        esta_pisando = piso
        esta_pisando = pisando_plataforma(lista_plataforma1,vin,piso)
        
        if vin._vida >0 :
            
            acciones_personaje(lista_teclas,PANTALLA,fondo_lvl_1,vin,esta_pisando,lista_plataforma1,lista_ogros)
            lista_monedas = enemigos(PANTALLA,lista_ogros,vin,lista_plataforma1,lista_monedas)
            monedas(PANTALLA,lista_monedas,vin)
        else: 
            PANTALLA.blit(fondo_lvl_1[0],(0,0))
            PANTALLA.blit(vin._dict_imagenes["muerta"][0],(vin._rectangulo.x,vin._rectangulo.y+vin._tamaño[1]))
            return 0

            
        cronometro.actualizar()
        cronometro.dibujar(PANTALLA)
        contador.actualizar(vin)
        contador.dibujar(PANTALLA)
        
        blitear_pisos(lista_plataforma1,PANTALLA)   
        
        next_level = level_manager(PANTALLA,portal,vin)
        
        if cronometro.acaba_el_tiempo() == True:
            return 0
        
        if next_level == True:
            set_score(vin._score)
            return 1
            
    
        RELOJ.tick(FPS)
        pygame.display.update()

    

#/-----BUCLE------
