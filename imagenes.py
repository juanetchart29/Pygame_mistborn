import pygame 


pygame.init()


#fotogramas de las animaciones 

#path fondo de prueba
lista_fondos_lvl_1 = ["src/fondos/fondo_nocturno.png"]

lista_fondos_lvl_2 = ["src/fondos/NIVEL2.png"]

lista_fondos_lvl_3 = ["src/fondos/NIVEL3 - copia.png"]
#path plataformas


#path vin quieta derecha
vin_quieta_derecha = ["src/personajes/VIN/quieta/quieta derecha.png"]

#path vin quieta izquierda
vin_quieta_izquierda = ["src/personajes/VIN/quieta/quieta izquierda.png"]

#path vin corriendo derecha
vin_corriendo_derecha=[
                        "src/personajes/VIN/CORRIENDO/corriendo 1.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 2.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 3.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 4.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 5.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 6.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 7.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 8.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 9.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 10.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 11.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 12.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 13.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 14.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 15.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 16.png",
                        "src/personajes/VIN/CORRIENDO/corriendo 17.png"]



vin_atacando_d =["src/personajes/VIN/atacando derecha/2.png",
                       "src/personajes/VIN/atacando derecha/3.png",
                       "src/personajes/VIN/atacando derecha/4.png",
                       "src/personajes/VIN/atacando derecha/5.png"]

vin_saltando_d = ["src/personajes/VIN/saltando/subiendo.png"]

vin_en_el_aire = ["src/personajes/VIN/saltando/suspendida.png"]
vin_callendo_d = ["src/personajes/VIN/saltando/callendo1.png"]

vin_super_salto_d = ["src/personajes/VIN/saltando/super salto.png"]



vin_empujando_d =["src/personajes/VIN/proyect derecha/0.png"]

vin_muriendo = ["src/personajes/VIN/muriendo/0.png"]

vin_muerta = ["src/personajes/VIN/muriendo/13.png"]


lista_proyectil =["src/personajes/coins/moneda1.png"]

path_trampa = ["src/trampa/0.png"]

path_portal = ["src/portal/0.png"]

lista_viga1 = ["src/vigas/plataforma piedra.png"]
lista_viga2 = ["src/vigas/6 (2).png"]

lista_plataforma1 = ["src/plataformas/plataforma piedra.png"] 

lista_plataforma2 = ["src/plataformas/6 (2).png"]

lista_plataforma3 = ["src/plataformas/4.png"]

lista_viga3 = ["src/vigas/4.png"]

#LISTA MONEDAS
path_monedas = ["src/personajes/coins/moneda1.png",
        "src/personajes/coins/moneda2.png",
        "src/personajes/coins/moneda3.png",
        "src/personajes/coins/moneda4.png",
        "src/personajes/coins/moneda5.png"]


path_contador = ["src/personajes/coins/moneda1.png","src/personajes/VIN/corazon/0.png"]

path_moneda_roja = ["src/personajes/coins/0.png"]

path_enemigos_i = [     "src/personajes/enemigos/9.png",
                        "src/personajes/enemigos/10.png",
                        "src/personajes/enemigos/11.png"]

path_enemigos_attack_i = ["src/personajes/enemigos/8.png"]

path_arquero_quieto = ["src/personajes/ARQUEROS/4.png"]

path_arquero_dispara = ["src/personajes/ARQUEROS/3.png",
                        "src/personajes/ARQUEROS/0.png",
                        "src/personajes/ARQUEROS/1.png",
                        "src/personajes/ARQUEROS/2.png"]
path_flecha = ["src/personajes/ARQUEROS/6.png"]
path_arquero_muere = ["src/personajes/ARQUEROS/5.png"]

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

icono_boss = ["src/personajes/jefe final/0.png"]
diccionario_boos = {"enemigo":path_boos,"icono":icono_boss}                      



