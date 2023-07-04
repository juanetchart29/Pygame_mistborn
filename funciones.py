import pygame
from Personaje import Personaje
from PersonajePrincipal import  *
from imagenes import *
from Proyectil import Proyectil

# -----BANDERAS------


def actualizar_pantalla(pantalla,fondo:list,un_personaje,lista_enemigos,lista_plataformas):
    pantalla.blit(fondo[0],(0,0))
    un_personaje.update(pantalla,lista_enemigos,lista_plataformas)
    
    
def acciones_personaje(lista_teclas:list,pantalla,fondo:list,un_personaje:Personaje,piso,lista_plataformas,lista_enemigos):
    """
    lee las teclas presionadas y asigna una acciona un_personaje._que_hace luego updeate pantalla
    """
    if un_personaje._vida > 0:   
        #si esta en el piso
        if un_personaje._bandera_suelo:
            if lista_teclas[pygame.K_d]:   
                
                un_personaje._bandera_ataque = True
            # else:
            #     un_personaje._bandera_ataque = False
                
            if lista_teclas[pygame.K_a]:
                if un_personaje._bandera_lado == "derecha":
                    un_personaje._que_hace ="empujando_d"
        
                else: 
                    un_personaje._que_hace = "empujando_i"
            
            elif lista_teclas[pygame.K_RIGHT]:
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
            elif lista_teclas[pygame.K_s]:
                un_personaje._bandera_suelo = False
                if un_personaje._bandera_lado == "derecha":
                    un_personaje._que_hace = "super_salto_d"
                else:
                    un_personaje._que_hace = "super_salto_i"
                un_personaje._velocidad_y  = un_personaje._potencia_super_salto
        #le aplico siempre gravedad      
        un_personaje.aplicar_gravedad(pantalla,piso,lista_plataformas)

        #actualizo la pantalla para las animaciones del personaje
        actualizar_pantalla(pantalla,fondo,un_personaje,lista_enemigos,lista_plataformas)
    else:
        un_personaje._que_hace = "muriendo"
        un_personaje.animacion_especifica(pantalla)

    
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

def ogros(pantalla,lista_ogros,un_personaje:Personaje):
    for ogro in lista_ogros:
        if ogro._vida > 0:
            ogro.accion_enemigo(un_personaje,pantalla)
            # print(ogro._vida)
    

# def blitear_proyectil(proyectil:Proyectil,pantalla):
#     if type(proyectil) == Proyectil :
#         if proyectil._activo ==  True:
#             pantalla.blit(proyectil._imagen,(proyectil._rectangulo.x,proyectil._rectangulo.y))
#             proyectil.desaparecer()