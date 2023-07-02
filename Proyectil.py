import pygame
from GameObject import GameObject
from settings import *


class Proyectil(GameObject):
    def __init__(self, tamaño: tuple, posicion: tuple, lista_imagen:list,potencia) -> None:
        super().__init__(tamaño, posicion)
        
        self._posicion_inicial = posicion
        
        self._lista_paths = lista_imagen
        self._imagen = self.convertir_imagenes_lista()[0]
        self._rectangulo = self._imagen.get_rect()
        self._rectangulo.x = self._posicion_inicial[0]
        self._rectangulo.y = self._posicion_inicial[1]
        
        self._potencia = potencia

        self._activo = False
        
        #lo lanzo para x positivo o x negativo
    def lanzar_proyectil(self,x):
        self._activo = True
        if x == 1:
            self._rectangulo.x += self._potencia
        else :
            self._rectangulo.x -= self._potencia

    
    

    def get_posicion(self):
        return (self._rectangulo.x,self._rectangulo.y)
    
    def desaparecer(self,lista_pisos):
        if self._rectangulo.x > W or self._rectangulo < 0:
            self._activo = False
            self._rectangulo.x = self._posicion_inicial[0]
        for piso in lista_pisos:
            if self._rectangulo.colliderect(piso):
                self._activo = False
                self._rectangulo.x
                
            
        
        