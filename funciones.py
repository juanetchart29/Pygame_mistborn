import pygame
from Personaje import Personaje
from PersonajePrincipal import  *
from imagenes import *
from Proyectil import Proyectil

# -----BANDERAS------


def actualizar_pantalla(pantalla,fondo:list,un_personaje,proyectil):
    pantalla.blit(fondo[0],(0,0))
    un_personaje.update(pantalla,proyectil)
    proyectil_personaje(proyectil,pantalla)

        
            
            
            



def acciones_personaje(lista_teclas:list,pantalla,fondo:list,un_personaje:Personaje,piso,proyectil):
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
            proyectil._activo = True
                
        if lista_teclas[pygame.K_RIGHT]:
            un_personaje._bandera_lado = "derecha"
            un_personaje._velocidad_x = 20
            un_personaje._que_hace = "corre_d"
        elif lista_teclas[pygame.K_LEFT]:
            un_personaje._bandera_lado = "izquierda"
            un_personaje._velocidad_x = 20
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
                
            un_personaje._velocidad_x = 20
            un_personaje.mover_personaje_x(1)
        elif lista_teclas[pygame.K_LEFT]:
            un_personaje._bandera_lado = "izquierda"
            if un_personaje._velocidad_y < 0:
                un_personaje._que_hace = "salta_i"
            elif un_personaje._velocidad_y > 0:
                un_personaje._que_hace = "cae_i"
                
            un_personaje._velocidad_x = 20
            un_personaje.mover_personaje_x(-1)

    #le aplico siempre gravedad      
    un_personaje.aplicar_gravedad(pantalla,piso)
    
    actualizar_pantalla(pantalla,fondo,un_personaje,proyectil)

    
def cual_pisa(lista_plataformas:list,un_personaje:Personaje,ultimo_pisado):
    for plataforma in lista_plataformas:
        if un_personaje._lados["bottom"].colliderect(plataforma._rectangulo):   
            return plataforma
    return ultimo_pisado



def blitear_lista(lista_objetos:list,pantalla):
        
    for i in range(len(lista_objetos)):
        if i != 0: 
            objeto = lista_objetos[i]
            pantalla.blit(objeto._imagen,objeto._posicion)
            
        
def proyectil_personaje(proyectil:Proyectil,pantalla,lista_pisos):
    if type(proyectil) == Proyectil :
        if proyectil._activo ==  True:
            proyectil.lanzar_proyectil(1)
            pantalla.blit(proyectil._imagen,(proyectil._rectangulo.x,proyectil._rectangulo.y))
            proyectil.desaparecer(lista_pisos)