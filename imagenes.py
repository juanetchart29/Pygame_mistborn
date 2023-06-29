import pygame 
import os

pygame.init()

def girar_imagenes(lista, flip_x, flip_y):
    lista_girada = []
    for imagen in lista:
        
        imagen_girada = pygame.transform.flip(imagen, flip_x, flip_y)  # Girar la imagen cargada
        lista_girada.append(imagen_girada)  # Agregar la imagen girada a la lista
    return lista_girada


#tener cuidado si mis imagenes tienen tamaños distintos usar esta funcion



def definir_imagenes_lista(lista_imagenes:list):
    for imagen in lista_imagenes:
        pygame.image.load(imagen)
    return lista_imagenes


#fotogramas de las animaciones 

#path fondo de prueba
lista_fondos_lvl_1 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\\PYGAME_MISTBORN\src\fondos\fondo_nocturno.png"]

#path plataformas


#path vin quieta derecha
vin_quieta_derecha = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\quieta\\quieta derecha.png"]

#path vin quieta izquierda
vin_quieta_izquierda = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\quieta\\quieta izquierda.png"]

#path vin corriendo derecha
vin_corriendo_derecha=["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 1.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 2.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 3.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 4.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 5.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 6.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 7.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 8.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 9.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 10.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 11.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 12.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 13.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 14.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 15.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 16.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\CORRIENDO\\corriendo 17.png"   
]

vin_atacando_d = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\atacando derecha\\2.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\atacando derecha\\3.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\atacando derecha\\4.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\atacando derecha\\5.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\atacando derecha\\6.png",
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\atacando derecha\\7.png" ]

vin_saltando_d = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\subiendo.png"]

vin_en_el_aire = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\suspendida.png"]
vin_callendo_d = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\callendo1.png"]

vin_super_salto_d = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\super salto.png"]

vin_muerta = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\muerta\\0.png"]




diccionario_vin = {"quieto_d":vin_quieta_derecha,
                   "quieto_i":vin_quieta_derecha,
                   "corre_d":vin_corriendo_derecha,
                   "corre_i":vin_corriendo_derecha,
                   "salta_d":vin_saltando_d,
                   "salta_i":vin_saltando_d,
                   "suspendido":vin_en_el_aire,
                   "cae_d":vin_callendo_d,
                   "cae_i":vin_callendo_d
                   
                   }

lista_plataformas = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\\PYGAME_MISTBORN\src\plataformas\plataforma piedra.png"] 
# diccionario_vin = definir_imagenes_dict(diccionario_vin)



########## pruebas de imagenes ###########
#----imagenes----
# lista_fondos  = cargar_imagenes(lista_fondos,"ff")
# #QUIETO DERECHA E IZQUIERDA
# vin_quieta_derecha= cargar_imagenes(vin_quieta_derecha)
# vin_quieta_izquierda= cargar_imagenes(vin_quieta_izquierda)
# #CORRIENDO DERECHA E IZQUIERDA
# vin_corriendo_derecha = cargar_imagenes(vin_corriendo_derecha)
# vin_corriendo_izquierda = girar_imagenes(vin_corriendo_derecha,True,False)
# #SALTANDO DERECHA E IZQUIERDA
# vin_saltando_d = cargar_imagenes(vin_saltando)
# vin_saltando_i = girar_imagenes(vin_saltando_d,True,False)
# #EN EL AIRE
# vin_en_el_aire = cargar_imagenes(vin_en_el_aire)
# #CALLENDO DERECHA E IZQUIERDA
# vin_callendo_d = cargar_imagenes(vin_callendo)
# vin_callendo_i = girar_imagenes(vin_callendo_d,True,False)

#/---imagenes----
