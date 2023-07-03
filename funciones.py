import pygame
from Personaje import Personaje
from PersonajePrincipal import  *
from imagenes import *
from Proyectil import Proyectil

# -----BANDERAS------


def actualizar_pantalla(pantalla,fondo:list,un_personaje):
    pantalla.blit(fondo[0],(0,0))
    un_personaje.update(pantalla)
    

    
def acciones_personaje(lista_teclas:list,pantalla,fondo:list,un_personaje:Personaje,piso):
    """
    lee las teclas presionadas y asigna una acciona un_personaje._que_hace luego updeate pantalla
    """
    #si esta en el piso
    if un_personaje._bandera_suelo:
        if lista_teclas[pygame.K_SPACE]:
            
            if un_personaje._bandera_lado == "derecha":
                un_personaje._que_hace ="empujando_d"
    
            else: 
                un_personaje._que_hace = "empujando_i"
            
            actualizar_pantalla(pantalla,fondo,un_personaje)
        if lista_teclas[pygame.K_RIGHT]:
            un_personaje._bandera_lado = "derecha"
            un_personaje._velocidad_x = 10
            un_personaje._que_hace = "corre_d"
        elif lista_teclas[pygame.K_LEFT]:
            un_personaje._bandera_lado = "izquierda"
            un_personaje._velocidad_x = 10
            un_personaje._que_hace = "corre_i"
        elif lista_teclas[pygame.K_UP]:
            if un_personaje._bandera_lado == "izquierda":
                un_personaje._que_hace = "salta_i"
            else:
                un_personaje._que_hace = "salta_d"
        else:
            if un_personaje._bandera_lado == "derecha":
                un_personaje._que_hace = "quieto_d"
            else:
                un_personaje._que_hace = "quieto_i"
    #si esta en el aire
    else:
        if lista_teclas[pygame.K_RIGHT]:
            un_personaje._bandera_lado = "derecha"
            if un_personaje._velocidad_y < 0:
                un_personaje._que_hace = "salta_d"
            elif un_personaje._velocidad_y > 0:
                un_personaje._que_hace = "cae_d"
                
            un_personaje._velocidad_x = 10
            un_personaje.mover_personaje_x(1)
        elif lista_teclas[pygame.K_LEFT]:
            un_personaje._bandera_lado = "izquierda"
            if un_personaje._velocidad_y < 0:
                un_personaje._que_hace = "salta_i"
            elif un_personaje._velocidad_y > 0:
                un_personaje._que_hace = "cae_i"
                
            un_personaje._velocidad_x = 10
            un_personaje.mover_personaje_x(-1)

    #le aplico siempre gravedad      
    un_personaje.aplicar_gravedad(pantalla,piso)

    #actualizo la pantalla para las animaciones del personaje
    actualizar_pantalla(pantalla,fondo,un_personaje)

    
def pisando_plataforma(lista_plataformas:list,un_personaje:Personaje,ultimo_pisado):
    for plataforma in lista_plataformas:
        if un_personaje._lados["bottom"].colliderect(plataforma._rectangulo):   
            return plataforma
    return ultimo_pisado



def blitear_pisos(lista_pisos:list,pantalla):
        
    for i in range(len(lista_pisos)):
        if i != 0: 
            objeto = lista_pisos[i]
            pantalla.blit(objeto._imagen,objeto._posicion)




def monedas(pantalla,lista_monedas,un_personaje:Personaje):
    for moneda in lista_monedas:
        if moneda._activo == True:
            moneda.animar_coin(pantalla)
            if moneda._rectangulo.colliderect(un_personaje._rectangulo):
                un_personaje.agarrar_moneda(moneda)

    
    

# def blitear_proyectil(proyectil:Proyectil,pantalla):
#     if type(proyectil) == Proyectil :
#         if proyectil._activo ==  True:
#             pantalla.blit(proyectil._imagen,(proyectil._rectangulo.x,proyectil._rectangulo.y))
#             proyectil.desaparecer()