import pygame 


pygame.init()


#fotogramas de las animaciones 

#path fondo de prueba
lista_fondos_lvl_1 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\\PYGAME_MISTBORN\src\fondos\fondo_nocturno.png"]

lista_fondos_lvl_2 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\fondos\NIVEL2.png"]

lista_fondos_lvl_3 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\fondos\NIVEL3 - copia.png"]
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
                        "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\atacando derecha\\5.png" ]

vin_saltando_d = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\subiendo.png"]

vin_en_el_aire = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\suspendida.png"]
vin_callendo_d = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\callendo1.png"]

vin_super_salto_d = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\PYGAME_MISTBORN\\src\\personajes\\VIN\\saltando\\super salto.png"]



vin_empujando_d =["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\proyect derecha\\0.png"]

vin_muriendo = ["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\0.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\1.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\2.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\3.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\4.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\5.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\6.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\7.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\8.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\9.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\10.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\11.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\12.png",
           "C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\13.png"]

vin_muerta = [r"C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\VIN\\muriendo\\13.png"]


lista_proyectil =["C:\\Users\\juane\\OneDrive\\Escritorio\\Programacion-y-labo-1\\MISTBORN\\Pygame_mistborn\\src\\personajes\\coins\\moneda1.png"]

path_trampa = ["src/trampa/0.png"]

path_portal = ["src/portal/0.png"]

lista_viga1 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\vigas\plataforma piedra.png"]
lista_viga2 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\vigas\6 (2).png"]

lista_plataforma1 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\\PYGAME_MISTBORN\src\plataformas\plataforma piedra.png"] 
# diccionario_vin = definir_imagenes_dict(diccionario_vin)
lista_plataforma2 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\plataformas\6 (2).png"]

lista_plataforma3 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\plataformas\4.png"]

lista_viga3 = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\vigas\4.png"]

#LISTA MONEDAS
path_monedas = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda1.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda2.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda3.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda4.png",
        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\moneda5.png"]

path_moneda_roja = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\coins\0.png"]

path_enemigos_i = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\9.png",
r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\10.png",
r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\11.png"]

path_enemigos_attack_i = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\enemigos\8.png"]

path_arquero_quieto = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\ARQUEROS\4.png"]

path_arquero_dispara = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\ARQUEROS\3.png",
                        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\ARQUEROS\0.png",
                        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\ARQUEROS\1.png",
                        r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\ARQUEROS\2.png"]
path_flecha = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\ARQUEROS\6.png"]
path_arquero_muere = [r"C:\Users\juane\OneDrive\Escritorio\Programacion-y-labo-1\MISTBORN\Pygame_mistborn\src\personajes\ARQUEROS\5.png"]

path_vin_empujando_a = ["src/personajes/VIN/vin empujando arriba/0.png"]
path_boos_proyectil = ["src/personajes/jefe final/proyectil jefe final.png"]
path_boos = ["src/personajes/jefe final/jefe final.png"]
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
                   "empujando_a_d":path_vin_empujando_a,
                   "empujando_a_i":path_vin_empujando_a,
                   "super_salto_d":vin_super_salto_d,
                   "super_salto_i":vin_super_salto_d,
                   "ataque_d":vin_atacando_d,
                   "ataque_i":vin_atacando_d,
                   "muriendo":vin_muriendo,
                   "muerta":vin_muerta      }

diccionario_ogro ={"camina_derecha_i":path_enemigos_i,
                   "camina_izquierda":path_enemigos_i,
                   "ataca_derecha_i":path_enemigos_attack_i,
                   "ataca_izquierda":path_enemigos_attack_i} 

diccionario_arquero = {"quieto" : path_arquero_quieto,
                       "dispara":path_arquero_dispara,
                        "muere":path_arquero_muere
                                        }

diccionario_boos = {"enemigo":path_boos}                      



