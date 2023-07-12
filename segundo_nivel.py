import pygame
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
from Contador import Contador
from Reloj import Reloj

pygame.init()


def nivel_2():
    fondo_lvl_2 = lista_fondos_lvl_2
    try:
        fondo_lvl_2[0]=pygame.image.load(lista_fondos_lvl_2[0])
    except TypeError:
        fondo_lvl_2[0] = lista_fondos_lvl_2[0]
    fondo_lvl_2[0]=pygame.transform.scale(fondo_lvl_2[0],TAMAÑO_PANTALLA)
    #/FONDO

    #PERSONAJES
    tamaño_personaje = (40,70)
    x_inicial = 50
    y_inicial = H - tamaño_personaje[0] -50

    vin = Personaje(tamaño_personaje,(x_inicial, y_inicial),diccionario_vin,0,"VIN",25,0,lista_proyectil)

    #ENEMIGOS 
    #ogros 

    ogro3 = Ogros((100,100),(100,50),diccionario_ogro,150,5,"ida")
    arquero1 = Arquero((100,100),(1368, 421),diccionario_arquero,path_flecha)
    arquero2= Arquero((100,100),(1368, 220),diccionario_arquero,path_flecha) 
    lista_enemigos = [ogro3,arquero1,arquero2]

    #CONTADOR Y RELOJ 
    cronometro = Reloj(60,(1250,0))
    contador = Contador((35,35),(1300,0),path_contador,vin)



    #COINS
    coin_1 = Coin((30,30),(400,500),path_monedas,20,False)


    coin_1 = Coin((30,30),(604, 680),path_monedas,20,False)
    coin_2= Coin((30,30),(603, 574),path_monedas,20,False)
    coin_3= Coin((30,30),(67, 549),path_monedas,20,False)
    coin_4= Coin((30,30),(279, 445),path_monedas,20,False)
    coin_5= Coin((30,30),(377, 240),path_monedas,20,False)
    coin_6= Coin((30,30),(1405, 655),path_monedas,20,False)
    coin_7= Coin((30,30),(1444, 455),path_monedas,20,False)
    coin_8= Coin((30,30),(740, 450),path_monedas,20,False)
    coin_9= Coin((40,40),(720,H-160),path_moneda_roja,20,True)

    # coin_10= Coin((30,30),(193, 149),path_moneda_roja,20,True) ,coin_10
    lista_monedas = [coin_1,coin_2,coin_3,coin_4,coin_5,coin_6,coin_7,coin_8,coin_9]

    #TRAMPA
    trampa_uno = Trampa((100,50),(550,670),path_trampa)
    trampa_dos = Trampa((100,50),(677,670),path_trampa)

    lista_trampas = [trampa_uno,trampa_dos]
    
    # PORTAL 
    portal = Portal((50,100),(120,30),path_portal)
    
    #PISO
    piso = Plataforma((W,20),(0,715),lista_plataforma1)

    #PLATAFORMAS
    plataforma1 = Plataforma((100,30),(0,600),lista_plataforma2)
    plataforma2 = Plataforma((650,30),(350,300),lista_plataforma2)
    plataforma3 = Plataforma((420,30),(0,150) ,lista_plataforma2)
    plataforma5 = Plataforma((950,30),(208, 497),lista_plataforma2)
    plataforma6 = Plataforma((250,30),(1350,300),lista_plataforma2)
    plataforma9 = Plataforma((250,30),(1350,500),lista_plataforma2)

    plataforma4 = Plataforma((W,30),(0,H-30),lista_plataforma2)
    plataforma7 = Plataforma((30,H),(0,0),lista_viga2)
    plataforma10 = Plataforma((30,H),(W-30,0),lista_viga2)
    plataforma11 = Plataforma((150,30),(639, 150),lista_plataforma2)
    plataforma12 = Plataforma((700,30),(1035, 150),lista_plataforma2)

    plataforma13 = Plataforma((30,160),(639, 0),lista_viga2)
    plataforma8 = Plataforma((30,W-524),(646, 524),lista_viga2)


    lista_pisos = [piso,plataforma1,plataforma2,plataforma3,plataforma4,plataforma5,plataforma6,plataforma7,plataforma8,plataforma9,plataforma10,plataforma11,plataforma12,plataforma13]


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
        lista_enemigos = dropear_ogros(lista_enemigos,(150,50),(W-150,50))
        
        if get_modo()==True:
            for lado in piso._lados:
                pygame.draw.rect(PANTALLA,"Blue",piso._lados[lado],1)
            for lado in vin._lados:
                pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1)
                # if lado == "right":
                #     pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1) 
            for lado in ogro3._lados:
                pygame.draw.rect(PANTALLA,"red",ogro3._lados[lado],1)
            try:
                pygame.draw.rect(PANTALLA,"yellow",vin._rectangulo_ataque,1)
            except :
                print("TODAVIAN NO SE HA ESTABLECIDO EL RECTANGULO DEL ATAQUE, ATACA PARA PONER EL MODO DESARROLLADOR")
            

        lista_teclas = pygame.key.get_pressed()
        
        esta_pisando = piso
        esta_pisando = pisando_plataforma(lista_pisos,vin,piso)
        
        
        if vin._vida > 0 : 
            acciones_personaje(lista_teclas,PANTALLA,fondo_lvl_2,vin,esta_pisando,lista_pisos,lista_enemigos)
            lista_monedas = enemigos(PANTALLA,lista_enemigos,vin,lista_pisos,lista_monedas)
            monedas(PANTALLA,lista_monedas,vin)
        else: 
            PANTALLA.blit(fondo_lvl_2[0],(0,0))
            PANTALLA.blit(vin._dict_imagenes["muerta"][0],(vin._rectangulo.center))
            return 0            

        
        cronometro.actualizar()
        cronometro.dibujar(PANTALLA)
        contador.actualizar(vin)
        contador.dibujar(PANTALLA)
        
        if cronometro.acaba_el_tiempo() == True:
            return 0
        
        
        blitear_pisos(lista_pisos,PANTALLA)
        trampas(lista_trampas,lista_enemigos,vin,PANTALLA)
        for lado in vin._lados:
            pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1)

            
        next_level = level_manager(PANTALLA,portal,vin)
        if next_level == True:
            set_score(vin._score)
            return 1
        
            
    
        RELOJ.tick(FPS)
        pygame.display.update()
    
