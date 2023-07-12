import pygame
from settings import *
from imagenes import *
from funciones import *
from ModoDesarrollador import *
from Personaje import *
from Plataforma import Plataforma
from Reloj import Reloj
from Contador import Contador


pygame.init()


def nivel_3():
    #PERSONAJES
    tamaño_personaje = (40,70)
    x_inicial = 50
    y_inicial = H - tamaño_personaje[0] -50
    vin = Personaje(tamaño_personaje,(x_inicial, y_inicial),diccionario_vin,0,"VIN",25,0,lista_proyectil)

    #BACKGROUND
    fondo_lvl_3 = lista_fondos_lvl_3
    try:
        fondo_lvl_3[0]=pygame.image.load(lista_fondos_lvl_3[0])
    except TypeError:
        fondo_lvl_3[0] = lista_fondos_lvl_3[0]
    fondo_lvl_3[0]=pygame.transform.scale(fondo_lvl_3[0],TAMAÑO_PANTALLA)

    #CRONOMETRO Y RELOJ 
    cronometro = Reloj(60,(0,0))
    contador = Contador((35,35),(58,0),path_contador,vin)

    #PISO
    piso = Plataforma((W+500,30),(0,H-30),lista_plataforma1)

    #PLATAFORMAS
    plataforma1 = Plataforma((100,30),(0,300),lista_plataforma2)
    plataforma2 = Plataforma((100,30),(1400,300),lista_plataforma2)

    plataforma3 = Plataforma((W,30),(0,H-30),lista_plataforma2)
    plataforma7 = Plataforma((40,H),(0,0),lista_viga2)
    plataforma10 = Plataforma((30,H),(W-30,0),lista_viga2)

    lista_pisos = [piso,plataforma3,plataforma1,plataforma2,plataforma7,plataforma10]


    #OGROS
    lista_enemigos=[]

    #JEFE FINAL
    dracula = Boss((400,200),(W/2 - 100,0),diccionario_boos,3,path_boos_proyectil)
    lista_enemigos.append(dracula )

    #MONEDAS
    coin_1 = Coin((30,30),(400,500),path_monedas,20,False)
    lista_monedas = [coin_1]


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
        lista_enemigos = dropear_ogros(lista_enemigos,(100,30),(1350,30))
        
        if get_modo()==True:
            for lado in piso._lados:
                pygame.draw.rect(PANTALLA,"Blue",piso._lados[lado],1)
            for lado in vin._lados:
                pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1)
          
            try:
                pygame.draw.rect(PANTALLA,"yellow",vin._rectangulo_ataque,1)
            except :
                pass

        lista_teclas = pygame.key.get_pressed()
        esta_pisando = piso
        esta_pisando = pisando_plataforma(lista_pisos,vin,piso)
        
        if vin._vida <=0 : 
            acciones_personaje(lista_teclas,PANTALLA,fondo_lvl_3,vin,esta_pisando,lista_pisos,lista_enemigos)
            lista_monedas = enemigos(PANTALLA,lista_enemigos,vin,lista_pisos,lista_monedas)
            monedas(PANTALLA,lista_monedas,vin)
            blitear_pisos(lista_pisos,PANTALLA)
        else: 
            return 0
        
        gana = derroto_al_jefe(lista_enemigos)
        if gana:
            set_score(vin._score)
            return 1
        
        cronometro.actualizar()
        cronometro.dibujar(PANTALLA)
        contador.actualizar(vin)
        contador.dibujar(PANTALLA)
        
        if get_modo():
            for lado in vin._lados:
                pygame.draw.rect(PANTALLA,"yellow",vin._lados[lado],1)
                
            for enemigo in lista_enemigos:
                for lado in enemigo._lados:
                    pygame.draw.rect(PANTALLA,"yellow",enemigo._lados[lado],1)
                    
            
            
        
        
            
    
        RELOJ.tick(FPS)
        pygame.display.update()
    
