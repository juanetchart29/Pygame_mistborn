import pygame
from Enemigo import Enemigo


class Ogros(Enemigo):
    def __init__(self, tamaño: tuple, posicion: tuple, diccionario_imagenes: dict,rango_movimiento_x:int,velocidad:int,tipo:str) -> None:
        super().__init__(tamaño, posicion, diccionario_imagenes)
        self._rango_movimiento = rango_movimiento_x

        self._velocidad = velocidad
        self._vida = 100
        self._daño = 1
        
        self._tipo = tipo
        
        self._que_hace = "camina_derecha_i"


    def accion_enemigo(self,un_personaje,pantalla):
        if self._tipo == "ida_vuelta":    
            if self._velocidad >= 0:
                if self._rectangulo.colliderect(un_personaje._rectangulo):
                    self._que_hace = "ataca_derecha_i"
                    un_personaje._vida -= self._daño
                else:
                    self._que_hace = "camina_derecha_i"
                    self.mover_enemigo_estable()
            else:
                if self._rectangulo.colliderect(un_personaje._rectangulo):
                    self._que_hace = "ataca_izquierda"
                    un_personaje._vida -= self._daño
                else:
                    self._que_hace = "camina_izquierda"
                    self.mover_enemigo_estable()
            
        self.animar_enemigo(pantalla)
            
            
    
    def animar_enemigo(self,pantalla):
    
        imagenes_lista = self._dict_imagenes[self._que_hace]
        largo = len(imagenes_lista)
        if self._contador/4 >= largo:
            self._contador = 0
        animacion = imagenes_lista[self._contador//4]
        pantalla.blit(animacion,(self._rectangulo.x,self._rectangulo.y))
        self._contador += 1
        
            
            

    
    def mover_enemigo_estable(self):  
        if self._rectangulo.x + self._velocidad > self._posicion[0] + self._rango_movimiento:
            self._velocidad *= -1
        if self._rectangulo.x + self._velocidad < self._posicion[0] - self._rango_movimiento:
            self._velocidad *= -1
        
        self._rectangulo.x += self._velocidad
        
    