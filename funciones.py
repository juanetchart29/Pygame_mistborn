import pygame
import sqlite3
from datetime import datetime
from Personaje import Personaje
from imagenes import *
from Proyectil import Proyectil
from Ogros import Ogros
from Arquero import Arquero
from settings import *
from Boos import Boss
from Portal import Portal
from Coin import Coin
# -----BANDERAS------
bandera_tiempo = pygame.time.get_ticks()
cool_down = 7000 #milis
score = 0

pygame.init()
pygame.mixer.init()

def detener_cancion():
    pygame.mixer.music.pause()

def cancion_menu():
    pygame.mixer.music.load("src/musica/menu.mp3")
    pygame.mixer.music.play(-1)
def cancion_nivel():
    pygame.mixer.music.load("src/musica/in_game.mp3")
    pygame.mixer.music.play(-1)


def level_manager(pantalla,portal:Portal,un_personaje):
    portal.funciones_portal(un_personaje,pantalla)
    if portal._next_lvl == True:
        return True
    else:
        return False    

def actualizar_pantalla(pantalla,fondo:list,un_personaje,lista_enemigos,lista_plataformas):
    try:
    
        pantalla.blit(fondo[0],(0,0))
    
    except:
        pantalla.blit(fondo,(0,0))

    un_personaje.update(pantalla,lista_enemigos,lista_plataformas)
    
    
def acciones_personaje(lista_teclas:list,pantalla,fondo:list,un_personaje:Personaje,piso,lista_plataformas,lista_enemigos):
    """
    lee las teclas presionadas y asigna una acciona un_personaje._que_hace luego updeate pantalla
    """
    if un_personaje._vida > 0:   
        #si esta en el piso
        if un_personaje._bandera_suelo :
            if lista_teclas[pygame.K_d]:   

                un_personaje._bandera_ataque = True
            if lista_teclas[pygame.K_a]:
                if un_personaje._bandera_lado == "derecha":
                    un_personaje._que_hace ="empujando_d"
                    
                else: 
                    un_personaje._que_hace = "empujando_i"
                    un_personaje._could_down = True
            
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
            elif lista_teclas[pygame.K_f]:
                if un_personaje._bandera_lado == "izquierda":
                    un_personaje._que_hace = "empujando_a_i"
                else:
                    un_personaje._que_hace = "empujando_a_d"
            
            
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
                if un_personaje._bandera_super_salto == True:
                    if un_personaje._bandera_lado == "derecha":
                        un_personaje._que_hace = "super_salto_d"
                    else:
                        un_personaje._que_hace = "super_salto_i"
                    un_personaje._velocidad_y  = un_personaje._potencia_super_salto
                    un_personaje._bandera_super_salto = False 
               
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

def enemigos(pantalla,lista_enemigos,un_personaje:Personaje,lista_plataformas,lista_monedas):
    lista_enemigos_vivos = filtrar_ogros_vivos(lista_enemigos)        
    for enemigo in lista_enemigos:
        if enemigo._vida > 0:
            if type(enemigo) == Ogros:
                enemigo.accion_enemigo(un_personaje,pantalla,lista_plataformas)
            elif type(enemigo) == Arquero:
                enemigo.accion_enemigo(pantalla,un_personaje,lista_enemigos_vivos)    
            elif type(enemigo) == Boss:
                    enemigo.accion_enemigo(pantalla,lista_plataformas,lista_enemigos,un_personaje)
                    enemigo.mostrar_vida(pantalla)
        else:
            if  type(enemigo)== Arquero:
                enemigo.arquero_muerto(pantalla,un_personaje,lista_enemigos_vivos)
            if type(enemigo)== Ogros:
                if enemigo._vivo == True:
                    nueva_moneda = Coin((30,30),(enemigo._rectangulo.x,enemigo._rectangulo.y),path_monedas,20,False)
                    enemigo._vivo = False
                    lista_monedas.append(nueva_moneda)
            #aca agregar la animacio de muerte del jefe final
            if type(enemigo)== Boss:
                enemigo._vive = False


    return lista_monedas     
        
def derroto_al_jefe(lista_enemigos):
    for enemigo in lista_enemigos:
        if type(enemigo) == Boss and enemigo._vida <= 0 and enemigo._vive == False:
            return True
    return False
         
           
                      
def dropear_ogros(lista_enemigos:list,primer_ogro_posic:tuple,segundo_ogro_posic:tuple):
    global bandera_tiempo
    tiempo_ahora = pygame.time.get_ticks()
    lista_ogros_vivos = filtrar_ogros_vivos(lista_enemigos)

            
    if tiempo_ahora - bandera_tiempo > cool_down and len(lista_ogros_vivos)<3:
        bandera_tiempo = tiempo_ahora
        nuevo_ogro1 = Ogros((103,103),primer_ogro_posic,diccionario_ogro,2,3,"ida")
        nuevo_ogro2 = Ogros((150,150),segundo_ogro_posic,diccionario_ogro,2,3,"vuelta")
        lista_enemigos.append(nuevo_ogro1)
        lista_enemigos.append(nuevo_ogro2)
    return lista_enemigos

def filtrar_ogros_vivos(lista_enemigos:list):
    lista_ogros_vivos = []
    for enemigo in lista_enemigos :
        if type(enemigo) == Ogros and enemigo._vida > 0:
            lista_ogros_vivos.append(enemigo)
    return lista_ogros_vivos
def trampas(lista_trampas:list,lista_enemigos:list,un_personaje,pantalla):
    for trampa in lista_trampas:
        trampa.hacer_daño(un_personaje,lista_enemigos)
        trampa.blitear_trampa(pantalla)
        
def set_score(x):
    global score
    score += x 

def get_score():
    global score
    
    return score

def restart_score():
    global score 
    score = 0
    
#FUNCIONES DE BASE DE DATOS


def add_database(nombre, score):
    tiempo_ahora = datetime.now()
    tiempo_formateado = tiempo_ahora.strftime("%d/%m/%Y")
    tiempo_ahora = str(tiempo_formateado)
    
    with sqlite3.connect("usuarios.db") as conexion:
        try:  
            sentencia = '''
            INSERT INTO Mistborn_users(Nombre, Puntos, Fecha) VALUES (?, ?, ?)
            '''
            conexion.execute(sentencia, (nombre, score, tiempo_ahora))
            # print("Se agregó con éxito.")
        except Exception as e:
            pass
            # print(e)


def get_database():
    lista_usuarios = []
    with sqlite3.connect("usuarios.db") as conexion:
        cursor = conexion.cursor()
        
        sentencia = '''
        SELECT Nombre, Puntos, Fecha
        FROM Mistborn_users
        ORDER BY Puntos DESC
        LIMIT 5
        '''
        
        cursor.execute(sentencia)
        
        resultados = cursor.fetchall()
        
        for row in resultados:
            nombre = row[0]
            puntos = row[1]
            fecha = row[2]
            usuario = f"""{nombre}-{puntos}-{fecha}"""  
            lista_usuarios.append(usuario)  
        return lista_usuarios

