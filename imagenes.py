import pygame 
import os

pygame.init()


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

vin_empujando_d =["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\proyect derecha\\0.png",
                  "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\proyect derecha\\1.png",
                  "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\proyect derecha\\2.png"]


lista_proyectil =["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\moneda1.png"]

# animacion_moneda_amarilla = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\0.png",
#                     "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\1.png",
#                     "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\2.png",
#                     "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\3.png"
#                     ]
# animacion_moneda_roja = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\4.png",
#                          "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\5.png",
#                          "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\6.png",
#                          "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\7.png"
#                          ]

diccionario_vin = {"quieto_d":vin_quieta_derecha,
                   "quieto_i":vin_quieta_derecha,
                   "corre_d":vin_corriendo_derecha,
                   "corre_i":vin_corriendo_derecha,
                   "salta_d":vin_saltando_d,
                   "salta_i":vin_saltando_d,
                   "suspendido":vin_en_el_aire,
                   "cae_d":vin_callendo_d,
                   "cae_i":vin_callendo_d,
                   "empujando_d":vin_empujando_d,
                   "empujando_i":vin_empujando_d,
                   "super_salto_d":vin_super_salto_d,
                   "super_salto_i":vin_super_salto_d,
                   "ataque_d":vin_atacando_d,
                   "ataque_i":vin_atacando_d                   
}



lista_plataformas = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\\PYGAME_MISTBORN\src\plataformas\plataforma piedra.png"] 
# diccionario_vin = definir_imagenes_dict(diccionario_vin)

#LISTA MONEDAS
path_monedas = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda1.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda2.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda3.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda4.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda5.png"]

path_enemigos_i = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\9.png",
r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\10.png",
r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\11.png"]

path_enemigos_attack_i = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\8.png"]

diccionario_ogro ={"camina_derecha_i":path_enemigos_i,"camina_izquierda":path_enemigos_i,"ataca_derecha_i":path_enemigos_attack_i,"ataca_izquierda":path_enemigos_attack_i} 
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
